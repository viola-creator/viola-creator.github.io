# Maana Website Redesign Plan

> Working plan to ship a full website redesign by end of September 2026. Use this as the source-of-truth when building Asana epics, tasks, and dependencies.

---

## North star

- **Deadline**: September 30, 2026
- **Scope**: Full English site redesign covering Navigation, Stays (3 properties), Book Now, Experiences hub + Workshops (already done), Artist Story page (replacing Retreats), Dine (light touch), FAQ + Access + Contact (consolidate), About Us (content-blocked, slip to October if needed), Home page
- **Out of scope (Phase 2)**: Japanese localization. AI translate first, then human review. Target end of December 2026.

---

## Page-by-page status going in

| Page | Status | Treatment |
|---|---|---|
| Workshops × 4 | **DONE** | Already shipped to staging. No further work. |
| Tea Ceremony × 2 | Done (external partner) | Keep linking out to maana.jp/experiences/tea-ceremony |
| Experiences hub | Done | Live polish only |
| Dine | Leave as is | Light review, no rebuild |
| Retreats | **DELETE** | Replace with Artist Story page. URL strategy TBD. |
| Stays × 3 (Atelier, Kiyomizu, Kamo) | **REBUILD** | All three to a new template. |
| Book Now | **REBUILD** | Date-first flow. Hardest UX challenge of the project. |
| Navigation | **REDESIGN** | Global. Touches every page. |
| Home | **REVIEW** | Likely needs updates given other changes. |
| FAQ | Reorganize | Consolidate with Access and Contact. GEO-aware. |
| Access | Reorganize | Same as above. |
| Contact | Reorganize | Same as above. |
| About Us | Future | Content-blocked. Possible October. |
| Press | Optional | If press mentions exist, build a page. Good for GEO. |

---

## Dependency map

Pages that can't be finished without each other:

**Cluster A: Booking funnel**
- Stay template design ← blocks Stay pages (×3)
- Stay pages ← block Book Now page
- Book Now ← integrates with stay pages + workshops + tea ceremony

**Cluster B: Global**
- Nav redesign ← affects every page
- Design tokens / system updates ← affect every page
- Recommended: lock these early, implement once

**Cluster C: Information layer**
- FAQ + Access + Contact ← consider as one IA cluster
- All three share content about location, hours, policies

**Cluster D: Artist story replacement**
- Retreats URL strategy ← affects sitemap and SEO
- Artist content collection ← blocks page build
- Product display logic ← affects build approach

**Cluster E: About**
- Independent of everything else
- Content-blocked

**Cluster F: JP localization**
- Runs after all content is locked
- Otherwise translation churn

---

## Proposed phasing for Asana

### Phase 0: Foundation (June, weeks 1-2)

Goal: Lock the IA, design language updates, and global pieces so everything else can move in parallel.

**Tasks**
- [ ] IA audit: current sitemap, content inventory, page-to-page link map
- [ ] Nav redesign concept (Viola)
- [ ] Nav prototype in vanilla HTML sandbox
- [ ] Design system review: any token updates needed for new pages
- [ ] Stay page template wireframes (Viola)
- [ ] Book Now page concept refinement (the cinematic stage direction was approved, refine into spec)
- [ ] Artist story page concept (Viola + content owner)
- [ ] Retreats URL strategy decision: keep slug or 301 redirect (Viola + Sol)
- [ ] Home page audit: what changes given other changes

**Owners**: Viola leads design, Sol for tech feasibility check

**Output**: Sketches and specs ready for Sol to start implementation

---

### Phase 1: Nav + Stay template + Stay 1 (June weeks 3-4 to mid-July)

Goal: Get the new nav live and the first stay page (the canonical one) shipped.

**Tasks**
- [ ] Nav build in NextJS (Sol)
- [ ] Nav adoption across existing pages (Sol)
- [ ] Stay page template build (Sol)
- [ ] Pick canonical stay page (recommend Maana Atelier or Maana Kiyomizu, whichever has the most content ready)
- [ ] Content collection for stay 1: photos, copy, room types, amenities, location, FAQ
- [ ] Stay 1 page build (Sol)
- [ ] Reviews from Google for stay 1
- [ ] Stay 1 cross-link to relevant workshops and experiences
- [ ] QA pass on stay 1

