---
name: landing-page-design-101
description: A conversion-first design doctrine for websites and landing pages — clarity beats spectacle, performance is a design constraint, and every element must earn its place. Use this skill whenever the user is designing, building, reviewing, critiquing, or copywriting any website, landing page, hero section, marketing site, portfolio, SaaS site, or agency site, and whenever they mention Framer, Webflow, Next.js sites, WebGL/Three.js, GSAP, scroll animations, particle effects, "make it look premium/award-winning," or ask why a site isn't converting. Also use it proactively before writing front-end code for a public-facing page, even when the user only asks for the build and says nothing about strategy — the trap this skill guards against is exactly the one users don't know to ask about.
---

# Landing Page Web Design 101: Clarity Over Spectacle

## The problem this skill exists to prevent

AI tooling (Framer 3.0, Claude Code, Codex, v0) has decoupled visual sophistication from engineering skill. Effects that once cost a $30k agency engagement — particle shaders, liquid scroll physics, scroll-triggered video — are now a prompt away. The result is a predictable failure mode: **designs that perform for other designers rather than for the people who need to use the site.**

Call it what it is — peer-driven design, or aesthetic narcissism. The tell is simple: the work is impressive in proportion to how hard it *looks* to make, not how well it does a job. It goes viral among practitioners on X, wins a Framer gallery slot, and generates zero dollars.

A useful analogy: it's the bodybuilder phase of web design. The muscles were supposed to attract customers. Now they mostly attract other bodybuilders.

**The counter-principle to hold onto:** a website is a commercial instrument. It exists to make it obvious what problem is solved, for whom, and what to do next. Everything else is subordinate to that. Simplicity is not the absence of skill — it is the hardest thing a mature designer does.

This skill is **not** an argument for ugly websites. Craft matters enormously. But craft lives in typography, hierarchy, spacing, image selection, and above all copywriting — not in overriding the scroll wheel.

## How to apply this

Two modes. Figure out which one you're in.

**Building or designing?** Run the four pillars below as pre-flight constraints, before writing markup or animation code. State the clarity decisions explicitly (what the headline promises, what the primary action is) before showing any visual work.

**Reviewing or critiquing?** Read `references/clarity-audit.md` and produce a structured audit against the same four pillars. Don't hedge — if the hero fails the five-second test, lead with that.

Be direct about tradeoffs, but don't be a scold. Users are often excited about an effect they've seen. The job is to redirect that energy toward something that also converts, not to lecture them out of caring about beauty.

---

## The Clarity-First Framework

Four non-negotiables. Nothing ships until all four pass.

### Pillar 1 — The five-second clarity test

If a stranger lands on the hero and cannot say **what problem you solve** and **where to click** within five seconds, the page has failed. Nothing downstream can rescue it.

The bulk of the buying decision is made in the hero. That means headline and subcopy are addressing fast, intuitive, pre-rational judgment — Kahneman's System 1 in *Thinking, Fast and Slow* — not a reader carefully evaluating claims. Clarity is a neurological requirement, not a stylistic preference.

Practically:
- Kill cryptic brand taglines. "Reimagining digital flow" says nothing. "Bookkeeping for UK construction firms, done by Friday" says everything.
- Name the audience or the outcome in the headline. Ideally both.
- One primary call to action above the fold. Competing CTAs are the same as no CTA.
- **The mum test:** show the hero to someone outside the industry and ask what this business does. If they hesitate, rewrite. This is faster and more honest than any internal review.

See `references/hero-patterns.md` for headline formulas and worked before/after rewrites.

### Pillar 2 — The mobile performance budget

Most traffic is on a phone. Performance is therefore not an engineering concern handed off after design — it is a design constraint that sits alongside colour and type.

**Budget: mobile hero renders meaningfully in under 1.5s; hard ceiling 2s.**

The direction of the conversion data is not seriously disputed, even if exact figures vary by study and vertical: e-commerce conversion peaks around a ~1s load, falls by roughly half by 2s, and degrades severely by 4s. Bounce rate climbs sharply with each additional second on mobile. Run the arithmetic for the user with their own numbers — it lands harder than a statistic. On 10,000 visitors and a $50 product, the gap between a 1-second and a 4-second page is the difference between roughly $15k and roughly $3.5k. That is revenue destroyed by latency alone, for effects nobody asked for.

