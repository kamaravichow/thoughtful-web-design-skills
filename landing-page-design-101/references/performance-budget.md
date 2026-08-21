# Performance budget — treating speed as a design constraint

Read this when a build involves video, WebGL/Three.js, heavy animation libraries, custom fonts, or when the user asks how to keep a site fast without making it plain.

## The budget

Set it before designing, not after. Mobile, mid-tier device, 4G:

| Metric | Target | Hard ceiling |
|---|---|---|
| Largest Contentful Paint (hero) | < 1.5s | 2.0s |
| Total page weight, first view | < 1 MB | 1.5 MB |
| JavaScript, first view | < 150 KB compressed | 300 KB |
| Web font files | 2 weights | 3 |
| Interaction to Next Paint | < 200ms | 500ms |
| Cumulative Layout Shift | < 0.1 | 0.1 |

Deliberately conservative. Exceeding a ceiling is allowed only with a stated reason and a measured before/after.

## Why the numbers matter

The relationship between load time and conversion is one of the better-replicated findings in web analytics, though exact figures vary by study, vertical, and traffic mix. The consistent shape: conversion peaks at around a one-second load, drops by roughly half by two seconds, and degrades severely by four. Mobile bounce rate climbs steeply with each additional second.

**Make it concrete for the user with their own numbers** — the arithmetic is more persuasive than the citation:

```
monthly visitors × conversion rate at current speed × order value
vs.
monthly visitors × conversion rate at 1s × order value
```

For 10,000 visitors and a $50 product, the spread between a fast page and a four-second page is roughly $15,000 against $3,500. Framed that way, a decorative particle field is a line item, not a flourish.

Present these as directional. Don't invent decimal precision, and if the user needs defensible figures for a client, tell them to measure with real-user monitoring on their own traffic.

## Where the weight actually goes

Usual offenders, in rough order of damage:

1. **Autoplaying hero video, uncompressed.** Often 10–40 MB. Almost always replaceable.
2. **Three.js / WebGL scenes.** The library alone is substantial before any shader work; the parse and compile cost lands on the main thread during the worst possible moment.
3. **Animation libraries loaded for one effect.** GSAP plus plugins for a fade-in.
4. **Full font families.** Six weights and italics when two weights would do.
5. **Unoptimised images.** PNG where AVIF would do, no responsive `srcset`, no dimensions set (which also causes layout shift).
6. **Third-party scripts.** Chat widgets, four analytics tools, A/B testing snippets. Each one is someone else's performance decision imposed on yours.

## Getting visual interest cheaply

Restraint doesn't mean plain. In rough order of cost:

- **Type as the visual.** A large, well-set headline with a deliberate scale is free and reads as confident.
- **CSS gradients, mesh backgrounds, noise via SVG filters.** Kilobytes, not megabytes.
- **CSS transforms and opacity transitions.** GPU-composited, no library required.
- **`@scroll-timeline` / scroll-driven CSS animations.** Native, non-blocking, and — unlike scrolljacking — they don't hijack the scroll, they only respond to it.
- **A single hand-written SVG animation** instead of a video loop.
- **One real photograph, properly art-directed.** Usually beats any generated abstraction, and says something true about the business.

## If heavy visuals are genuinely required

Sometimes the effect is the product. Then:

- Never block first paint. Render the headline and CTA in HTML/CSS; hydrate the effect after.
- Lazy-load below the fold and on intersection.
- Serve a static poster image as the default and upgrade only on capable devices.
- Gate on `prefers-reduced-motion` and on device memory / connection hints where available.
- Cap frame rate and pause rendering when the canvas isn't visible — an idle `requestAnimationFrame` loop drains battery and reads as jank.
- Give video a hard budget: under 3 seconds, muted, looped, under 1 MB, AV1 or H.265 with a fallback, and a poster frame that already carries the message.

## Verifying

- Lighthouse mobile, throttled — not desktop, which flatters everything.
- Test on a real mid-range Android phone, not a flagship and not a simulator.
- Check on a genuinely poor connection. The site's audience includes people on trains.
- Watch first paint with the network throttled to see what the visitor sees at second one. That frame is the actual hero.