**Owners**: Sol on code, Viola on content collection and review, photographer/content team if separate

**Output**: New nav live across all pages. One stay page in staging.

---

### Phase 2: Stay 2, Stay 3, Book Now (mid-July to mid-August)

Goal: All three stay pages live, Book Now page wired.

**Tasks**
- [ ] Content collection for stay 2 and stay 3 (Viola + team)
- [ ] Stay 2 and stay 3 builds (Sol, parallel)
- [ ] Book Now design refinement based on stay page learnings (Viola)
- [ ] Book Now page build (Sol)
- [ ] Integration: Book Now connects to all three stays + workshops + tea ceremony
- [ ] Date-first availability surface (depends on stay calendars + workshop calendars from Acuity)
- [ ] Stripe checkout flow stays the same as on workshops, just wider entry point
- [ ] QA pass on full booking funnel

**Owners**: Sol on code, Viola on content, Tomomi on copy review

**Output**: Three stay pages + Book Now in staging. Full booking funnel testable end to end.

---

### Phase 3: Artist Story + Info layer reorg + Home (mid-August to early September)

Goal: Replace Retreats, reorganize FAQ/Access/Contact, refresh Home if needed.

**Tasks**
- [ ] Artist story content collection (artists, products, narratives)
- [ ] Product display logic decision (embed Shopify? Custom? Linked out?)
- [ ] Artist story page build (Sol)
- [ ] Retreats URL handling: redirect or content swap (Sol)
- [ ] Sitemap and robots updates
- [ ] FAQ + Access + Contact IA decision: merge any? Cross-link more?
- [ ] FAQ rewrite with GEO-aware questions (see GEO_HARNESS.md)
- [ ] Access page refresh
- [ ] Contact page refresh
- [ ] Home page updates: any new featured content, removed retreats references

**Owners**: Sol on code, Viola on IA, Tomomi on copy

**Output**: Artist story live, info layer reorganized, home refreshed

---

### Phase 4: Launch prep (September weeks 2-3)

Goal: Polish, QA, performance, launch checklist.

