---
name: thoughtful-design
description: >-
  Design landing pages and marketing sites that feel built for a specific
  audience: discovery interview first, mood photography (Pexels), palettes
  sampled from images, Frankensteined site flow, and motion as a repeating
  brand system. Use when designing, redesigning, or reviewing websites,
  landing pages, SaaS marketing sites, heroes, visual identity, web branding,
  or when a site feels generic, vibe-coded, soulless, sterile, or mismatched
  to who it claims to serve.
---

# Thoughtful Design

Do not make the site more modern or fancy. Make it feel like it was built
for a specific person in a specific world.

A site can have a clean layout, good animation, and decent visuals and
still feel soulless. The usual failure: **the copy names the audience, then
the design behaves like it has never heard of them.**

The gap to close is not polish. It is **relating to the user and building
trust** — one actionable promise, and a world they recognize.

**Ask before you design.** Read [discovery.md](discovery.md) and run the
interview. Do not skip to components, Pexels, or code.

## Non-negotiables

1. **Interview first.** Fill the discovery brief. Do not invent the
   audience's kitchen, clinic, or workshop to save a turn.
2. **Design the audience's world, not the product's admin UI.**
3. **Photography is not decoration.** Zero images of the user's world is a
   telltale vibe-coded, robotic site.
4. **One heading that promises the job.** Not a feature tour.
5. **Identity before components.** Mood image → palette from those photos,
   type, texture, icons. Not a formula.
6. **Frankenstein structure, then throw away the look.**
7. **Motion is part of the brand.** One or two motifs that repeat.

## Workflow

Copy and track:

```
Thoughtful design:
- [ ] 0. Discovery interview (discovery.md) — block until the brief exists
      (incl. Pexels key gate or user-provided mood images)
- [ ] 1. Confirm audience world + feeling from answers
- [ ] 2. Diagnose the current page (if any)
- [ ] 3. Find mood images (Pexels if keyed, else user files) + extract palette
- [ ] 4. Frankenstein message + site flow
- [ ] 5. Extract wireframe only
- [ ] 6. Translate identity onto each section
- [ ] 7. Define animation visual identity
- [ ] 8. Critique against anti-patterns
```

### 0. Discovery interview

Follow [discovery.md](discovery.md).

- Round 1 is mandatory even if the user says "just go."
- Use AskQuestion for closed questions; chat for promise, URL, objects.
- Skip questions already answered in the prompt.
- Write the filled brief back before touching visuals.

If you cannot picture their physical world after Round 2, ask again. You
are not ready to search images.

### 1. Audience world + feeling

From the brief, lock:

- **Who** (role, setting, time of day, tools they touch)
- **World** (materials, light, mess, craft)
- **Feeling** in 3–5 words
- **Promise** in one sentence: exactly what the product does for them

### 2. Diagnose (existing sites)

Look for:

| Symptom | What it actually means |
|---------|------------------------|
| Copy says who it's for; visuals are generic SaaS | Designed like you've never heard of the audience |
| No photographs anywhere | Vibe-coded / robotic |
| Bright sterile light or typical flat dark | Defaulted to software-template aesthetics |
| Heading lists features or "how to set up" | Talking about the product instead of relating |
| Random monospace / all-sans "safe" type | No personality, no craft analogy |
| Hard cuts between sections | Motion and hierarchy were bolted on |

A compact, clean, feature-forward page can still fail this test.

### 3. Mood images + palette from photos

Start with **one image**, not a palette generator.

Queries describe **place + light + materials**, never the product
category. Good: `dark restaurant kitchen night wood`. Bad: `restaurant
SaaS`, `modern dashboard`.

**Find images (execute, do not rewrite):**

```bash
# SKILL_DIR = folder that contains this SKILL.md
pip install -r "$SKILL_DIR/scripts/requirements.txt"
export PEXELS_API_KEY=...   # https://www.pexels.com/api/

python "$SKILL_DIR/scripts/search_pexels.py" search "QUERY" --orientation landscape --moody --json
python "$SKILL_DIR/scripts/search_pexels.py" moodboard \
  -q "QUERY_A" -q "QUERY_B" -q "QUERY_C" \
  --out ./moodboard --palette
```

`find_images()` and `moodboard()` in `scripts/search_pexels.py` are the
library API. Prefer darker frames (`--moody`). Credit photographers
("Photo by Name on Pexels"). Do not scrape Pexels.

**No `PEXELS_API_KEY`:** follow the photo gate in [discovery.md](discovery.md).
Ask them to set a key **or** provide 4–8 mood images (files, folder paths,
or URLs). Do not search Pexels, invent stock, or proceed to palette /
layout until images are on hand.

If the user is providing photos, put them in a folder and skip search.

**Then pull the palette from those files (execute, do not rewrite):**

```bash
python "$SKILL_DIR/scripts/extract_palette.py" moodboard/*.jpg --json --hero-darken 0.35 --swatch palette.png
```

`palette_from_images()` in `scripts/extract_palette.py` samples the
photos, merges near-duplicates, and roles colors as grounds / paper /
midtones / accents. Use those hexes. If accents are weak, search a second
mood reference that already has punch — do not invent a trendy ramp.

