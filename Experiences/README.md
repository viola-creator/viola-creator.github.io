# Maana Experiences

Static site for the experiences hub + six workshop pages, deployed to GitHub Pages at **[viola-creator.github.io/experiences/Experiences/](https://viola-creator.github.io/experiences/Experiences/)**. Lives at top level of the sandbox alongside `Stay/`, `Shop/`, and `Book/`.

No framework, no backend, no DB. Vanilla HTML + CSS + a small JS toggle, plus a Python build script that generates 5 of the 6 workshop pages from a single template.

---

## Structure

```
.
├── index.html                    # Experiences hub (standalone, hand-edited)
├── earthen-wall/index.html       # MASTER WORKSHOP TEMPLATE — edit this directly
├── tea-dye/index.html            # generated  ┐
├── botanical-teas/index.html     # generated  │  all built from earthen-wall
├── koji-fermentation/index.html  # generated  │  via _build_workshops.py
├── morning-tea/index.html        # generated  │
├── night-tea/index.html          # generated  ┘
│
├── _build_workshops.py           # build script — per-workshop data + substitutions
├── _partials/                    # shared partials, fetched at runtime
│   ├── header.html               # nav with logo + language toggle
│   ├── atelier.html              # "the space" block (workshops at Maana Atelier)
│   ├── tea-house.html            # "the space" block (tea ceremony workshops)
│   ├── kri.html                  # Kyoto Research Institute collab block
│   ├── closing.html              # final CTA band
│   ├── footer.html
│   ├── mobile-cta.html
│   ├── float-book.html           # floating "next session" card
│   ├── nav.js                    # scroll-darken + EN/JA toggle (localStorage)
│   ├── shared.css                # site-wide styles + brand tokens
│   └── images/                   # shared imagery (showcase-*, atelier, guest panels)
│
└── <workshop>/images/            # per-workshop imagery (hero, craft, process, etc.)
```

### Runtime partials
Each workshop page does:

```html
<div data-include="../_partials/header.html"></div>
```

…and a tiny inline script at the bottom (`fetch` + `outerHTML`) inlines the partial on load, then fires a `partials-loaded` event. **Partials must be loaded over HTTP** — opening `file://` will fail.

---

## Local preview

```bash
cd Workshop/earthen-wall-redesign
python3 -m http.server 8000
# open http://localhost:8000/
```

---

## Editing workflow

### Hub page
Edit `index.html` directly. No build step.

### Earthen Wall workshop
Edit `earthen-wall/index.html` directly. **This file is also the template** for the other 5 workshops — markup changes here propagate when the build script runs.

### Other 5 workshops (tea-dye, botanical-teas, koji-fermentation, morning-tea, night-tea)
Don't edit those `index.html` files directly — they're regenerated. Instead:

1. Edit per-workshop data in `_build_workshops.py` (each workshop is a dict with `title`, `lede`, `craft_p1`, `spend_steps`, `faq`, and `*_jp` Japanese siblings).
2. Run `python3 _build_workshops.py`.
3. The 5 `index.html` files get rewritten.

### Partials
Edit any file under `_partials/`. No rebuild needed — they're fetched at runtime.

---

## Language toggle (EN / JA)

- A button in the nav toggles between English and Japanese.
- Every translatable string is wrapped as two siblings:
  ```html
  <span class="lang-en">English</span><span class="lang-jp">日本語</span>
  ```
- CSS hides one based on `<html lang>`:
  ```css
  .lang-jp { display: none; }
  html[lang="ja"] .lang-jp { display: inline; }
  html[lang="ja"] .lang-en { display: none; }
  ```
- `_partials/nav.js` reads/writes the choice to `localStorage` under key `maana-lang`.
- In `_build_workshops.py`, the `bi(en, jp)` helper emits the dual-span markup for substituted content.

---

## Deployment

The repo is wired to GitHub Pages on the `main` branch (`Settings → Pages → Branch: main, Folder: /`).

- Push to `main` → Pages rebuilds and serves at `viola-creator.github.io/experiences/` within ~60s.
- `.nojekyll` is present so Pages serves files as-is.

### Moving to production
For a custom domain (e.g. `maanahomes.com/experiences/`):
- All internal links are relative (`../tea-dye/`, `_partials/...`) so the path can move freely as long as the folder structure stays intact.
- External links already point to `https://maanahomes.com/*` (Stay, Our Story, Book Stay).
- Either set a custom domain in GitHub Pages settings, or copy the static output into your existing deploy pipeline.

---

## Bookings

There's no booking system — all "Book Now" / "ご予約" CTAs are `<a href="https://maanahomes.com/contact" target="_blank">` links out to the main Maana site. The calendar on each workshop page is **read-only**, populated from `sessions_data` lists in `_build_workshops.py`.

---

## What ships vs. what's hidden

**Live (4 workshops)**: Earthen Wall, Tea Dye, Botanical Teas, Koji Fermentation.

**Drafted but hidden from users (re-enable when ready)**:
- **Japanese version** — all `.lang-jp` content is in place but the toggle button is hidden via one CSS rule. To re-enable, **delete the `#lang-toggle { display: none; }` rule** in two places: `_partials/shared.css` and the inline `<style>` block in `index.html`.
- **Morning Tea + Night Tea Ceremony pages** — `/morning-tea/` and `/night-tea/` exist in the repo but aren't linked. The seasonal feature card and the two ceremony cards on the hub, plus the "Other experiences" carousel on every workshop, currently link out to the existing ceremony pages on the live Maana site:
  - Morning → `https://www.maana.jp/experiences/tea-ceremony`
  - Night → `https://www.maana.jp/experiences/tea-ceremony-night`
  
  To bring the new internal pages live, find/replace those URLs back to `./morning-tea/` / `./night-tea/` (and `../morning-tea/` / `../night-tea/` for the workshop "Other experiences" links and the `EXPERIENCES_CARDS` list in `_build_workshops.py`), then re-run `python3 _build_workshops.py`.

## Known gaps / handoff notes

- **No real booking flow** — intentionally delegated to the main Maana site.
- **Calendar dates** in `sessions_data` are sample data for May–June 2026. Needs a real source (CMS, JSON feed, or periodic manual refresh).
- **Guest photos**: Tea-dye has 9 wired; Koji intentionally hides its gallery (`strip_voices_gallery: True`); other workshops have no guest photos yet.
- **Japanese copy** was AI-assisted with a native-tone pass — a final review by a native editor would tighten it before re-enabling the toggle.
- **PNG photos**: a few are 1–2 MB. Converting to JPEG would cut ~80% off page weight if performance matters.
- **Cache-buster**: `_partials/shared.css?v=N` — bump `N` whenever you ship CSS changes if you want to dodge stale browser caches.
