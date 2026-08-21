# Thoughtful Design — Patterns

Read this when executing a section, choosing type/color/texture, or
defining motion. Keep [SKILL.md](SKILL.md) as the workflow.

## Visual identity

### Mood before palette

Do not start in sterile light mode or typical flat dark mode. Start with
a photograph that already has the feeling.

Process:

1. Build Pexels queries from the discovery brief: place + light +
   materials. Run `scripts/search_pexels.py` (`find_images` / `moodboard`).
2. One hero mood crop (audience world, not a product screenshot).
3. Darken + grain/noise + brand wordmark on top — this is the taste test.
4. 4–8 more frames in the same light, palette, and grit.
5. Sample fills with `scripts/extract_palette.py` (`palette_from_images`).
   Use grounds / paper / midtones / `--hero-darken` for hero fills.
6. Accents: 1–2 colors that punch on those darks. If the script reports
   weak accents, search a second mood still that already has punch — not
   a generic ramp.
7. Texture plates: a surface from their craft, and optionally one
   "software in that world" object (tablet on a pass, laptop on a desk).
8. Type pairing: sans for clarity; serif for the craft analogy from
   discovery (menu, editorial, invitation, ledger).
9. 3–5 icons, drawn in the accent, one per core job.

If the mood crop with the wordmark on it does not already feel like the
brand, do not proceed to layout.

### Pexels query shape

| Do | Don't |
|----|--------|
| `dark restaurant kitchen night wood` | `restaurant saas` |
| `freelancer desk keyboard late lamp` | `modern software dashboard` |
| `clinic hallway quiet morning light` | `healthcare technology` |

Filter with `--moody` so average color stays dark. Keep photographer
attribution. Landscape for grounds; mixed orientations for scatter objects.

### Type pairing

| Role | Default | Notes |
|------|---------|--------|
| Display / promise | Serif *or* mixed | Personality; split across lines |
| Body / UI | Sans | Keep the current good sans if it works |
| Meta / labels | Sans, smaller | Do not default to monospace unless the craft is code/log-like |

Drop a font that only signals "tech" when the craft is not tech.

### Texture

| Goal | Treatment |
|------|-----------|
| Moody, analog, trust | Image + noise + vignette |
| Contrast for type on photos | Stronger grain |
| Clean software beat | Cream/paper, **no** noise, optional graph grid |
| Craft object | Photograph of tools/materials, not an icon of them |

## Frankensteining

You are assembling **jobs**, not a moodboard for copying.

| Page job | What to steal | What to discard |
|----------|---------------|-----------------|
| Hero | Single promise; audience cue in the first screen | Their art direction, product chrome |
| Proof | Continuous logo ribbon / marquee | Their logo style |
| How it works | Big imagery, low step-ness | Numbered tutorial UI, small icons-as-steps |
| Features | Full-screen color tabs/panels; image scale | 90% of the text; tiny UI shots |
| Proof (human) | Quotes with room to breathe | Rules, kicker lines, equal card grid |
| CTA | Heavy type as the layout | Centered generic banner; flat fill |

After collage: trace boxes. Delete everything else.

## Section recipes

### Hero

**Job:** Relate instantly. Promise the product in one line. Show who
it's for without saying "for X" as a substitute for pictures.

- Ground: darkened mood image (or identity color if the image is the
  scatter, not the fill).
- Headline: one actionable promise of what the software **does**.
- Split the line like the identity, not like a balanced typesetting
  exercise.
- Subtext: who/where, not a feature list.
- Buttons ≥ 2× the heading→subtext gap.
- Scatter objects from the audience world (plates, tickets, tools,
  laptops — whatever is true).
- Depth: large pieces behind, small pieces in front.
- Margin of safety: no object kisses the type.
- Vignette toward the headline.

### Logo ribbon

**Job:** Quiet proof. Keep it moving so it does not become a graveyard.

- Thin band. Rotating/marquee.
- Does not compete with the hero promise.

### How it works

**Job:** Explain the product while repeating who uses it.

- Less step-like than a 1-2-3 tutorial.
- Images **way bigger** than software-site defaults.
- Background photos from the same identity family.
- Mid-size type (not hero scale, not caption scale).
- Stronger noise if the ground is photographic.

### Features

**Job:** A few jobs, felt — not a catalog.

- Full-bleed colored panels or tabs (one atmosphere per job).
- Image dominates the panel.
- Cut copy until it hurts (~90% gone).
- Identity icons, not generic stroke icon packs.
- Optional contrast beat: cream, no noise, graph-paper, huge shots —
  "software" without leaving the brand.

### Testimonials

**Job:** Extra proof beyond logos.

- Not blocky equal cards.
- No extra heading chrome, rules, or kicker rows above the quotes.
- Type and photos should still belong to the identity.

### CTA

**Job:** Bookend. Demand a decision.

- Heavy, bold type as the primary layout element.
- Image from the identity as ground (not a flat brand fill).
- Left-aligned.
- Motion is the hero's exit **reversed**.

### Footer

**Job:** Land the zoom-out. Utility, not a new campaign.

- After a loud CTA, keep it simple.
- Same type and color language; no new personality.

## Layering (hero and image sections)

Feel: scattered, accidental. Reality: stacked and protected.

```
back  image ground (cropped, darkened)
      large objects (low in the frame / lower z)
      noise
      type + buttons  ← margin of safety on all sides
      small objects (higher z, overlapping edges, not type)
front edge vignette
```

Never:

- Same-size stickers on one layer
- Objects overlapping the promise
- Bright, even lighting with no center pull

## Motion

### Build a motif pair

Pick two themes and reuse them:

1. **Section ownership** — outgoing section recedes (slide, scale, blur);
   incoming section covers it.
2. **Joinery** — something continuous between sections (gradient wash,
   shared color bleed, overlap) so the page is one environment.

If a motion happens once, it is decoration. If it happens in every major
transition, it is identity.

### Focal point

| Moment | Focal point | Motion |
|--------|-------------|--------|
| Land | Headline | World can be still or breathing slightly |
| Leave hero | Next section | Objects slide off; type blurs; next panel covers |
| Mid features | Each featured image | Timer rotation; hover zoom (small) |
| Arrive CTA | Bold promise | Reverse of hero exit |

Avoid a hard horizontal cut that dumps a new background with no
handoff.

### Mid-page dryness

When four (or n) images all matter, do not rely on scroll luck:

- Auto-advance on a timer
- Pause on hover/focus
- Slight zoom on hover so inspection feels intended

## Identity swap test

Same wireframe. New mood crop, palette-from-photos, type pair, textures.

If the page does not feel like a different business, the layout is still
carrying generic SaaS defaults. Strip them and put the identity back in
the grounds, type, and objects.
