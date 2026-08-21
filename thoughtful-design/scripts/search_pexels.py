#!/usr/bin/env python3
"""Find and download Pexels photographs of the audience's world.

Search queries must describe a physical place, light, and materials — not the
product category ("restaurant kitchen night wood", not "restaurant SaaS").

Requires PEXELS_API_KEY (https://www.pexels.com/api/).

Execute this script. Do not scrape Pexels and do not reimplement the client.

Examples:
  python search_pexels.py search "dark restaurant kitchen night" --orientation landscape --moody
  python search_pexels.py download 123 456 --out ./moodboard
  python search_pexels.py moodboard -q "moody dining room" -q "restaurant pass night" --out ./moodboard --palette
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API_ROOT = "https://api.pexels.com/v1"
USER_AGENT = "thoughtful-design-pexels/1.0"


def load_api_key(explicit: str | None = None) -> str:
    if explicit:
        return explicit.strip()
    env = os.environ.get("PEXELS_API_KEY", "").strip()
    if env:
        return env
    for candidate in (Path(".env"), Path(".env.local")):
        if not candidate.exists():
            continue
        for line in candidate.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            if key.strip() == "PEXELS_API_KEY":
                return value.strip().strip('"').strip("'")
    raise SystemExit(
        "Missing PEXELS_API_KEY.\n"
        "Get a free key at https://www.pexels.com/api/ then:\n"
        "  export PEXELS_API_KEY=your_key\n"
        "or pass --api-key. Do not scrape Pexels instead."
    )


def _request(path: str, api_key: str, params: dict | None = None) -> dict:
    url = path if path.startswith("http") else f"{API_ROOT}{path}"
    if params:
        url += ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": api_key,
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
            remaining = resp.headers.get("X-Ratelimit-Remaining")
            if remaining is not None:
                payload["_rate_limit_remaining"] = remaining
            return payload
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code == 401:
            raise SystemExit("Pexels rejected the API key (401). Check PEXELS_API_KEY.") from exc
        if exc.code == 429:
            raise SystemExit("Pexels rate limit hit (429). Wait and retry.") from exc
        raise SystemExit(f"Pexels HTTP {exc.code}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"Network error talking to Pexels: {exc}") from exc


def hex_luminance(value: str | None) -> float | None:
    if not value:
        return None
    h = value.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)

    def chan(c: float) -> float:
        c = c / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * chan(r) + 0.7152 * chan(g) + 0.0722 * chan(b)


def normalize_photo(photo: dict) -> dict:
    avg = photo.get("avg_color")
    luma = hex_luminance(avg)
    photographer = photo.get("photographer") or "unknown"
    page_url = photo.get("url") or ""
    return {
        "id": photo.get("id"),
        "alt": photo.get("alt") or "",
        "width": photo.get("width"),
        "height": photo.get("height"),
        "photographer": photographer,
        "photographer_url": photo.get("photographer_url"),
        "page_url": page_url,
        "avg_color": avg,
        "luminance": round(luma, 4) if luma is not None else None,
        "src": photo.get("src") or {},
        "attribution": f"Photo by {photographer} on Pexels",
        "attribution_html": (
            f'Photo by <a href="{page_url}">{photographer}</a> on '
            f'<a href="https://www.pexels.com/">Pexels</a>'
        ),
    }


def find_images(
    query: str,
    api_key: str | None = None,
    *,
    orientation: str | None = "landscape",
    color: str | None = None,
    locale: str | None = None,
    page: int = 1,
    per_page: int = 15,
    moody: bool = False,
    max_luminance: float = 0.45,
) -> dict:
    """Search Pexels. Returns normalized photos plus pagination. Import this."""
    key = load_api_key(api_key)
    params: dict[str, str | int] = {
        "query": query,
        "page": page,
        "per_page": min(max(per_page, 1), 80),
    }
    if orientation:
        params["orientation"] = orientation
    if color:
        params["color"] = color
    if locale:
        params["locale"] = locale

    payload = _request("/search", key, params)
    photos = [normalize_photo(p) for p in payload.get("photos") or []]
    if moody:
        photos.sort(key=lambda p: p["luminance"] if p["luminance"] is not None else 1.0)
        photos = [
            p
            for p in photos
            if p["luminance"] is None or p["luminance"] <= max_luminance
        ]

    return {
        "query": query,
        "page": payload.get("page", page),
        "per_page": payload.get("per_page", per_page),
        "total_results": payload.get("total_results", 0),
        "next_page": payload.get("next_page"),
        "rate_limit_remaining": payload.get("_rate_limit_remaining"),
        "photos": photos,
        "attribution_required": "Photos provided by Pexels — credit each photographer.",
    }


def get_photo(photo_id: int, api_key: str | None = None) -> dict:
    key = load_api_key(api_key)
    payload = _request(f"/photos/{photo_id}", key)
    return normalize_photo(payload)


def download_photo(
    photo: dict,
    dest_dir: Path,
    size: str = "large2x",
    api_key: str | None = None,
) -> Path:
    src = photo.get("src") or {}
    url = src.get(size) or src.get("large") or src.get("original")
    if not url:
        # Fetch full record if this was a bare id wrapper
        if photo.get("id") and not src:
            photo = get_photo(int(photo["id"]), api_key=api_key)
            src = photo.get("src") or {}
            url = src.get(size) or src.get("large") or src.get("original")
    if not url:
        raise SystemExit(f"No download URL for photo {photo.get('id')}")

    dest_dir.mkdir(parents=True, exist_ok=True)
    slug = "".join(ch if ch.isalnum() else "-" for ch in (photo.get("alt") or "")[:40]).strip("-")
    filename = f"{photo['id']}{('-' + slug) if slug else ''}.jpg"
    dest = dest_dir / filename

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        dest.write_bytes(resp.read())

    meta = dest.with_suffix(".json")
    meta.write_text(json.dumps(photo, indent=2), encoding="utf-8")
    return dest


def moodboard(
    queries: list[str],
    dest_dir: Path,
    api_key: str | None = None,
    *,
    per_query: int = 4,
    orientation: str | None = "landscape",
    moody: bool = True,
    size: str = "large2x",
) -> dict:
    """Search several world-queries, download a tight set, return paths + photos."""
    key = load_api_key(api_key)
    seen: set[int] = set()
    saved: list[dict] = []
    for query in queries:
        result = find_images(
            query,
            api_key=key,
            orientation=orientation,
            per_page=min(20, max(per_query * 3, 8)),
            moody=moody,
        )
        picked = 0
        for photo in result["photos"]:
            if photo["id"] in seen:
                continue
            path = download_photo(photo, dest_dir, size=size, api_key=key)
            seen.add(photo["id"])
            saved.append({"query": query, "path": str(path), "photo": photo})
            picked += 1
            if picked >= per_query:
                break
        if picked == 0:
            saved.append({"query": query, "path": None, "photo": None, "warning": "no matches"})
    return {"out": str(dest_dir), "items": saved}


def _print_search(result: dict) -> None:
    photos = result["photos"]
    print(
        f"query: {result['query']}  "
        f"shown: {len(photos)}  total: {result['total_results']}  "
        f"rate_remaining: {result.get('rate_limit_remaining')}"
    )
    if not photos:
        print(
            "No photos. Use a more specific physical-world query "
            "(place + light + materials), not a product category."
        )
        return
    print(f"{'ID':<10} {'LUMA':>6} {'AVG':<8}  ALT / PHOTOGRAPHER")
    for photo in photos:
        luma = f"{photo['luminance']:.2f}" if photo["luminance"] is not None else "—"
        alt = (photo["alt"] or "(no alt)")[:64]
        print(
            f"{photo['id']:<10} {luma:>6} {str(photo['avg_color'] or '—'):<8}  "
            f"{alt}  — {photo['photographer']}"
        )
        print(f"           {photo['page_url']}")
    print(f"\n{result['attribution_required']}")


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--api-key", help="Pexels API key (else PEXELS_API_KEY)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Find Pexels photos of an audience's physical world."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    search_p = sub.add_parser("search", help="Search photos")
    search_p.add_argument("query")
    search_p.add_argument("--orientation", choices=["landscape", "portrait", "square"])
    search_p.add_argument("--color", help="red, brown, black, #1a1410, ...")
    search_p.add_argument("--page", type=int, default=1)
    search_p.add_argument("--per-page", type=int, default=15)
    search_p.add_argument("--moody", action="store_true", help="Prefer darker avg_color")
    search_p.add_argument("--max-luminance", type=float, default=0.45)
    search_p.add_argument("--json", action="store_true")
    _add_common(search_p)

    get_p = sub.add_parser("get", help="Fetch one photo by id")
    get_p.add_argument("photo_id", type=int)
    get_p.add_argument("--json", action="store_true")
    _add_common(get_p)

    dl_p = sub.add_parser("download", help="Download photo ids")
    dl_p.add_argument("photo_ids", nargs="+", type=int)
    dl_p.add_argument("--out", type=Path, default=Path("moodboard"))
    dl_p.add_argument(
        "--size",
        default="large2x",
        choices=["original", "large2x", "large", "medium", "landscape"],
    )
    _add_common(dl_p)

    board_p = sub.add_parser("moodboard", help="Search several queries and download")
    board_p.add_argument("-q", "--query", action="append", required=True, dest="queries")
    board_p.add_argument("--out", type=Path, default=Path("moodboard"))
    board_p.add_argument("--per-query", type=int, default=4)
    board_p.add_argument("--orientation", choices=["landscape", "portrait", "square"], default="landscape")
    board_p.add_argument("--no-moody", action="store_true")
    board_p.add_argument("--palette", action="store_true", help="Run extract_palette.py on downloads")
    board_p.add_argument("--json", action="store_true")
    _add_common(board_p)

    args = parser.parse_args(argv)
    key = args.api_key

    if args.cmd == "search":
        result = find_images(
            args.query,
            api_key=key,
            orientation=args.orientation,
            color=args.color,
            page=args.page,
            per_page=args.per_page,
            moody=args.moody,
            max_luminance=args.max_luminance,
        )
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            _print_search(result)
        return 0

    if args.cmd == "get":
        photo = get_photo(args.photo_id, api_key=key)
        print(json.dumps(photo, indent=2) if args.json else json.dumps(photo, indent=2))
        return 0

    if args.cmd == "download":
        saved = []
        for photo_id in args.photo_ids:
            photo = get_photo(photo_id, api_key=key)
            path = download_photo(photo, args.out, size=args.size, api_key=key)
            saved.append(str(path))
            print(f"{photo_id} -> {path}")
            print(f"  {photo['attribution']}")
        return 0

    if args.cmd == "moodboard":
        result = moodboard(
            args.queries,
            args.out,
            api_key=key,
            per_query=args.per_query,
            orientation=args.orientation,
            moody=not args.no_moody,
        )
        paths = [item["path"] for item in result["items"] if item.get("path")]
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            for item in result["items"]:
                if item.get("warning"):
                    print(f"no matches: {item['query']}")
                    continue
                photo = item["photo"]
                print(f"{photo['id']}  {item['path']}")
                print(f"  {photo['attribution']}  (query: {item['query']})")
            print(f"\nPhotos provided by Pexels. Downloaded {len(paths)} files to {args.out}")

        if args.palette and paths:
            scripts = Path(__file__).resolve().parent
            sys.path.insert(0, str(scripts))
            from extract_palette import palette_from_images, _print_table

            palette = palette_from_images(paths, hero_darken=0.35)
            if args.json:
                print(json.dumps({"palette": palette}, indent=2))
            else:
                print("\nPalette from moodboard")
                _print_table(palette)
        elif args.palette and not paths:
            print("No images to extract a palette from.", file=sys.stderr)
            return 1
        return 0

    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit(130)
