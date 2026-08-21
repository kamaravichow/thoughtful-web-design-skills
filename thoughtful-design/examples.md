# Thoughtful Design — Examples

## Restaurant management SaaS (full teardown)

Submitted site: clean, compact, fast to features. By generic standards,
"well designed." Still soulless.

### Discovery brief (what Round 1–3 should have produced)

```
Product: Koa's restaurant management software
Promise: (lock one job — floor / pass / books — not "features for restaurants")
Audience: independent restaurant owners
World: service + back-of-house; low light; wood, metal, linen, tickets, glass
Feeling: moody, warm, analog, in-service
Never: generic SaaS dark UI; no photography; setup-wizard copy in the hero
Existing site: viewer submission (clean, compact, feature-first)
Scope: identity + full landing
Brand locks: keep the working sans; drop the monospace
Photo source: Pexels (or equivalent mood stills)
Type craft: printed menu
CTA: left, heavy type, image ground
Jobs: 3–4 product jobs, image-led panels
Proof on hand: logos + quotes if they exist
Frankenstein donors: Actual → hero promise; Better Stack → logo ribbon;
  Superpowered → how-it-works (less steppy, bigger images);
  Miro → feature tabs; Attio → testimonials (less blocky);
  Wise → CTA type
Motion taste: fluid bookends + mid-page image rotation
```

### Pexels queries + palette

```bash
python scripts/search_pexels.py moodboard \
  -q "dark restaurant kitchen night wood" \
  -q "moody dining room candlelight" \
  -q "restaurant pass tickets metal" \
  -q "tablet on restaurant counter night" \
  --out ./moodboard --palette
```

Use the script's grounds as the dark identity; paper/cream for the clean
software beat; accents only if they already live in the photos.

### Diagnosis

- Copy says it is for **restaurant owners**.
- Design has **never heard of a restaurant**: setup instructions, no
  photographs, no service/kitchen world.
- Heading and body describe the product, not a promise a owner can feel.
- No images anywhere → vibe-coded, robotic.
- Existing sans is usable; monospace fights the craft.

Compare a site that relates: freelancers/agencies get laptops and
keyboards **and** one actionable heading that states exactly what the
software does. That is the gap.

### Audience world + feeling

- Who: independent restaurant owners, service and back-of-house
- World: low light, wood, metal, linen, tickets, glass, late hours
- Feeling: moody, warm, analog, in-service
- Promise: one line for the actual job (run the floor / the pass /
  the books — whichever is true). Not "features for restaurants."

### Visual identity

1. One moody restaurant photograph. Crop, darken, noise, wordmark.
2. More frames in the same light (not bright stock interiors).
3. Palette sampled from those frames (earth, soot, brass, cream).
4. Accents pulled from a similarly moody reference (not a SaaS ramp).
5. Texture: a counter with pots, pans, spoons — or a tablet on that
   same counter so the product still lives in the room.
6. Type: keep the working sans; add a serif like a **printed menu**.
7. Accent icons for the three or four product jobs.
8. Mark in the corner; more of the same image family.

Nothing here is a template. It is what makes sense for that brand.

### Frankenstein (jobs only)

| Section | Borrowed job | Local change |
|---------|--------------|--------------|
| Hero | Single promise, immediate who-it's-for | Scatter restaurant objects, not generic 3D |
| Ribbon | Rotating logo proof | Keep thin and secondary |
| How it works | Explain product with big art | Less step-like; images much larger; kitchen/floor backgrounds |
| Features | Full-screen color tabs | Bigger image; ~90% less text |
| Testimonials | Human proof | No top rules/kickers; less blocky |
| CTA | Heavy bold type as layout | Image ground; left align |
| Footer | Close | Simple |

Zoom out: ugly collage. Trace the wireframe. Delete the rest.

### Translate

**Hero.** Mood image ground. Noise for grit and type contrast. Split
serif/sans lines. Subtext. Buttons at ≥ 2× heading-to-subtext spacing.
Scatter: large dishes/tools low and back, small objects forward. Safety
margin around the promise. Darken edges.

**How it works.** Image grounds, stronger noise, mid-size type. Same
depth rules. Reinforces who uses it, not a setup wizard.

**Features.** Cream, **no** noise (clean software beat). Graph-paper.
Huge images. Identity icons. Copy cut to the bone.

Continue through proof and CTA with the same deck. The page should read
as one restaurant-world product, not a template with food adjectives.

### Motion

- Bookend: hero objects slide off + type blurs as the next section
  covers; CTA uses the reverse.
- Middle: feature images on a timer; slight zoom on hover.
- No hard cut between hero and the rest.

### Identity swap

Keep this wireframe. Drop in a different mood family (e.g. clinic,
workshop, studio). The feeling on load should change completely. If it
does not, generic SaaS structure is still leaking through.

---

## Quick contrast: "pretty" vs thoughtful

| Pretty / typical | Thoughtful |
|------------------|------------|
| Clean layout, trendy motion, stock-safe dark UI | Looks like the customer's actual room |
| "For restaurant owners" as a label | Kitchen, service, materials, light |
| Feature grid in the first screen | One promise + world |
| No photos (or generic gradients) | Mood crops as identity |
| All sans, optional mono | Sans + craft serif |
| Copied Awwwards skin | Copied flow, original identity |
| Animation in the hero only | Two motifs, repeated; bookends |
