# Maana Website Redesign — Project Plan

> Integrated, phase-based execution plan. Pairs the dependency-driven timeline from `REDESIGN_PLAN.md` with Viola's actual working loop: **Design → Clickable mockup → Stakeholder review → Handoff to Sol → Deploy → Joint test.**
> Source-of-truth context: `PROJECT_HARNESS.md`, `GEO_HARNESS.md`, `REDESIGN_PLAN.md`, sandbox `README.md`.
> Companion file: `MAANA_REDESIGN_ROADMAP.html` (visual one-pager for the team).

**Deadline:** September 30, 2026 (English site). JP localization runs Oct–Dec as Phase 5.

---

## 1. How the work actually moves (the unit workflow)

Every page passes through the same six gates. The plan below is just this loop, repeated and sequenced by dependency. "Done" for any page means it has cleared all six.

| # | Gate | Owner | What happens | Exit signal |
|---|---|---|---|---|
| **G1** | Design concept | Viola | Wireframe / spec for the page. Reuses brand tokens + the workshop page model. | Concept sketched, scope agreed |
| **G2** | Clickable mockup | Viola (AI-assisted) | Built in the vanilla sandbox (`Workshop/earthen-wall-redesign/`), HTML/CSS, navigable like the real thing | Mockup runs locally over HTTP, links work |
| **G3** | Stakeholder review | Founders + area owner + Tomomi | Review with **Hana & Irene** (founders) plus the people who own that area; **Tomomi** does the copy pass | Sign-off, or a revision list |
| **G4** | Handoff to Sol | Viola → Sol | Approved mockup + spec handed off. Sol ports into `maana-web` on a feature branch off `staging` | PR opened |
| **G5** | Deploy to staging | Sol | PR review, merge to `staging`, preview at **preview.maana.jp** | Page live on preview |
| **G6** | Joint test → prod | Viola + Sol | Test on preview against the QA checklist, then production deploy to **maana.jp**, then verify | Live + verified on prod |

**Who reviews what at G3** (the review is scoped to the page):

| Page type | Founders | Area reviewers | Copy |
|---|---|---|---|
| Global (Nav, design tokens) | Hana, Irene | Sol (feasibility) | Tomomi |
| Home | Hana, Irene | Home / stays team | Tomomi |
| Stay pages | Hana, Irene | Stays/home team, photographer | Tomomi |
| Workshop pages | Hana, Irene | Workshop teachers | Tomomi |
| Book Now | Hana, Irene | Sol (architecture), ops | Tomomi |
| Artist Story | Hana, Irene | The artist(s), ops | Tomomi |
| FAQ / Access / Contact | Hana, Irene | Ops / atelier | Tomomi |

**Definition of Done (per page):** approved mockup (G3) → ported component merged (G5) → passes QA checklist on preview → required schema in place (see GEO track) → live on prod (G6) → post-deploy verification logged.

---

## 2. Roles & stakeholders

| Person | Role on this project |
|---|---|
| **Viola** | Design, PM, mockups, content collection, QA, sign-off. Owns G1–G3 and drives the page through to done. |
| **Sol** (CTO, `zenzen-sol`) | All engineering: ports mockups into Next.js, integrations, deploys. Owns G4–G6 on the code side. Branch off `staging`, PR back, never push to main. |
| **Hana & Irene** | Founders / final approvers at the G3 review gate and at launch sign-off. |
| **Tomomi** | Copy review and brand voice. No customer-facing copy ships without her pass. Schedule her time *per phase* — she is a recurring gate, not a one-off. |
| **Workshop teachers** | Area reviewers for workshop pages; sources for teacher bios (GEO track). |
| **Photographer / content creator** | Imagery for stay pages and the artist page. **Not yet confirmed — see Open Decision #1.** Potential critical-path blocker. |

---

## 3. Dependency map (what gates what)

```
Design tokens ┐
Nav redesign  ┴─────────────► every page (lock these FIRST, build once)

Stay template ──► Stay 1 ──► Stay 2 ─┐
                          └─ Stay 3 ─┴──► Book Now ──► Booking funnel (Stripe + Acuity + PMS)
                                                         ▲
Workshop availability (Acuity) ──────────────────────────┘
Stays availability (PMS — TBC) ──────────────────────────┘

Retreats URL decision ─► Artist content ─► Product-display decision ─► Artist Story page ─► sitemap/robots/301s

FAQ + Access + Contact  ── treat as ONE information-architecture cluster (shared location/hours/policy content)

About Us  ── independent, content-blocked, background track
GEO content ── parallel background track (schema + explainer pages + press)
JP localization ── runs only AFTER all EN content is locked (else translation churn)
```

**Critical path:** Nav/tokens → Stay template → Stay 1 → Stays 2/3 → **Book Now** → Launch. Book Now is the longest pole and the highest-risk item; everything else can flex around it.

---

## 4. The phases