Then finish the deck by hand:

1. Crop, darken, noise, brand name on the best still — taste test.
2. Keep 4–8 frames in the same light.
3. Texture from the world (tools, surfaces) and optionally software
   sitting in that world (tablet on the pass).
4. Sans for UI; serif for the craft analogy from discovery.
5. Accent icons for the 3–4 product jobs.
6. Mark + the same image family.

Details: [patterns.md](patterns.md#visual-identity).

### 4. Frankenstein message + flow

Collage living sites for *message and flow*, not style. Use the donors
from discovery. For each, steal **one job**:

- Hero: who it's for + one promise (scatter objects from their world)
- Proof ribbon: quiet logo marquee
- How it works: large images, not a numbered step UI
- Features: full-bleed color panels, image dominates, **cut ~90% of text**
- Testimonials: extra social proof; less blocky; less chrome
- CTA: heavy bold type, image background, left-aligned
- Footer: close the page; don't compete with the CTA

Zoom out. You should see a Frankenstein. That is the point.

### 5. Extract the wireframe

Keep **only the boxes and order**. Toss borrowed color, type, photo, and
component skin.

```
Hero (promise + audience world)
→ Logo ribbon
→ How it works (big images, who it's for)
→ Features (image-led panels)
→ Social proof
→ CTA (bold, image, left)
→ Footer
```

Adapt jobs to the product. Do not skip "who this is for" on screen one.

### 6. Translate identity onto the wireframe

Same recipe, section by section:

1. **Ground** — palette ground **or** a mood image.
2. **Texture** — noise (helps type contrast), paper, grain, or none for a
   clean software beat.
3. **Type** — split the heading; mix serif / sans from the deck.
4. **Subtext**, then **buttons at least 2×** the heading-to-subtext gap.
5. **Assets** that *feel* scattered but are not:
   - Larger elements **below** (further back)
   - Smaller elements **on top** (closer)
   - **Margin of safety** around the text
6. **Vignette** — darken the edges toward the center.

Contrast sections on purpose (moody hero → cream graph-paper features).

Swapping a new identity into the same wireframe should feel like a
different business. If it doesn't, generic SaaS is still leaking.

Details: [patterns.md](patterns.md#section-recipes).

### 7. Animation visual identity

Two repeating themes, not a unique trick per section. Example: pull-away
as a section is scrolled past + a wash that joins sections. Identity
because they happen **throughout**.

- Direct the eye. Land on the headline.
- Kill hard breaks. Hero exit: objects slide off, type blurs, next panel
  covers so the hero becomes background.
- CTA: the same idea in reverse (bookends).
- Dry middle: timer-rotate important images; slight zoom on hover.

Details: [patterns.md](patterns.md#motion).

### 8. Anti-patterns

- Skipping discovery / inventing the room
- Making it trendier instead of more true to the audience
- Palette from a trend list instead of from photographs
- Pexels queries for "SaaS," "dashboard," or "business people"
- Feature setup copy in the hero; no photography
- Template light mode or generic flat dark as the identity
- All-sans, or a font that belongs to a different craft
- Copying a reference site's look
- Feature walls of text; tiny screenshots
- Blocky testimonial cards with extra headers
- Random scatter that crowds the headline
- Equal-size objects on one plane
- Buttons tucked under the heading like body leading
- Animation only in the hero, or a new gimmick every section

## Implementation notes (web)

- Real photographs. Do not ship illustration-only or gradient-only heroes
  to avoid finding images.
- Overlay: noise + edge vignette.
- Stack: image → dim/crop → noise → large objects → text → small objects.
- Type: one sans + one serif. Split headlines for the promise.
- Credit Pexels photographers when those files are used.
- Shared primitives (type, radius, button, overlay) so art direction can
  change without the page falling apart.

## Output format

1. **Filled discovery brief** (from [discovery.md](discovery.md))
2. **Diagnosis** if a current site exists
3. **Mood queries + selected frames** (ids, attribution)
4. **Palette** from `extract_palette.py` (roles + any human edits)
5. **Visual identity** — type pairing, texture, icons, mark
6. **Frankenstein map** — donors and jobs
7. **Wireframe** — ordered sections
8. **Section recipes** — ground, texture, type, layering, vignette
9. **Motion identity** — two motifs; bookends; mid-page
10. **Risks** — leftover generic SaaS habits

## Utility scripts

Run from the folder that contains this `SKILL.md` (`SKILL_DIR`). Requires
Pillow; Pexels search also needs `PEXELS_API_KEY`.

| Script | When to execute |
|--------|-----------------|
| [scripts/search_pexels.py](scripts/search_pexels.py) | After the world brief. `search`, `download`, `moodboard`. |
| [scripts/extract_palette.py](scripts/extract_palette.py) | After you have local (or URL) photos. Palette + optional swatch. |

Install: `pip install -r "$SKILL_DIR/scripts/requirements.txt"`

## Additional resources

- Interview script: [discovery.md](discovery.md)
- Section recipes, layering, motion: [patterns.md](patterns.md)
- Worked teardown (restaurant SaaS): [examples.md](examples.md)
