# Clarity Audit — reviewing an existing site or design

Read this when the user asks you to review, critique, roast, or diagnose a website, landing page, or design mockup. Also read it when they ask "why isn't this converting?"

## Before you start

Establish three things. Ask if they aren't obvious — an audit against the wrong goal is worse than none.

1. **Who is the intended customer?** Not the demographic — the person with the problem.
2. **What is the one action the page exists to drive?** Book a call, start a trial, buy, join the list.
3. **What does the business actually charge for?** A page can look clear and still hide the offer.

If the user can't answer these quickly, that *is* the finding. The page can't be clearer than the strategy behind it.

## Scoring the four pillars

Score each pillar Pass / Weak / Fail with a specific, quotable reason. Vague notes ("hierarchy could be stronger") are useless — point at the element.

### Pillar 1 — Five-second clarity
- Read only the hero. Write down, in your own words, what this company does and who for. If you can't, that's a Fail — and say what you *did* absorb instead, because that's the real message being transmitted.
- Is the primary CTA visually dominant, or competing with a nav item, a secondary link, and a scroll cue?
- Does the headline contain a claim that could be made by a competitor verbatim? If yes, it's not a headline, it's wallpaper.

### Pillar 2 — Performance
- Estimate weight: hero video, WebGL/canvas, font count, uncompressed images, animation libraries.
- Where possible, check actual numbers rather than guessing. If the site is public and tools are available, look it up; otherwise say clearly that the assessment is structural, not measured.
- Flag anything that blocks first meaningful paint: intro loaders, full-screen video that must buffer, fonts without `font-display: swap`.

### Pillar 3 — Native UX integrity
Check for, and name explicitly if present:
- Scrolljacking / scroll-driven section snapping
- Horizontal scroll sections
- Hover-only content on a page that gets mobile traffic
- Custom cursors
- Intro animations that gate content
- Missing `prefers-reduced-motion` handling
- Content that only exists after an interaction

### Pillar 4 — Outcome-driven hierarchy
Walk the page section by section. For each, ask: understand, act, or neither? Produce the "neither" list. That list is the deliverable — it's the concrete edit.

## Report structure

Use this shape. Keep it tight; a long audit gets skimmed like a bad landing page.

```
## Verdict
[Two or three sentences. Lead with the single biggest problem. Be direct.]

## The five-second test
[What you understood from the hero alone, verbatim. Then what the page presumably wanted you to understand.]

## Scorecard
| Pillar | Score | The specific issue |
|---|---|---|
| Five-second clarity | | |
| Mobile performance | | |
| Native UX integrity | | |
| Outcome-driven hierarchy | | |

## What to fix first
[Ranked, 3–5 items, each with the concrete change — not the principle. Include a rewritten headline if the current one is weak.]

## What's genuinely working
[Real, not consolation. If the typography is good, say so. Credibility depends on this section being honest.]
```

## Tone

The person built this and probably likes it. Be straight about what's broken and specific about the fix — that's the respectful version. Avoid both flattery and contempt. Where an effect is genuinely well-executed but strategically wrong, say exactly that: the craft is real, the placement isn't.