Dates follow `REDESIGN_PLAN.md`. Treat them as a sketch to sanity-check with Sol before committing, not a contract.

### Phase 0 — Foundation · *June, weeks 1–2*

**Goal:** Lock the global layer (IA, nav, design tokens) and resolve the open decisions so everything downstream can run in parallel. Nothing expensive should start until the Phase 0 decisions are made.

**Work items**

- IA audit — current sitemap, content inventory, page-to-page link map (Viola)
- Nav redesign concept → mockup (G1–G2, Viola)
- Design-system review — any token updates the new pages need (Viola + Sol feasibility)
- Stay-page template wireframes (G1, Viola)
- Book Now spec — turn the approved cinematic mockup (`mockups/book-now/`) into an engineering-ready spec (Viola + Sol)
- Artist Story page concept (Viola + content owner)
- Home audit — what changes given everything else
- **Resolve all eight Open Decisions in §6** — especially photographer (#1) and stay booking architecture (#6), which block Phases 1–2

**Review gate (G3):** Founders sign off on overall direction + the nav concept. Sol confirms technical feasibility of tokens + nav.

**Exit / output:** Approved nav concept, stay template wireframes, Book Now spec, and answered open decisions. Sol can begin implementation.

---

### Phase 1 — Nav + Stay template + Stay 1 · *June wk3 → mid-July*

**Goal:** New nav live across the site; the first (canonical) stay page shipped end-to-end. This phase also *proves the whole workflow* — first full trip through G1–G6.

**Work items**

- Nav: handoff → Sol builds in Next.js → adopt across existing pages (G4–G6)
- Stay template: build in Next.js so Stays 2/3 are fast to follow (Sol)
- Pick the canonical stay — recommend **Atelier or Kiyomizu**, whichever has the most content ready
- Content collection for Stay 1: photos, copy, room types, amenities, location, FAQ (Viola + photographer)
- Stay 1: mockup (G2) → review with founders + stays team (G3) → handoff → preview → joint test (G6)
- Pull Google reviews for Stay 1; cross-link to relevant workshops + experiences
- QA pass on Stay 1

**Review gate:** Founders + stays/home team approve Stay 1 mockup; Tomomi copy pass.

**Entry criteria:** Phase 0 decisions resolved; design tokens locked.

**Exit / output:** New nav live on all pages. One stay page on preview/prod. Template proven and reusable.

---

### Phase 2 — Stays 2/3 + Book Now · *mid-July → mid-August*

**Goal:** All three stay pages live; Book Now wired into the date-first booking funnel. **This is the hardest, highest-risk phase.**

**Work items**

- Content collection for Stays 2 & 3 (Viola + team)
- Stays 2 & 3 builds — parallel, off the locked template (Sol)
- Book Now design refinement based on what Stay pages taught us (Viola)
- Book Now build (Sol) — *real product engineering, not a CSS pass:*
  - Merged results page: stays (from PMS) + workshops (from Acuity API) for the picked dates
  - Date-first entry with "Staying with us / Day visit only" toggle
  - **Stripe Elements in-panel checkout** (Path b — greenlit; on-brand, slot stays locked)
  - Confirmation writes to both PMS and Acuity, with the reconciliation/alerting plan from `PROJECT_HARNESS.md`
- QA pass on the full booking funnel, end to end

**Review gate:** Founders + Sol (architecture) sign off on Book Now; Tomomi copy pass. Extra scrutiny on payment/booking sync edge cases.

**Entry criteria:** Stay template live (Phase 1); booking architecture decision made (#6); Acuity `?datetime=` support confirmed (#8).

**Exit / output:** Three stay pages + Book Now on preview. Full booking funnel testable end to end.

> **Risk flag:** Book Now depends on Sol being a single engineer and on the PMS/Acuity/Stripe reconciliation being solid. If anything slips, it slips here. Build in schedule slack and keep Book Now isolated so the rest of the site can launch even if booking lags.

---

### Phase 3 — Artist Story + Info layer + Home · *mid-August → early September*

**Goal:** Replace Retreats with the Artist Story page; consolidate FAQ/Access/Contact; refresh Home.

**Work items**

- Artist Story: content collection (artists, products, narratives) → product-display decision (#3) → mockup → review with the artists + founders → build
- Retreats handling: 301 redirect or content swap (#4) → sitemap + robots updates (Sol)
- FAQ + Access + Contact: treat as one IA cluster; decide merges/cross-links; rewrite FAQ GEO-aware (see `GEO_HARNESS.md`); refresh Access + Contact
- Home: apply updates surfaced by the Phase 0 audit (remove Retreats references, new featured content)

**Review gate:** Founders + relevant area owners per page; Tomomi copy pass on all new/edited copy.

**Exit / output:** Artist Story live, info layer reorganized, Home refreshed. Old Retreats URL handled cleanly.

---

### Phase 4 — Launch prep · *September weeks 2–3*

**Goal:** Polish, QA, performance, and a clean launch.

**Checklist**

- Cross-browser test (Safari, Chrome, Firefox)
- Mobile test (iOS, Android)
- Lighthouse pass on every page — performance, accessibility, SEO
- Broken-link audit
- 404 + redirect audit (especially the old Retreats URL)
- Image optimization pass (convert heavy PNGs to JPEG)
- Schema markup validation (Google Rich Results Test)
- hreflang sanity check (even though JP isn't live yet)
- **Launch sign-off** from Viola, Sol, Tomomi + founders
- Press / social rollout plan if applicable
- Vercel production deploy
- Post-launch monitoring window (48 hours)

**Exit / output:** Live English site at maana.jp, monitored.

---

### Background track A — About Us · *any time, ships when ready*

Content-blocked, no hard deadline (possible October). Don't let it gate launch.
Founder interview/story (Viola + founder) → team bios + photos → values/mission (Tomomi + Viola) → wireframe → build (Sol) → soft launch.

### Background track B — GEO content · *parallel, ongoing*

Owned largely by the other AI agent Viola is briefing; Tomomi reviews copy; Sol merges schema PRs. Ordered by impact-per-effort (`GEO_HARNESS.md`):
1. AggregateRating + Review schema on every workshop page (real Google reviews)
2. Course schema per workshop (`helpers/jsonld.ts`)
3. FAQ expansion — 10–15 conversational questions per workshop, in Tomomi's voice
4. Teacher bio blocks (needs Viola to gather photos/bios)
5. Topical explainer pages — start with "What is tsuchikabe" and "What is shio-koji"
6. Press page, if there are mentions to surface
7. Place schema with geo coords on Atelier + each stay
8. Mirror upcoming Acuity sessions as Event JSON-LD in page HTML

### Phase 5 — JP localization · *October → end December*

Runs only after EN content is locked. AI-translate `messages/ja.json` → native-speaker review (page by page) → re-enable the JP toggle (delete the one CSS rule in `_partials/shared.css` + `index.html`) → hreflang verification in prod → JP schema review (`inLanguage`) → JP launch announcement. Needs budget for a native reviewer (#7).

---

## 5. Risks & bottlenecks

| Risk | Why it matters | Mitigation |
|---|---|---|
| **Sol is a single engineer** | Schedule assumes ~one major area per sprint; any block cascades down the critical path | Keep Book Now isolated; sequence so the rest can launch without it; give Phase 2 slack |
| **Content bottleneck** | Stay pages need photos/room copy/amenities; Artist page needs bios + product info — people-dependent, not code-dependent | Resolve photographer (#1) and artist content (#2) in Phase 0; start content collection before builds |
| **Tomomi as a recurring gate** | Every customer-facing string needs her review | Book her time explicitly each phase, not at the end |
| **Book Now payment/booking sync** | Stripe charges but Acuity/PMS booking fails (or vice versa) | Path (b) + real-time retries + Slack alerts + reconciliation; flag last-minute (<24h) bookings need faster-than-daily checks |
| **Stays book differently than workshops** | Stays may use a PMS, not Acuity — different flow | Decide architecture with Sol in Phase 0 (#6) before designing Book Now |

---

## 6. Open decisions (resolve in Phase 0 — these gate the build)

1. **Photographer / content creator** — is someone shooting the stay + artist imagery, or does it need commissioning? Timeline impact on Phases 1–3.
2. **Artists for the new page** — how many, who, is the story written or does it need commissioning?
3. **Products on the artist page** — custom build, Shopify embed, or simple linked-out cards?
4. **Retreats URL** — keep `maana.jp/retreats` and swap content, or 301 to a new slug like `/artists`? Affects sitemap + SEO.
5. **Home scope** — light refresh or significant rebuild? If significant, it becomes its own track.
6. **Stay booking architecture** — stays through the existing PMS (Cloudbeds?) or the new Stripe-on-Acuity pattern? Needs Sol; blocks Book Now.
7. **JP native reviewer budget** — needed for Phase 5.
8. **Acuity `?datetime=` deep-link support** — confirm with whoever manages the Acuity account before designing around carried-over slots.

---

## 7. Guardrails (don't break these)

- Prototype in the **sandbox** first; approved designs port to **`maana-web`** on a feature branch off `staging`. **Never push to main/staging directly** — branch + PR, Sol reviews.
- **Brand tone:** slow, editorial, "Maana-quiet." No OTA energy, no fake urgency, no marketing-voice em-dashes (Tomomi's AI tell). The test: *would Tomomi cringe?*
- **Don't unhide the JP toggle** without explicit sign-off.
- **Don't restore Morning/Night Tea internal pages** — they intentionally route out to live maana.jp ceremony URLs.
- Keep brand tokens consistent between sandbox CSS and Next.js components (cream/paper/ink/terracotta, Cormorant Garamond + Inter + Noto Serif JP).
