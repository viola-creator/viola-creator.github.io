# Maana Website — Project Harness

A context document for any AI agent (or new collaborator) picking up Viola's Maana website work mid-stream. **Read this before touching anything.**

---

## TL;DR

- **Who:** Viola — designer/PM at Maana (boutique homes + workshops in Kyoto). She "vibe codes" with AI; she's not an engineer. Sol is the CTO, runs the production NextJS app at **maana.jp**.
- **What this repo is:** Viola's sandbox of static HTML/CSS/JS mockups for the next Maana site. Sol ports approved designs into the real NextJS app on feature branches.
- **What's been built so far:** Stay listing + 3 property pages (Kyoto, Kamo, Kiyomizu with 3 inline suites), Shop landing, Book flow (booker → availability results), and the original 4 workshop pages + Morning/Night tea ceremony pages under Experiences. Image weight slashed from 496 MB → 148 MB.
- **Live URLs:** Repo is `viola-creator/viola-creator.github.io` (the special "user site" name) — pages deploy to the root of `viola-creator.github.io/`:
  - `viola-creator.github.io/Stay/`
  - `viola-creator.github.io/Shop/`
  - `viola-creator.github.io/Book/`
  - `viola-creator.github.io/Experiences/`
- **What's next:** Whatever Viola asks next. The Annex page is still pending design. Tea ceremony pages may get a refresh later.

---

## Folder structure

Top-level layout — Stay, Shop, Book, Experiences are **parallel peers**:

```
Maana Website/
├── Stay/
│   ├── index.html               # listing (4 properties; Annex on row 2 marked coming-soon)
│   ├── kyoto.html               # Maana Kyoto detail
│   ├── kamo.html                # Maana Kamo detail
│   ├── kiyomizu.html            # overview + 3 inline suite sections (#suite1 / #suite2 / #suite3)
│   └── images/
│       ├── kyoto/, kamo/, kiyomizu/{kissa-shop,kissa-food}.jpg
│       ├── kiyomizu/{suite1,suite2,suite3}/
│       └── annex/hero.jpg       # was .png; converted during compression pass
├── Shop/
│   ├── index.html               # shop landing (Masako "Her work" carousel + Our favourites carousel)
│   ├── Products/                # product photography
│   └── Masako Nakagami/         # featured maker
├── Book/
│   ├── index.html               # booker (date picker + Staying with us / Workshop only toggle + tea-ceremony pairing)
│   └── availability.html        # results page (Stays via Airhost, Workshops direct)
├── Experiences/                 # WAS Workshop/earthen-wall-redesign/ — promoted to top level
│   ├── index.html               # experiences hub (existing; bilingual EN/JA, links external to maana.jp)
│   ├── earthen-wall/            # MASTER WORKSHOP TEMPLATE
│   ├── tea-dye/, koji-fermentation/, botanical-teas/   # generated from earthen-wall
│   ├── morning-tea/, night-tea/ # tea ceremony pages (hand-edited; bilingual)
│   ├── _partials/               # shared header, footer, atelier, kri, closing, mobile-cta, shared.css, nav.js
│   ├── _build_workshops.py      # generator for 4 of the 6 workshop pages
│   ├── _previews/               # dev-only screenshots (safe to gitignore)
│   ├── mockups/                 # old book-now mockups + new "deal" mockups
│   └── README.md                # detailed README for the workshop sub-site
├── maana-web/                   # production NextJS repo (gitignored — separate repo)
├── Logo med.png                 # brand logo (has a space in filename; not breaking but worth renaming someday)
├── PROJECT_HARNESS.md           # this file
├── MAANA_REDESIGN_PROJECT_PLAN.md
└── .gitignore
```

The `Workshop/` folder is gone. Don't recreate it. Anything that was at `Workshop/earthen-wall-redesign/...` is now at `Experiences/...`.

---

## Git + deploy

### One repo, one remote

```
local:  ~/Desktop/Maana Website
git:    https://github.com/viola-creator/viola-creator.github.io.git  (renamed from viola-creator/experiences)
pages:  serves the root of main branch at https://viola-creator.github.io/
```

The repo name `viola-creator.github.io` is the magic name that tells GitHub Pages to serve at the root URL instead of nesting under `/reponame/`. Don't rename it back.

### Routine commit + push