Treat these as directional benchmarks, not precise laws — cite them as "studies consistently show" rather than inventing decimal-point precision. If the user needs defensible numbers for a client deck, tell them to measure their own site with real-user data.

Budget specifics and cheap ways to keep visual interest are in `references/performance-budget.md`.

### Pillar 3 — Native UX integrity

Stop overriding what the browser already does well.

Scrolljacking — hijacking scroll to drive a choreographed sequence — is the headline offender. So are horizontal scroll traps, hover-to-reveal content, custom cursors that lag, and scroll-locked video that must finish before content appears. These read as innovative to practitioners and as broken to everyone else. They also wreck keyboard navigation, screen readers, reduced-motion preferences, and browser find-in-page.

The user's scroll expectation is deeply learned. Violating it doesn't feel luxurious; it feels like the page is fighting back.

Non-negotiable minimums:
- Native scroll physics. Momentum, position, and scrollbar behave normally.
- All meaningful content exists in the DOM without requiring an interaction to reveal it.
- `prefers-reduced-motion` respected, always.
- Nothing important is hover-only — touch devices have no hover.

### Pillar 4 — Outcome-driven hierarchy

Every element on the canvas answers one question:

> Does this help the user **understand** the product, or help them **act**?

If the honest answer is "it demonstrates what the tool can do," delete it. That is the single highest-leverage edit available on most modern sites.

This is also how to keep beauty in the build. Animation that survives this filter tends to be functional: a state change that confirms an action, motion that directs attention to the CTA, a product demo that shows the thing working. Animation that fails it is decoration competing with the message.

---

## People scan; they don't attend

A website is not cinema. The visitor did not buy a ticket, silence their phone, and agree to experience a sequence from beginning to end. Eye-tracking research consistently finds scanning patterns — commonly an F-shape: heavier reading across the top, a shorter horizontal pass lower down, then a vertical scan down the left edge.

The visitor is extracting an answer with minimum effort. Pricing, scope, proof, contact. Design decisions that insert artificial pauses between them and that answer are friction wearing a nice outfit.

Design consequences:
- Front-load meaning. First few words of headings and paragraphs carry the load.
- Left-align body copy. Centred paragraphs break the scan edge.
- Make pricing and service scope reachable without hunting.
- Use subheadings as a skim path — someone reading only the headings should get the whole argument.
- Proof close to the claim: real customer photos, named quotes, concrete numbers.

**The case that keeps getting cited, for good reason:** 37signals replaced a feature-heavy Highrise landing page with a stripped-back version built around a large photograph of a real customer, a direct headline, and a clear quote. Sign-ups roughly doubled — a reported ~102% lift. The elaborate version wasn't beaten by a prettier one. It was beaten by a clearer one.

---

## Where craft actually goes

When constraints strip away spectacle, the remaining budget goes into things that compound:

- **Copywriting.** Overwhelmingly the highest-leverage lever on any page. Specific beats clever, every time.
- **Typographic hierarchy.** Deliberate scale, weight, and measure. A page with three type sizes used with conviction outperforms one with nine.
- **Whitespace and rhythm.** Confidence reads as space.
- **Image selection.** Real people, real product, real work. Abstract 3D gradients say nothing.
- **Restrained, purposeful motion.** Short, interruptible, non-blocking, reduced-motion aware.

Beauty and conversion aren't opposed. They are opposed only when beauty is aimed at peers instead of customers.

---

## Failure modes to watch for in your own output

- Producing the impressive build first and mentioning strategy afterward as a caveat. Lead with clarity.
- Accepting "make it look premium" as a brief. Ask what premium means to *their customer* — often it means less, not more.
- Adding a WebGL hero because the request mentioned Three.js, without asking what the page is for.
- Reciting conversion statistics with false precision.
- Being so principled about restraint that the result is generic. Restraint plus real typographic and copy craft is the target — not a bootstrap template.

## When the rules bend

Judgment still applies. An interactive brand experience, a game, a portfolio whose product *is* the technical execution, an art piece — for these, the spectacle may be the utility. The failure isn't ambition; it's ambition misapplied to a page whose job was to sell accounting software. When a user's project genuinely falls in the first category, say so and help them do it well.