**Tasks**
- [ ] Full site cross-browser test (Safari, Chrome, Firefox)
- [ ] Mobile test on iOS and Android
- [ ] Lighthouse pass on every page: performance, accessibility, SEO
- [ ] Broken link audit
- [ ] 404 and redirect audit (especially for old Retreats URL)
- [ ] Image optimization pass
- [ ] Schema markup validation (Google Rich Results Test)
- [ ] hreflang sanity check (even though JP isn't live yet)
- [ ] Launch checklist sign-off from Viola, Sol, Tomomi
- [ ] Press / social rollout plan if applicable
- [ ] Vercel production deploy
- [ ] Post-launch monitoring window (48 hours)

**Owners**: Whole team

**Output**: Live site at maana.jp

---

### Background track: About Us (any time, ships when ready)

Goal: Don't block on it. Add when content is in.

**Tasks**
- [ ] Founder interview / story collection (Viola + founder)
- [ ] Team bios and photos (HR / Viola)
- [ ] Values / mission articulation (Tomomi + Viola)
- [ ] Page wireframe
- [ ] Page build
- [ ] Soft launch when ready, no hard deadline

**Owner**: Viola coordinates, Tomomi writes, Sol builds when content is ready

---

### Background track: GEO content additions (any time)

Goal: Add the topical depth pages that AI search engines reward. See GEO_HARNESS.md for the full list.

**Tasks**
- [ ] "What is tsuchikabe" explainer page
- [ ] "What is shio-koji" explainer page
- [ ] "Cha-zome explained" page
- [ ] "Asa-chaji vs yo-chaji" page
- [ ] "Nishijin district guide" page
- [ ] AggregateRating + Review schema on all workshop pages
- [ ] Course schema on workshops
- [ ] Place schema with geo coords on stays and atelier
- [ ] Expanded FAQs (10-15 conversational questions per workshop)
- [ ] Press page if there are mentions to surface

**Owner**: Likely the other AI agent Viola is briefing. Tomomi for copy review.

---

### Phase 5: JP localization (October to end of December)

Goal: Japanese version of every page, native-reviewed.

**Tasks**
- [ ] AI-translate all messages/ja.json content (likely a single sprint with manual review of structured strings)
- [ ] Native speaker review pass (page by page, may need to recruit reviewer)
- [ ] Re-enable JP toggle in nav
- [ ] hreflang verification in production
- [ ] JP-specific schema review (inLanguage tags etc)
- [ ] JP launch announcement

**Owner**: Viola coordinates, native reviewer TBD, Sol re-enables toggle

---

## Roles and capacity assumptions

- **Viola**: design, PM, content collection, QA, sign-off
- **Sol**: all engineering, integrations, deploys
- **Tomomi**: copy review, voice preservation, final wording sign-off
- **Hana**: testing, ops support
- **Photographer / content creator**: needed for stay page imagery, artist page imagery (currently not in scope, flag if missing)

**Risk areas**
- Bottleneck on Sol: he's a single engineer. The schedule assumes he can ship one major area per sprint. If anything blocks him, the chain slips.
- Bottleneck on content: stay pages need photos, room copy, amenity lists. Artist page needs artist bios and product info. These are people-dependent, not code-dependent.
- Bottleneck on Tomomi: every customer-facing string needs her review. Schedule her time explicitly per phase.

---

## Suggested Asana structure

**Projects (top-level)**
1. Website Redesign 2026 (the main one)
2. GEO Content Track (parallel, ongoing)
3. JP Localization (Phase 5)

**Inside Website Redesign 2026, sections (epics)**
- Phase 0: Foundation
- Phase 1: Nav + Stay 1
- Phase 2: Stays 2/3 + Book Now
- Phase 3: Artist + Info Layer + Home
- Phase 4: Launch Prep
- Background: About Us
- Risks and blockers

**Within each section, tasks** with:
- Owner
- Due date
- Dependencies
- Definition of done

**Custom fields worth adding**
- Phase
- Owner role (Design, Eng, Copy, Content, QA)
- Blocked by
- Effort estimate (S / M / L)

---

## Building this in Asana directly

Cowork now has a live Asana connection in this session. That means we don't have to use this doc as a manual copy-paste source. I can read your Asana workspace and create the project skeleton (project, sections, tasks, due dates, dependencies) directly.

**Recommended flow**

1. Confirm which Asana workspace and team this should live under (Maana's main workspace, "Website" or "Design" team if you have one, otherwise just personal)
2. I create the three projects: Website Redesign 2026, GEO Content Track, JP Localization
3. Inside Website Redesign 2026, I add the phase sections and all the tasks listed above
4. I add due dates based on the phasing in this doc (Phase 0 mid-June, Phase 1 mid-July, etc.)
5. I tag owners where roles are known: Viola, Sol, Tomomi, Hana
6. You eyeball the result, edit anything that's off

**What I won't do without confirming first**

- Assign tasks to specific people (need their Asana user IDs and your sign-off)
- Set hard due dates (the phasing here is a sketch, you should sanity-check before they're committed)
- Add anyone to a project (notifications, etc.)

**What stays your job**

- The open questions below, those are decisions I can't make for you
- Final review of the Asana board once built
- Communicating the plan to the team

Say the word and I'll start with step 1. If you'd rather build it yourself using this doc as a guide, that's also fine, the structure is here either way.

---

## Open questions for Viola

Before locking the Asana plan, decisions needed:

1. **Photographer / content creator**: is there someone shooting the stay pages, or does that need to be commissioned? Timeline impact.
2. **Artists for the new page**: how many artists, who are they, is there a story already written or does it need to be commissioned?
3. **Products on the artist page**: where do these live? Custom build or Shopify embed or simple linked-out cards?
4. **Retreats URL**: keep `maana.jp/retreats` and change content, or redirect to a new slug like `maana.jp/artists`?
5. **Home page scope**: how much rebuild does home need? If significant, that's its own track.
6. **Booking architecture for stays**: are stays going through Cloudbeds (the existing flow) or moving into the new Stripe-on-Acuity pattern? Stay bookings work very differently from workshops, so this needs Sol's input.
7. **Budget for JP native reviewer**: needed for Phase 5.

---

## What to do today

1. Skim this with Sol so he sanity-checks the technical assumptions
2. Skim with Tomomi so she sees how much copy review work is coming
3. Answer the open questions above
4. Build the Asana project skeleton using the structure above
5. Schedule a kickoff meeting once Asana is set up, to walk the team through phases and lock owners