```bash
cd "/Users/panko/Desktop/Maana Website"
git add .
git commit -m "Short description"
git push
```

Pages rebuild takes 2-5 minutes. Browser may cache aggressively — hard refresh (Cmd+Shift+R) or open incognito to verify.

### Production repo (do not touch)

The `maana-web/` folder is a clone of the real NextJS production app (`maana-japan/maana-web`). It's gitignored from the sandbox repo on purpose. Approved designs from the sandbox get manually ported into NextJS on feature branches by Sol; never push directly.

---

## Brand tokens / design language

Defined as CSS variables — match these in any new pages and in NextJS components.

```css
--cream:           #f1e9d8
--cream-deep:      #ebe1c8
--paper:           #faf5ea
--ink:             #1a1714
--ink-soft:        #5a524a
--ink-mute:        #8b8074
--rule:            #d9cfb8
--terracotta:      #b3744a
--terracotta-soft: #d8a679
--serif: 'Cormorant Garamond', Georgia, serif
--sans:  'Inter', -apple-system, BlinkMacSystemFont, sans-serif
--jp:    'Noto Serif JP'  (kanji accent; loaded via Google Fonts)
--ease-out: cubic-bezier(0.22, 0.61, 0.36, 1)
```

### Typographic patterns

- **Eyebrows:** 11px Inter, uppercase, terracotta, letter-spacing ~0.28em, weight 500
- **Section titles:** Cormorant Garamond weight 400, **NOT italic**, font-size `clamp(32px, 3.8vw, 48px)`, line-height 1.05
- **Hero titles:** Cormorant Garamond weight 400, larger `clamp(56px, 7vw, 110px)`
- **Body:** Inter, 15-17px, line-height 1.55-1.65, ink-soft for body, ink for emphasis
- **Stat lines / metadata:** Inter 11px, uppercase, letter-spacing 0.22em, ink-mute
- **Spacing:** generous; sections use `clamp(56px, 7vw, 100px)` padding bands

### Hard brand rules (Viola has enforced repeatedly)

- **NO em-dashes** anywhere in user-facing copy or in chat with Viola. Use commas, periods, colons, or "to" instead. She flagged it early: *"i don like —"*. Applies to titles, descriptions, and section copy. Comments in CSS/JS are fine.
- **No italics on structural section titles.** Italic Cormorant is reserved for emotional moments inside body copy, not for `<h2>` section headings.
- **No trailing periods on titles or eyebrows.**
- **No marketing-voice CTAs** (no "Hurry!", "Don't miss out", etc.). Stay editorial.
- **No banners, no shouting.** Aman / Six Senses / boutique-machiya register.

---

## Layout patterns used across the site

These are conventions to keep using on new pages so the site feels coherent.

### Top nav (Stay/Shop/Book/Availability)

```html
<nav class="site-nav">
  <a class="site-nav__logo" href="../"><img src="../Logo med.png" alt="Maana" /></a>
  <div class="site-nav__links">
    <a class="site-nav__link" href="../Stay/index.html">Stay</a>
    <a class="site-nav__link" href="../Experiences/index.html">Experiences</a>
    <a class="site-nav__link" href="../Shop/index.html">Shop</a>
    <a class="site-nav__cta" href="../Book/index.html">Book Now</a>
  </div>
</nav>
```

- `position: sticky; top: 0` with `background: var(--ink); color: var(--paper)`
- Logo is inverted via `filter: brightness(0) invert(1)`
- `.is-active` class on the current section's link (paper color) or CTA (paper bg, ink text)
- Mobile: smaller padding/fonts, links may compress

The Experiences hub (`Experiences/index.html`) still has the OLD bilingual nav with maanahomes.com external links. It hasn't been harmonized with the new nav. Viola knows; she may or may not ask for that next.

### Property card (Stay listing)

- Full-card clickable via invisible absolute `<a class="prop__link">` overlay (z-index 3)
- Internal CTAs (`prop__cta-row` buttons) sit at higher z-index so they remain individually clickable
- Image is portrait `aspect-ratio: 5/6` with gradient overlay at bottom
- Stat line in overlay (`89 m² · 2 Bedrooms · Sleeps 5`)
- Body has: name + stats + "Best for..." line + CTA row
- Annex card uses `prop--coming` and shows `Opening · December 2026` status pill
- Kiyomizu card has a 3-thumbnail strip below the body (deep-links to `kiyomizu.html#suite1/#suite2/#suite3`)

