# Maana Website — Project Harness

A context document for any AI agent (or new collaborator) picking up Viola's Maana website work mid-stream. Read this before touching anything.

---

## TL;DR

- **Who:** Viola — designer/PM at Maana (boutique homes + workshops in Kyoto). She "vibe codes" with AI; she's not an engineer. Sol is the CTO, runs the production NextJS app at **maana.jp**.
- **What's been built so far:** an experiences hub + 4 workshop detail pages (Earthen Wall, Tea Dye, Botanical Teas, Koji Fermentation) deployed at `viola-creator.github.io/experiences/`. Built as a static vanilla-HTML sandbox; Sol will be porting it into the real NextJS app.
- **What's next:** rebuilding more Maana site pages, especially a new **Book Now** flow (date-first, stay + workshops merged). Plus a parallel Annex project being handed off separately.
- **Workflow shift in progress:** Viola is being added to the real Maana NextJS repo as a collaborator. From now on, work happens on feature branches in the real codebase, PR-reviewed by Sol. Prototypes still get explored in a sandbox first.

---

## Why this project exists

Maana's current marketing site has a discoverability problem: **guests don't know the workshops exist until they arrive in person.** "Book Now" in the current nav leads to a tabbed page with Stays / Experiences / Retreats, where the Experiences tab is visually subtle — most users default-assume "Book Now" means "Book Stay" and never click further.

Viola wanted to:
1. Rebuild the workshop pages from scratch with a calmer, more editorial feel (the immediate goal — done for 4 workshops).
2. Eventually rebuild **Book Now** itself into a date-first flow where stays and workshops surface together — so a guest browsing dates is shown workshops happening during their stay, naturally, without ever needing to know the word "experience."

Decisions are anchored to a few brand instincts:
- **Slow, editorial, "Maana-quiet."** No OTA energy, no banners, no shouting CTAs. The Aman / Six Senses / boutique-machiya register.
- **Workshops as enrichment of a stay, not a separate product to deliberate over.** The cross-sell happens naturally inside the booking flow.
- **Bilingual (EN / JA).** Translations drafted but hidden pending native review (one CSS rule hides the toggle).

---

## Current state of the codebase

There are **two repos in play** right now:

### 1. The sandbox repo — `viola-creator/experiences`
- Plain static site (HTML/CSS/vanilla JS + a small Python build script)
- Deployed via GitHub Pages → `viola-creator.github.io/experiences/`
- Lives locally at `~/Desktop/Maana Website/Workshop/earthen-wall-redesign/`
- Contains the 4 workshop pages + the experiences hub + a Book Now mockup
- Has a thorough README inside it explaining structure

### 2. The real site repo — Maana's NextJS app (Sol's)
- NextJS (React + TypeScript)
- Deployed at maana.jp
- Viola is being added as a collaborator now; future work lands here
- We don't have direct visibility into its structure yet — Sol will share dev setup, conventions, branch strategy on first sync

The sandbox approach (1) was the right tool for early design exploration — fast iteration, no NextJS overhead, AI can edit HTML easily. Now that the design is settled for the workshops, Sol is doing the manual port into the NextJS app.

---

## Workflow from this point forward

