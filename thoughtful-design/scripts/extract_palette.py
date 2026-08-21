#!/usr/bin/env python3
"""Extract a design palette from photographs.

Pulls grounded fills from images (not a trend ramp). Classifies colors into
grounds, paper, midtones, and accents so they can be used as a brand deck.

Execute this script. Do not reimplement.

Examples:
  python extract_palette.py hero.jpg kitchen.jpg --json
  python extract_palette.py https://images.pexels.com/photos/123/photo.jpg --swatch palette.png
  python extract_palette.py moodboard/*.jpg --css --hero-darken 0.35
"""

from __future__ import annotations

import argparse
import colorsys
import io
import json
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse

USER_AGENT = "thoughtful-design-palette/1.0"


def _require_pillow():
    try:
        from PIL import Image, ImageDraw, ImageOps  # noqa: F401
    except ImportError:
        print(
            "Pillow is required. Install with:\n  pip install -r scripts/requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)


def rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    def chan(c: float) -> float:
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (chan(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def rgb_to_hsl(rgb: tuple[int, int, int]) -> tuple[float, float, float]:
    r, g, b = (x / 255.0 for x in rgb)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h, s, l


def color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5


def darken_rgb(rgb: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    factor = max(0.0, min(1.0, 1.0 - amount))
    return tuple(max(0, min(255, int(c * factor))) for c in rgb)  # type: ignore[return-value]


def load_image(source: str):
    """Load an image from a local path or http(s) URL. Applies EXIF orientation."""
    from PIL import Image, ImageOps

    if source.startswith(("http://", "https://")):
        req = urllib.request.Request(source, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
        except urllib.error.URLError as exc:
            raise SystemExit(f"Failed to fetch image: {source}\n{exc}") from exc
        image = Image.open(io.BytesIO(data))
    else:
        path = Path(source)
        if not path.exists():
            raise SystemExit(f"Image not found: {source}")
        image = Image.open(path)
    image = ImageOps.exif_transpose(image) or image
    return image.convert("RGB")


def extract_colors(
    image,
    n: int = 8,
    sample: int = 240,
    merge_distance: float = 42.0,
) -> list[dict]:
    """Median-cut palette with near-duplicate merge. Returns share-sorted colors."""
    from PIL import Image

    work = image.copy()
    work.thumbnail((sample, sample), Image.Resampling.LANCZOS)
    quantized = work.quantize(colors=max(n + 4, n), method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette() or []
    counts = Counter(quantized.getdata())
    total = sum(counts.values()) or 1

    raw: list[tuple[tuple[int, int, int], int]] = []
    for index, count in counts.items():
        base = index * 3
        if base + 2 >= len(palette):
            continue
        rgb = (palette[base], palette[base + 1], palette[base + 2])
        raw.append((rgb, count))
    raw.sort(key=lambda item: item[1], reverse=True)

    merged: list[list] = []  # [rgb, count]
    for rgb, count in raw:
        placed = False
        for bucket in merged:
            if color_distance(rgb, bucket[0]) <= merge_distance:
                total_count = bucket[1] + count
                bucket[0] = tuple(
                    int((bucket[0][i] * bucket[1] + rgb[i] * count) / total_count)
                    for i in range(3)
                )
                bucket[1] = total_count
                placed = True
                break
        if not placed:
            merged.append([rgb, count])

    merged.sort(key=lambda item: item[1], reverse=True)
    colors = []
    for rgb, count in merged[:n]:
        rgb_t = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
        h, s, l = rgb_to_hsl(rgb_t)
        colors.append(
            {
                "hex": rgb_to_hex(rgb_t),
                "rgb": list(rgb_t),
                "hsl": {
                    "h": round(h * 360, 1),
                    "s": round(s, 3),
                    "l": round(l, 3),
                },
                "luminance": round(relative_luminance(rgb_t), 4),
                "share": round(count / total, 4),
            }
        )
    return colors


def assign_role(color: dict) -> str:
    s = color["hsl"]["s"]
    l = color["hsl"]["l"]
    if l >= 0.82:
        return "paper"
    if l <= 0.18:
        return "ground"
    if s >= 0.38 and 0.22 <= l <= 0.72:
        return "accent"
    if s < 0.14:
        return "muted"
    return "midtone"


def role_groups(colors: Iterable[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {
        "grounds": [],
        "paper": [],
        "midtones": [],
        "muted": [],
        "accents": [],
    }
    for color in colors:
        role = color.get("role") or assign_role(color)
        color["role"] = role
        key = {
            "ground": "grounds",
            "paper": "paper",
            "midtone": "midtones",
            "muted": "muted",
            "accent": "accents",
        }[role]
        if color["hex"] not in groups[key]:
            groups[key].append(color["hex"])
    return groups


def css_variables(groups: dict[str, list[str]], hero_grounds: list[str] | None = None) -> str:
    lines = [":root {"]
    mapping = [
        ("grounds", "--color-ground"),
        ("paper", "--color-paper"),
        ("midtones", "--color-mid"),
        ("muted", "--color-muted"),
        ("accents", "--color-accent"),
    ]
    for group, prefix in mapping:
        for i, hex_value in enumerate(groups.get(group, []), start=1):
            suffix = "" if i == 1 else str(i)
            lines.append(f"  {prefix}{suffix}: {hex_value};")
    if hero_grounds:
        for i, hex_value in enumerate(hero_grounds, start=1):
            suffix = "" if i == 1 else str(i)
            lines.append(f"  --color-hero-ground{suffix}: {hex_value};")
    lines.append("}")
    return "\n".join(lines)


def write_swatch(colors: list[dict], path: Path, width: int = 720, height: int = 96) -> None:
    from PIL import Image, ImageDraw, ImageFont

    if not colors:
        raise SystemExit("No colors to swatch.")
    image = Image.new("RGB", (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    slot = width / len(colors)
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None
    for i, color in enumerate(colors):
        x0 = int(i * slot)
        x1 = int((i + 1) * slot)
        rgb = tuple(color["rgb"])
        draw.rectangle([x0, 0, x1, height], fill=rgb)
        label = color["hex"]
        ink = (255, 255, 255) if color["luminance"] < 0.45 else (20, 20, 20)
        if font:
            draw.text((x0 + 8, height - 22), label, fill=ink, font=font)
    path.parent.mkdir(parents=True, exist_ok=True)
    image.save(path)


def palette_from_images(
    sources: list[str],
    n: int = 8,
    min_share: float = 0.015,
    hero_darken: float = 0.0,
) -> dict:
    """Merge palettes from one or more photos. This is the function to import."""
    _require_pillow()
    per_source = []
    combined: dict[str, dict] = {}

    for source in sources:
        image = load_image(source)
        extracted = extract_colors(image, n=n)
        per_source.append({"source": source, "colors": extracted})
        for color in extracted:
            existing = combined.get(color["hex"])
            if existing:
                existing["share"] = round(existing["share"] + color["share"], 4)
            else:
                combined[color["hex"]] = dict(color)

    merged = sorted(combined.values(), key=lambda c: c["share"], reverse=True)
    if min_share > 0:
        kept = [c for c in merged if c["share"] >= min_share]
        merged = kept or merged[:n]
    merged = merged[:n]
    for color in merged:
        color["role"] = assign_role(color)

    groups = role_groups(merged)
    hero_grounds = []
    if hero_darken > 0:
        seeds = groups["grounds"] or [
            c["hex"] for c in merged if c["hsl"]["l"] < 0.45
        ][:2]
        for hex_value in seeds[:3]:
            hero_grounds.append(rgb_to_hex(darken_rgb(hex_to_rgb(hex_value), hero_darken)))

    notes = []
    if not groups["accents"]:
        notes.append(
            "Weak or missing accents — sample a second mood reference that already "
            "has a punch color, then re-run. Do not invent a trendy ramp."
        )
    if not groups["grounds"]:
        notes.append("No dark grounds found. Prefer a moodier crop, or darken the source photo.")
    if not groups["paper"]:
        notes.append("No paper/cream found. That is fine for a dark identity; add cream later for a clean software beat.")

    return {
        "sources": sources,
        "colors": merged,
        "roles": groups,
        "hero_grounds": hero_grounds,
        "css": css_variables(groups, hero_grounds or None),
        "notes": notes,
    }


def _print_table(result: dict) -> None:
    print(f"Sources: {', '.join(result['sources'])}")
    print(f"{'HEX':<10} {'ROLE':<8} {'SHARE':>6}  {'L':>5}  RGB")
    for color in result["colors"]:
        rgb = tuple(color["rgb"])
        print(
            f"{color['hex']:<10} {color['role']:<8} {color['share']*100:5.1f}%  "
            f"{color['luminance']:5.2f}  {rgb}"
        )
    print("\nRoles")
    for role, values in result["roles"].items():
        print(f"  {role}: {', '.join(values) if values else '—'}")
    if result["hero_grounds"]:
        print(f"  hero_grounds: {', '.join(result['hero_grounds'])}")
    if result["notes"]:
        print("\nNotes")
        for note in result["notes"]:
            print(f"  - {note}")
    print("\nCSS")
    print(result["css"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Extract grounds, paper, midtones, and accents from photographs."
    )
    parser.add_argument("images", nargs="+", help="Local paths or image URLs")
    parser.add_argument("-n", "--colors", type=int, default=8, help="Max colors (default 8)")
    parser.add_argument("--min-share", type=float, default=0.015, help="Drop specks below this share")
    parser.add_argument(
        "--hero-darken",
        type=float,
        default=0.0,
        help="Also emit darkened hero grounds (0-1, e.g. 0.35). Does not replace sampled colors.",
    )
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--css", action="store_true", help="Print CSS variables only")
    parser.add_argument("--swatch", type=Path, help="Write a PNG swatch strip")
    args = parser.parse_args(argv)
    _require_pillow()

    if args.colors < 3 or args.colors > 16:
        print("--colors must be between 3 and 16", file=sys.stderr)
        return 2

    result = palette_from_images(
        args.images,
        n=args.colors,
        min_share=args.min_share,
        hero_darken=args.hero_darken,
    )

    if args.swatch:
        write_swatch(result["colors"], args.swatch)
        if not args.json and not args.css:
            print(f"Wrote swatch: {args.swatch}", file=sys.stderr)

    if args.json:
        print(json.dumps(result, indent=2))
    elif args.css:
        print(result["css"])
    else:
        _print_table(result)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