### Stay detail page (Kyoto / Kamo template)

Order: Hero → Sub-nav → Quicklook → Story → Design rows → Mosaic → Amenities (kitchen/bath/coffee cards + 6-icon row of essentials) → Location → Workshops cross-link → Exterior → Book CTA → Other properties → Floating book widget.

- Sticky sub-nav with scroll-spy (About · Design · Amenities · Location · Workshops · Book)
- 6 essentials in a 3-col × 2-row icon grid (WiFi, Washer & dryer, Indoor slippers, Iron, Yoga mats, Wireless speaker). SVG icons stroked terracotta. **The pills "Also included" section was removed; everything that matters is in the icons.**
- Floating book widget (`position: fixed`, bottom-right desktop, sticky bottom mobile) shown after hero scrolls out

### Kiyomizu page (different — boutique-of-3-suites)

- Triptych hero (3 suite images side by side, each deep-linking to `#suite1/#suite2/#suite3` inline sections)
- Suites overview section (3 compact cards)
- Three inline suite-detail sections (alternating L/R image+text spread; Suite 2 has cream background as middle stripe)
- Each suite-detail__media is a **carousel** (single image on Suite 1, multi-image on Suite 2 + Suite 3, see "Suite carousel" below)
- Kissa Kishin breakfast section (food + shopfront in vertical 2-cell media stack on the left, copy + hours + "included with stay" on the right)
- Standard Location → Workshops → Other Properties tail
- Floating widget says "Choose a suite →" (scrolls to `#suites`) instead of "Book your stay"

### Suite carousel (kiyomizu suite-detail__media)

```html
<div class="suite-detail__media carousel"> <!-- add carousel--single class if only 1 slide -->
  <div class="carousel__slides">
    <div class="carousel__slide is-active"><img src="..."></div>
    <div class="carousel__slide"><img src="..."></div>
  </div>
  <button class="carousel__btn carousel__btn--prev">←</button>
  <button class="carousel__btn carousel__btn--next">→</button>
  <div class="carousel__dots">
    <button class="carousel__dot is-active"></button>
    <button class="carousel__dot"></button>
  </div>
  <span class="carousel__count">1 / 2</span>
  <span class="suite-detail__tag">Suite 1</span>
</div>
```

JS hooks every `.carousel` on load. Arrows fade in on hover, dots show active state as a pill, count badge sits top-right. Keyboard arrow keys also work when carousel is focused. `carousel--single` class hides all controls for one-image cases.

---

## Booking flow

### `Book/index.html` — the booker

