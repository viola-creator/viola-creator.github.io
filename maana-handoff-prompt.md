# Maana Homes Navigation Redesign — Handoff Prompt

Paste this into a new chat session. The working file is in the shared folder.

---

## Who I Am

I'm Viola (viola@kaolingallery.com), UX lead for Maana Homes, a premium hospitality brand in Kyoto. I'm redesigning the site navigation. The current production site (maanahomes.com) over-relies on a hamburger-only menu. We're building an interactive prototype to pitch a better IA to the team.

---

## The Prototype

**File:** `maana-nav-prototype.html` (~3,500 lines, single self-contained HTML/CSS/JS file)
**Also:** `index.html` — a copy prepared for Netlify Drop deployment (NOTE: this copy is STALE from v2.4 and needs to be re-copied from `maana-nav-prototype.html` before deploying)

It's a fully interactive SPA prototype — no frameworks, no build tools. Click navigation, view transitions, booking modal with date picker, carousel hero, accordion drawer, the works.

### Tech Stack
- Single HTML file, all CSS and JS inline
- CSS custom properties for theming
- Google Fonts: Cormorant Garamond (serif headings), Inter (sans body)
- SPA navigation via show/hide `<div class="view">` elements
- No external dependencies

### Brand & Visual Direction
- Dark, calm, minimal — inspired by the current maanahomes.com
- Color palette: warm charcoal (#1a1816), cream (#f7f3ee), muted gold (#c4a96a), sage, indigo
- Wide letter-spacing on the MAANA logo
- Editorial tone, not commercial

---

## Current Version: v2.5

### Information Architecture

**Desktop top nav (left to right):**
Overview (→ homepage) · Stay · Experiences · Retreats · Journal
**Center:** MAANA logo (also links to homepage)
**Right:** Language toggle (EN/JP) · Book Now button (always visible)

**Mobile:**
Hamburger icon (left) → full-screen drawer with accordion menus
MAANA logo (center) · Book Now (right, compact)
Floating Book Now bar appears on scroll (high contrast, backdrop blur)
No bottom navigation.

### Views in the Prototype (12 total)

| View ID | What It Is |
|---------|-----------|
| `view-home` | Homepage with 3-slide auto-advancing carousel (2s per slide) |
| `view-stay` | Stay hub — entry point for all accommodations |
| `view-homes` | Homes index — 3 machiya cards with spec pills for at-a-glance comparison |
| `view-prop-kyoto` | Maana Kyoto detail page |
| `view-prop-kamo` | Maana Kamo detail page |
| `view-prop-kiyomizu` | Maana Kiyomizu detail page (with 3-unit picker) |
| `view-flagship` | Maana Annex — new-build flagship house (placeholder, "Opening Soon") |
| `view-hotel` | Future 10-room hotel (placeholder) |
| `view-experiences` | Experiences index — seasonal featured card + year-round grid |
| `view-tea` | Tea ceremony detail page with Morning/Night tabs |
| `view-retreats` | Retreats index — 3 multi-day retreat cards |
| `view-journal` | Journal placeholder ("Coming Soon") |

### Properties (names are SEO-locked, cannot change)

1. **Maana Kyoto** — 4 guests, 2 bed, textile district, hinoki bath, garden. Whole-house.
2. **Maana Kamo** — 6 guests, 3 bed, Kamo River view, tatami, courtyard. Whole-house.
3. **Maana Kiyomizu** — 3 connected machiya near Kiyomizu-dera. Book individually or together.
   - Unit 1: 2 guests, 1 bed, 55 m², camellia courtyard, cedar tub
   - Unit 2: 4 guests, 2 bed, 85 m², maple garden, loft room (largest)
   - Unit 3: 4 guests, 2 bed, 80 m², bamboo garden, step-free accessible
4. **Maana Annex** — new flagship, purpose-built, adjacent to Kyoto. Placeholder only.

**Property detail pages feature:**
- Sticky property-switcher tabs (Kyoto | Kamo | Kiyomizu) for instant comparison without back-navigating
- Hero banner → horizontal spec bar → editorial body → amenities grid → Book CTA
- Kiyomizu has a visual unit picker: all 3 units visible simultaneously with key specs, clicking one reveals its detail panel inline

### Experiences (under "Experiences" nav)

**Seasonal section (top of page, featured hero card):**
- 夜咄茶事 Night Tea Ceremony — summer only, gold "Summer Only" badge, full-width dark card

**Year-round section (3-column grid, 6 cards):**
1. Night Tea Ceremony *(also appears here with subtle "Summer" italic tag — pairs with Morning below)*
2. Morning Tea Ceremony and Breakfast Workshop (朝茶事)
3. Tea Dye Workshop (茶染)
4. Earthen Wall Workshop (土壁)
5. Kyoto Botanical Teas Workshop (日本茶 x 草木茶)
6. Koji Fermentation Workshop (発酵 x 保存)

**Kanji treatment:** Kanji appears in the small category label line (e.g., "Tea · 朝茶事"), NOT in the main title. Titles are English-only. On the featured card, kanji appears as a small subtitle below the English title. This keeps it elegant, not overbearing. The carousel hero has NO kanji — English only.

### Retreats (under "Retreats" nav)
- Home Design Retreat
- Culinary Retreat
- Pottery Retreat

These are multi-day immersive programs. Night Tea Ceremony is NOT a retreat — it's an experience.

### Tea Ceremony Detail Page
- Two tabs: "Morning Ceremony · 朝茶事" and "Night Ceremony · 夜咄茶事"
- Each tab shows: description, duration, time, guests, availability/season, Book CTA
- Back-link returns to Experiences (tea is mapped to `experiences` activeNav)

### Carousel (Homepage Hero)
- 3 slides, 2 seconds each, auto-advancing with progress indicators
- Slide 1: warm charcoal (#2a2420) — "Explore Stays" CTA
- Slide 2: deep indigo (#1a1e2a) — "Experience · Summer Only" / Night Tea Ceremony
- Slide 3: sage green (#1e221c) — "Hands-on Workshops" / Experiences
- Pauses on hover

### Mobile Drawer Accordion Structure
```
Stay ▾
  View All
  Maana Kyoto
  Maana Kamo
  Maana Kiyomizu
  Maana Annex
  Hotel
Experiences ▾
  夜咄茶事 Night Tea Ceremony
  朝茶事 Morning Tea Ceremony
  茶染 Tea Dye Workshop
  土壁 Earthen Wall Workshop
  日本茶 x 草木茶 Botanical Teas
  発酵 x 保存 Koji Fermentation
Retreats ▾
  Home Design Retreat
  Culinary Retreat
  Pottery Retreat
Journal
```
No "Home" button. No "Overview" in drawer. Drawer has a Book Now button and secondary links (FAQs, Access, Contact).

### Book Now Behavior
- **Desktop:** Always visible in header upper-right. Styled with border, inverts on solid header. Opens booking modal.
- **Mobile:** Compact version in header upper-right + floating full-width bar on scroll (backdrop blur, semi-transparent bg for contrast against dark sections).
- **Booking modal:** Date picker with check-in/check-out range selection, availability badges on property cards after dates selected.

---

## Key Design Decisions Made

1. **Experiences ≠ Retreats.** Experiences are workshops/ceremonies (half-day). Retreats are multi-day immersive programs. Night Tea is an Experience, not a Retreat.
2. **No "Home" in nav.** Confusing with "Homes" (machiya). Homepage reached via logo click or "Overview" on desktop.
3. **Property comparison:** Individual pages + sticky switcher tabs, not side-by-side grid. Preserves visual quietness while making back-and-forth effortless.
4. **Kiyomizu units:** All 3 always visible in a picker (no accordion/expand), so users don't need memory. Clicking a unit reveals its detail inline.
5. **Kanji as accent, not headline.** Appears in small label lines and subtitles. English titles are the primary read. Carousel has no kanji at all.
6. **Desktop floating Book Now removed.** Header CTA is persistent and sufficient. Mobile keeps the floating bar for scroll-state visibility.
7. **Units named simply:** Unit 1, Unit 2, Unit 3 (not evocative names).

---

## Notion Version Log

**Page ID:** `2ff57f0a-5cda-81b7-8b2f-f627652c6dc7`
**Parent page (Maana Website Audit):** `2f557f0a-5cda-8175-8e3d-cdee815297de`

Changelog entries exist for v2.0 through v2.4. Each entry documents changes, decisions, and rationale.

---

## What's Next / Open Items

- `index.html` needs to be re-synced from `maana-nav-prototype.html` before deploying to Netlify Drop
- Netlify Drop deployment for shareable team link (drag `index.html` onto app.netlify.com/drop)
- Hotel view is a placeholder — room types and booking flow TBD
- Journal view is a placeholder
- Maana Annex content is placeholder
- No real images yet — all visuals are CSS gradients as stand-ins
- May need to test on actual devices for mobile drawer/scroll behavior
- The team hasn't reviewed yet — feedback round incoming once the link is shared

---

## Working with this File

The prototype is a single HTML file. To continue iterating:
- Edit `maana-nav-prototype.html` directly
- CSS is in a `<style>` block at the top (~1600 lines)
- HTML views are in the middle (~1700 lines)
- JS is in a `<script>` block at the bottom (~800 lines)
- Views are `<div class="view" id="view-xxx">` — navigation shows/hides them
- `navigateTo(viewId, hash)` is the core SPA router function
- activeNav mapping: `homes/flagship/hotel/prop-*` → `stay`, `tea` → `experiences`
- All Book buttons are wired through a single `bookBtns` array → `openModal()`
- After edits, copy to `index.html` for deployment: `cp maana-nav-prototype.html index.html`