1. **Prototypes / explorations** — stay in a sandbox (Viola's repo or a new mockup folder). Fast, no risk, throwaway-friendly.
2. **Approved designs** — port into the real NextJS repo on a **feature branch**, e.g. `viola/book-now-redesign`.
3. **Pull requests** — Sol reviews before merging to main. Never push directly to main.
4. **Local dev** — for the real repo, that means Node + `npm install` + `npm run dev` (Sol will confirm versions and steps). Static mockups can still use `python3 -m http.server`.
5. **Staging URL** — to be confirmed with Sol so changes can be previewed before going live.

---

## What's already shipped on the workshop pages

In the sandbox, the 4 workshop pages have:

- A clean editorial hero, craft section, take-home keepsake, "How you'll spend it" 4-step walkthrough, calendar/sessions placeholder, real Google reviews ("voices"), Kyoto chapter section, FAQ, "Other experiences" grid, and shared partials (atelier, KRI collab, closing, footer, mobile CTA).
- **Real Google reviews wired in** (Juan Allison, Sherry Chan, Laura George, etc.) — per-workshop, three per page. One Japanese review (Rika) is shown as-is in Japanese for diversity.
- **Tomomi copy revisions** applied throughout (refund wording, "all materials provided," koji rewrite, botanical tea regional foraging note, Mixing step rewritten, etc.) — see git history for the full list.
- **Drying-time reminder** added to Earthen Wall FAQ.
- **Per-workshop process imagery** in the spend section (each workshop has its own `process.jpg`).
- **Lightbox** on guest panels — click a panel, it opens full-screen.
- **JP toggle hidden via CSS** until copy is reviewed. The translation spans (`<span class="lang-en">` / `<span class="lang-jp">`) and Noto Serif JP loading remain in place — just one rule to delete to re-enable.
- **Tea ceremonies (Morning + Night) excluded from this update.** Their cards link out to existing `https://www.maana.jp/experiences/tea-ceremony[-night]` URLs. Their voices section is stripped entirely. Marked clearly in the README.

---

## Brand tokens / design language

Defined as CSS variables — match these in NextJS components.

```
--cream:       #f1e9d8
--cream-deep:  #e7dcc6
--paper:       #faf5ea
--ink:         #1a1714
--ink-soft:    #5a524a
--ink-mute:    #8b8074
--rule:        #ddd2bc
--terracotta:      #b3744a
--terracotta-soft: #d8a679
--serif: 'Cormorant Garamond', Georgia, serif
--sans:  'Inter', -apple-system, BlinkMacSystemFont, sans-serif
--jp:    'Noto Serif JP' (for kanji)
```

Typographic patterns:
- **Eyebrows:** 11px Inter, uppercase, terracotta, letter-spacing ~0.28em
- **Headings:** Cormorant Garamond, weight 300, italic for emotional moments, no-italic for structural
- **Body:** 16–17px Inter, line-height 1.7, ink-soft for body, ink for emphasis
- **Kanji-accent in titles:** Noto Serif JP, ~0.42em of parent size, opacity 0.55

Spacing is generous; sections use `clamp(56px, 7vw, 100px)` padding bands.

---

## Booking architecture — the big decision

This is the most important thing to understand before touching Book Now.

### Current state
Each workshop session has a "Book Now" button that opens a side panel with the session details + a CTA out to **Acuity** (Maana's existing booking provider). Acuity collects payment via Stripe or Square under the hood.

### Why the current Acuity hand-off is suboptimal
At the final step of booking, the user gets bounced from Maana-branded UI to an Acuity-hosted page to pick the date *again* and pay. Two problems:
1. **The slot the user already picked isn't carried over** (unless Acuity's `?datetime=` URL param is supported on Maana's plan tier — TBC).
2. **The brand-experience breaks** exactly when trust matters most (credit card entry).

### Two paths Sol laid out

**Path (a) — Redirect at the end (simplest)**
- User fills in details in Maana's side panel.
- Maana site → `POST /appointments` to Acuity → Acuity returns a confirmation page URL.
- User gets bounced to Acuity to actually pay.
- Pro: simplest. Con: breaks the in-panel illusion at the last step.

**Path (b) — Pay inside the panel (on-brand) ← preferred**
- Embed **Stripe Elements** inside Maana's side panel.
- User pays inside Maana UI, never leaves.
- On Stripe success → `POST /appointments` to Acuity with `paid=true`.
- Pro: fully on-brand, slot stays locked. Con: more dev work + payment/booking are now two separate operations to keep in sync.

**Viola has greenlit (b)** because launch timing isn't the priority and the on-brand experience is worth the engineering investment.

### Edge-case handling (Sol's plan)

The risk with (b) is **payment + booking getting out of sync** (e.g., Stripe charges but Acuity booking fails, or vice versa). Sol's three-layer plan:

1. **Real-time retries + escalation.** If `POST /appointments` fails after Stripe success, retry + alert. The goal: no guest can ever end up charged-but-not-booked.
2. **Slack alerts.** Route critical events ("payment succeeded but booking failed," "refund didn't complete") to a shared channel watched by both dev and the atelier/ops team.
3. **Daily reconciliation backstop.** A nightly job compares every Acuity booking against every Stripe payment and flags any mismatch. Viola flagged one concern back: for **last-minute bookings** happening within 24h, daily isn't fast enough — needs more frequent runs or near-term-booking prioritization. Sol's response is TBD.

### Cancellations & refunds

- Maana already captures all Acuity bookings in the **Maana Data app**.
- New: an admin UI inside Maana Data that lets ops cancel a booking — this bundles "free the Acuity slot" + "refund the Stripe charge" so neither gets left dangling.
- **Human-in-the-loop**, not automated. Workshop volume is low enough that a human reviewing each cancellation is safer than full auto, and it allows judgment on edge cases.
- Refund policy: **100% refund if cancelled more than 7 days before the workshop. No refund within 7 days.** The admin UI should surface the days-until-event so the policy is easy to apply at a glance.

### The bottom line for any agent working on booking-related code

- **Acuity stays the system of record** for all bookings and availability. Teachers continue to use the Acuity dashboard exactly as today; nothing changes for them.
- **Stripe is the payment processor in path (b).** Acuity records the booking, Stripe records the money — and reconciliation logic keeps them in agreement.
- **The Maana site's job** is to provide the booking UI (availability calendar + checkout) and to handle the orchestration between Stripe and Acuity.
- **Availability on the site should pull from Acuity's API in real time** so we never show a slot that's already booked. The current calendar on the workshop pages is **placeholder data** (`sessions_data` lists in `_build_workshops.py`); the real thing needs to read Acuity availability.

---

## Future state: the Book Now rebuild

The Book Now redesign is the next major project. Direction:

### The pattern
**Date-first**, not product-first. User picks dates → site shows both stays and workshops available during those dates on a single results page. Workshops appear as natural add-ons to the stay flow rather than as a separate destination the user has to discover.

### Why this pattern
- High-intent users come with dates, not product categories.
- Workshops get surfaced at the moment of peak intent (when committing to a stay), which solves the long-standing "guests don't know workshops exist" problem without ever having to "sell" the concept of experiences.
- Day-only visitors who don't need a stay also have a clean path via a toggle (*"Staying with us / Day visit only"*).

### Mockup
A static mockup of the entry page lives at `mockups/book-now/index.html` in the sandbox repo. Layout: full-bleed cinematic stage, slow Ken Burns slideshow of mixed imagery (stays, experiences, archival), centered italic headline *"When are you visiting Kyoto?"*, floating frosted-glass booker bar anchored low (toggle + 2 date fields + CTA). No grid, no sidebar — single focal point.

### What the real version needs
- **Stays availability** from Maana's PMS (whichever property management system is used — TBC with Sol)
- **Workshop availability** from Acuity API
- **Merged results page** showing both for the picked dates
- **Add-to-cart pattern** so a stay + one or more workshops can be booked together (or workshops independently for day-visit toggle)
- **Unified checkout** with Stripe Elements embedded
- Confirmation handles booking writes to both PMS and Acuity, with reconciliation as described above

This is real product engineering, not a CSS pass. Scope it with Sol as part of the same conversation as the Stripe/Acuity wiring.

---

## Other future work in flight

- **Annex project** — Viola's been working on a separate Annex (annex building) project that's being handed off to Sol around the same time. Launch is **6/1**. Annex repo handoff approach is TBD (might be a branch in the Maana repo or a separate repo, depending on Sol's preference).
- **Workshop launch** — independent of Annex, on the original schedule. The 4 ported workshop pages should go live in the NextJS app as soon as the port lands.
- **Tea Ceremony pages (Morning + Night)** — currently link out to existing maana.jp pages. May get the redesign treatment later.
- **Japanese translations** — drafted but awaiting native-tone review before unhiding the toggle.

---

## People

- **Viola** — designer/PM; primary product decision-maker for design + UX.
- **Sol** — CTO; owns the NextJS app and all backend integrations; reviews PRs.
- **Tomomi** — internal team member who reviews copy. Has already done one detailed copy pass on the workshops (output is already applied). Future copy revisions will likely come from her.

---

## Things to never assume / always ask

- **Don't assume Acuity's plan supports `?datetime=` deep-links.** Need to confirm with whoever manages the Acuity account before designing around it.
- **Don't assume the workshops have any backend yet.** Right now sessions are static placeholder data in a Python file.
- **Don't push to main on the real Maana repo.** Branch + PR, always.
- **Don't unhide the JP toggle** without explicit sign-off — translations are awaiting native review.
- **Don't restore Morning Tea / Night Tea internal pages** without checking — they were intentionally hidden and re-routed to the live maana.jp ceremony pages.
- **Don't trust copy that has em-dashes everywhere** — Tomomi flagged that as an AI tell. Trim em-dashes in body copy when generating new content.

---

## Useful conventions / patterns to keep using

### Bilingual content
Every translatable string is wrapped as two siblings:
```html
<span class="lang-en">English</span><span class="lang-jp">日本語</span>
```
CSS hides one based on `<html lang>` attribute. A small `bi(en, jp)` helper in the build script generates this markup. The toggle is currently hidden but the markup is in place everywhere.

### Imagery
- Heroes: `hero.jpeg` per workshop. ~1600px wide, JPEG q82 progressive.
- Workshop-local images in `<workshop>/images/`, shared imagery in `_partials/images/`.
- PNGs are heavier than JPEGs for photos — convert to JPEG when possible.

### Calendar / sessions
- All sample sessions live in `_build_workshops.py` per workshop, as `sessions_data` lists.
- These are placeholders. The real implementation should read Acuity availability live.

### Workshop pages — the page model
Every workshop page has the same structural sections in this order: Hero → Craft → Take-home → How you'll spend it (4 steps) → Sessions (calendar) → Voices (real Google reviews) → Kyoto chapter → FAQ → Other experiences → Atelier/Tea-house partial → KRI collab partial → Closing → Footer → Mobile CTA → Lightbox.

The earthen-wall page is the template; the other 4 are generated by `_build_workshops.py` from per-workshop data dicts.

---

## Where to look for things

| Looking for | Where |
|---|---|
| Workshop pages | `Workshop/earthen-wall-redesign/<workshop-slug>/index.html` |
| Build script + per-workshop data | `Workshop/earthen-wall-redesign/_build_workshops.py` |
| Shared partials (header, footer, atelier, kri, etc.) | `Workshop/earthen-wall-redesign/_partials/` |
| Shared CSS + brand tokens | `Workshop/earthen-wall-redesign/_partials/shared.css` |
| Book Now mockup | `Workshop/earthen-wall-redesign/mockups/book-now/index.html` |
| Detailed README (workshops) | `Workshop/earthen-wall-redesign/README.md` |

---

## How to act when picking this up

1. **Read this whole file.** It encodes context that's expensive to rediscover.
2. **Skim the README inside the sandbox repo** for hands-on details about the workshop pages.
3. **Before any structural change to booking-related code:** re-read the "Booking architecture" section above. Path (b) + reconciliation is the agreed direction; don't drift.
4. **Brand tone:** slow, editorial, considered. No banners, no "Hurry!" copy, no marketing-voice em-dashes.
5. **When in doubt about scope, ask Viola.** When in doubt about technical/backend approach, ask Sol.