- Clean cream/paper background, **no slideshow** (intentionally stripped)
- Title: "When are you visiting Kyoto?" — one line, smaller than a hero (`clamp(28px, 3.6vw, 46px)`)
- Mode toggle: **"Staying with us" / "Workshop only"** (only those two — don't add a third)
- Custom-built date picker (vanilla JS, ~150 lines at the bottom of the file):
  - Click Arrive or Depart field → calendar popup
  - Past dates disabled, today has a terracotta ring
  - Picking arrive auto-advances to depart-picking
  - Picking depart before arrive resets to new arrive
  - Click outside or Escape closes the popup
  - Defaults: arrive = today + 30 days, depart = arrive + 3 nights
- URL params on load (`?arrive=&depart=&mode=`) pre-fill the picker — used by the "Change dates" link on the availability page
- "Pair your stay with a tea ceremony" section below the booker:
  - Single-sentence H2 only (no eyebrow)
  - Two cards: Night Tea Ceremony (with **Summer Only** terracotta badge) + Morning Tea Ceremony
  - Copy is lifted verbatim from `Experiences/night-tea/` and `Experiences/morning-tea/` — don't rewrite
- "Not sure yet? Browse our properties →" link at the bottom (`booker-foot`)

### `Book/availability.html` — the results page

The booker CTA navigates here with `?arrive=&depart=&mode=`.

- Trip summary banner: big date range "Jun 24 to Jun 27", nights count, mode pill, "Change dates" outline button
- Ticker count: "5 homes · 3 workshops available for these dates"
- **Two sections, ordered by mode:**
  - Stay mode → Stays first, Workshops second ("while you're here")
  - Workshop mode → Workshops first, Stays second
- Each section's eyebrow names the booking method:
  - **"Stays · Booked via Airhost"** (NOT Airbnb — Maana uses Airhost as the property management / booking system)
  - **"Workshops · Booked directly"**
- **The differentiation that matters most** — each card has its own CTA:
  - **Stay card CTA:** *Reserve on Airhost* — solid ink button, diagonal-arrow icon (↗), `target="_blank"`, URL is `https://book.airhost.co/<property>?check_in=&check_out=` (placeholders for now; Viola will swap in real listing IDs)
  - **Workshop card CTA:** *Book directly →* — solid **terracotta** button, horizontal arrow, same-tab, links to `Experiences/<workshop-slug>/index.html?date=YYYY-MM-DD`
- Each card also has secondary actions:
  - Stay card: small "See more →" link (text + bottom border) to the property page (kyoto, kamo, or kiyomizu with anchor)
  - Workshop card: just the primary CTA
- **Images are NOT clickable.** The card frame and price aren't either. Only the primary CTA and the "See more" link.
- Each stay card has a "What's included" row showing 6 amenity icons (lifted from the property page essentials) — WiFi, Washer/Dryer, Slippers, Iron, Yoga mats, Speaker
- The 6 SVG icons are defined once as `<symbol>`s at the top of `<body>` and referenced via `<use href="#i-wifi">` in each card
- Workshop schedule is hardcoded by weekday in JS at the top of the script — Mon: Tea Dye, Tue: Koji Fermentation, Wed: Botanical Teas, Thu: Earthen Wall, Fri: Tea Dye, Sat: Koji Fermentation, Sun closed. Swap to real Acuity API when wiring backend.

### Current prices (placeholders Viola set — all 80k+ per night)

| Property | From |
|---|---|
| Maana Kyoto | ¥85,000 / night |
| Maana Kamo | ¥95,000 / night |
| Kiyomizu Suite One | ¥80,000 / night |
| Kiyomizu Suite Two | ¥125,000 / night |
| Kiyomizu Suite Three | ¥110,000 / night |

---

## Booking architecture (the long-term vision)

The mockup uses **Airhost** as the external stay-booking system. The earlier doc described an Acuity + Stripe Elements plan for workshops — that direction is still alive for the real NextJS build. Summary so this isn't lost:

- **Stays:** booked through **Airhost** (Maana's property management system). Site sends the user to Airhost with dates pre-filled for now; longer term, an embedded checkout is possible if Airhost supports it.
- **Workshops:** booked **directly on the Maana site** via Acuity API. The on-brand path is to embed **Stripe Elements** in the checkout panel so users never leave Maana UI; on Stripe success, `POST /appointments` to Acuity records the booking. Acuity stays the system of record for slots and availability; Stripe records the money.
- **Reconciliation:** real-time retries + Slack alerts + a nightly job comparing every Acuity booking to every Stripe payment. Viola flagged that for last-minute bookings (<24h) the nightly cadence isn't fast enough — Sol's response TBD.
- **Cancellations:** human-in-the-loop via an admin UI in the Maana Data app. Policy: 100% refund if cancelled >7 days before; no refund within 7 days. Surface days-until-event in the admin UI.

The current `Book/availability.html` is a **mockup** of the picker + results UI. Real availability calls aren't wired yet — placeholder schedule + Airhost URL stubs.

---

## Image compression policy

A full compression pass dropped image folders from **496 MB → 148 MB**. To avoid bloating the repo again:

- **Web target:** max 2400px wide, JPEG quality 85, EXIF stripped
- **Photos as PNG should be JPEG** — the Annex hero was converted (`hero.png` → `hero.jpg`)
- **Hero / card images:** ~300 KB to 1 MB is the sweet spot
- **Don't commit DSLR-direct files** (60+ MB JPEGs). If Viola adds a new image, run it through ImageMagick or Preview's Export with reduced quality first.

To compress a new image in Terminal:
```bash
convert input.jpg -auto-orient -resize '2400x2400>' -quality 85 -strip output.jpg
```

The big originals from earlier commits are still in git history (e.g., the 63 MB `kyoto/exterior.jpeg`). Cleaning history requires `git-filter-repo` + force-push — only worth doing once the repo is shared with collaborators.

---

## People

- **Viola** — designer/PM; primary product decision-maker for design + UX. Working hands-on with AI agents like this one.
- **Sol** — CTO; owns the NextJS app and all backend integrations; reviews PRs.
- **Tomomi** — internal team member who reviews copy. Has done one detailed copy pass on the workshops. Future copy revisions likely come from her.

---

## Things to never assume / always ask

- **No em-dashes in user-facing copy.** Viola flagged it directly. Comments in code are fine.
- **Don't push to main on the production NextJS repo.** Branch + PR via Sol, always.
- **Don't unhide the JP toggle in Experiences pages** without explicit sign-off. Translations are awaiting native review.
- **Don't restore separate per-suite pages for Kiyomizu.** Viola explicitly chose the inline `#suite1/#suite2/#suite3` deep-link pattern over standalone suite pages.
- **Don't auto-rewrite the tea-ceremony card copy.** It was lifted verbatim from `Experiences/{morning,night}-tea/index.html`. If those change, the Book page should pull the new wording.
- **Don't assume Airhost URL params.** The `?check_in=&check_out=` pattern in the mockup is what most PMSs use; verify with whoever manages Maana's Airhost account before treating it as final.
- **Don't add a new "Day visit only" toggle option.** The mode toggle is exactly "Staying with us / Workshop only."
- **Don't change `Logo med.png` filename** without updating every reference. (Worth renaming someday but not right now.)
- **Past sessions noted she dislikes overengineering.** Lean to the simple HTML/CSS solution unless complexity is justified.

---

## Workflow guidance

1. **Read this whole file first.**
2. **Use `AskUserQuestion` for clarifying ambiguity** before starting multi-step work. Viola appreciates being asked rather than seeing wasted effort.
3. **Don't preview "I'll now do X" before doing it.** Just do the thing concisely.
4. **Brief, conversational replies.** Not long marketing-style postambles. Viola has explicitly preferred shorter wrap-ups.
5. **When she shows you a screenshot, look at what's actually on screen** before answering.
6. **Hard refresh / incognito** is the right first move when she says "I don't see it" on the live site — Pages caches aggressively.
7. **Use `git status` to verify before assuming what's pushed.**
8. **Compress images before committing them** if they're big.

---

## Where to look for things

| Looking for | Where |
|---|---|
| Stay listing | `Stay/index.html` |
| Stay detail templates | `Stay/kyoto.html` (canonical), `Stay/kamo.html` (variant) |
| Kiyomizu (different layout — 3 inline suites + breakfast) | `Stay/kiyomizu.html` |
| Booker (date picker + tea pairing) | `Book/index.html` |
| Availability results page | `Book/availability.html` |
| Shop landing | `Shop/index.html` |
| Experiences hub | `Experiences/index.html` (still uses old bilingual nav) |
| Workshop pages | `Experiences/<workshop-slug>/index.html` |
| Workshop build script | `Experiences/_build_workshops.py` |
| Shared partials (Experiences) | `Experiences/_partials/` |
| Tea ceremony pages | `Experiences/morning-tea/index.html`, `Experiences/night-tea/index.html` |
| Brand logo | `Logo med.png` (top level — note the space in filename) |
| This document | `PROJECT_HARNESS.md` |
| Other planning docs | `MAANA_REDESIGN_PROJECT_PLAN.md` |
| Old workshop README | `Experiences/README.md` |

---

## Recent session log (for handoff context)

The last working session covered, in rough order:
1. Built out Stay listing with 4-property grid (Annex on row 2 as coming-soon).
2. Built Kyoto property page (sticky sub-nav, 6 essentials icon row, floating book widget, summer "Stay 3, Pay 2" banner, cross-link to workshops).
3. Built Kamo using the Kyoto template (signature: "Designed around the bathtub").
4. Built Kiyomizu with the differentiated 3-suite layout (hero triptych, inline suite detail sections, Kissa Kishin breakfast block).
5. Added per-suite carousels.
6. Built the Book flow: booker (`Book/index.html`) → availability results (`Book/availability.html`).
7. Migrated all cross-references from old `Workshop/earthen-wall-redesign/` path to `Experiences/`.
8. Renamed the GitHub repo from `experiences` to `viola-creator.github.io` so Pages serves at the root URL.
9. Compressed every oversized image; 496 MB → 148 MB.
10. Added the "Pair your stay with a tea ceremony" section to `Book/index.html` with verbatim copy from the experience pages + Summer Only badge on Night Tea card.
