# Discovery interview

Do this **before** mood images, palette, wireframe, or code.

Do not invent the audience's world to skip questions. If the user already
answered something in the prompt, do not re-ask it. Ask only the gaps.
If they say "just go," still complete Round 1 — skipping it is how
soulless sites happen.

Prefer the AskQuestion tool for closed questions. Ask open questions
(product job, URL, headline) in chat. Batch a round; wait; then continue.

---

## Round 1 — must answer before anything else

Ask these as a set. Block on them.

**Open (chat):**
- What is the product called, and what does it **do** in one sentence?
  Not the category ("restaurant software") — the job ("run the floor
  without radio chaos").
- If a site or mock exists: paste the URL or drop screenshots.

**Closed (AskQuestion):**

1. `audience` — Who is the primary person this page is for?
   - Independent restaurant owner / operator
   - Freelancer or agency
   - Clinician or clinic staff
   - Trades / field / workshop
   - Founder or internal ops
   - Consumer / shopper
   - Other (I'll describe)

2. `existing` — What are we looking at?
   - Live site to teardown
   - Screenshots / Figma
   - Greenfield (nothing yet)
   - Other

3. `feeling` — First three seconds should feel…
   - Moody / analog / in-service
   - Warm craft
   - Dark editorial
   - Daylight / material / honest
   - Clean software, but still *of their world*
   - Not sure — derive it from the audience

4. `scope` — What should come out of this pass?
   - Visual identity deck only
   - Identity + wireframe
   - Full landing page design
   - Implement in code
   - Review / teardown only

Stop until Round 1 is answered. Then write back a one-line audience
world guess and confirm it.

---

## Round 2 — audience world (identity fuel)

Ask after Round 1. Skip any item already known.

**Open (chat):**
- Where is this person when the product matters? Room, site, time of day.
- What objects, materials, and tools are in that room?
- Words or clichés that must **never** appear (stock handshakes, neon
  SaaS gradients, "all-in-one platform," etc.)?

**Closed (AskQuestion):**

5. `light` — Light in their world?
   - Night / low tungsten
   - Dawn or close-of-service
   - Overhead fluorescent / practical
   - Daylight through windows
   - Mixed / seasonal
   - Other

6. `photos` — Photography source? (check `PEXELS_API_KEY` first — see below)
   - Search Pexels from the world brief
   - We will provide photos
   - Mix: Pexels now, replace later
   - Other

7. `constraints` — Brand locks? (allow multiple)
   - Must keep logo
   - Must keep colors
   - Must keep type
   - No locks — build identity from mood
   - Other

8. `type_craft` — Serif / display should feel like…
   - Printed menu
   - Ledger / invoice
   - Editorial magazine
   - Poster / workshop sign
   - Invitation / hospitality
   - No serif (only if the craft is not analog)
   - Other

### Photo source + API key gate (required)

Before asking `photos`, or immediately after if they pick Pexels/mix:

1. Check for `PEXELS_API_KEY` in the environment (and `.env` / `.env.local`
   in the project). Do **not** scrape Pexels.
2. **If the key is present** — offer all `photos` options above. If they
   choose Pexels or mix, proceed with `scripts/search_pexels.py`.
3. **If the key is missing** — do not run Pexels. Ask this as its own
   step (AskQuestion + open follow-up):

   **Closed — `pexels_key`:**
   - I will paste / set a Pexels API key now
   - Skip Pexels — I will provide mood images myself
   - Other

   **If they choose to set a key:** ask them to `export PEXELS_API_KEY=...`
   or paste it for this session. Key: https://www.pexels.com/api/
   Re-check that it is available before searching.

   **If they skip Pexels (or still have no key):** set
   `Photo source: provided` and **block** until they drop files, paths,
   or URLs. Ask in chat:

   - Drop 4–8 mood photos of the audience's world (place, light,
     materials — not product screenshots), **or**
   - Paste local folder paths / image URLs

   Do not invent stock, generate fake photos, or continue to palette /
   layout without real images. Reminder: photography of their world is
   non-negotiable.

---

## Round 3 — page jobs

**Open (chat):**
- Draft or confirm the **one** promise heading (what the software does).
- Primary CTA label and destination.
- 3–4 product jobs that deserve a feature panel (not a catalog).
- Proof you actually have: logos, quotes, metrics — or none.
- 2–5 sites whose **flow** you like, and which job each should donate
  (hero / ribbon / how-it-works / features / proof / CTA). Steal jobs,
  not skins.

**Closed (AskQuestion):**

9. `motion` — Motion taste?
   - Quiet, almost still
   - Fluid bookends (hero recedes, CTA inverse)
   - Cinematic / section-ownership
   - Not sure — propose a motif pair

10. `must_not` — What should the page refuse? (allow multiple)
    - Feature-grid hero
    - No photography
    - Generic dark SaaS
    - Numbered 1-2-3 how-it-works
    - Wall of feature text
    - Centered flat CTA banner
    - Other

---

## Brief (fill this; then start work)

Copy and complete. Empty fields mean you skipped discovery.

```
Product:
Promise (one sentence):
Audience (role):
World (place, light, materials, objects):
Feeling (3–5 words):
Never:
Existing site:
Scope:
Brand locks:
Photo source: Pexels / provided / mix
PEXELS_API_KEY: present / missing → provided images
Mood images on hand: (paths, URLs, or “pending from user”)
Type craft:
CTA:
Jobs (3–4):
Proof on hand:
Frankenstein donors (site → job):
Motion taste:
```

Only after this brief exists: search mood images, extract palette,
Frankenstein flow, wireframe, translate, motion.
