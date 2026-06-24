# GEO Harness for Maana

> A briefing for any AI agent working on Generative Engine Optimization for the Maana website. Read top to bottom before recommending changes.

---

## What this work is

Maana wants to be the answer when a traveler asks an AI assistant (ChatGPT, Claude, Perplexity, Google AI Overviews, etc.) something like:

- "Where can I do a hands-on craft workshop in Kyoto?"
- "Best boutique stay in Kyoto for cultural travelers"
- "What is shio-koji and where can I learn to make it?"
- "Traditional earthen wall workshop Japan"
- "Tea dyeing workshop Kyoto"

The goal is not just rankings on Google. It is being the cited source inside AI-generated answers. The optimization target is large language models reading our pages and treating them as canonical.

That target rewards a different set of habits than classic SEO:
- Concrete, factual writing with names, dates, prices, durations
- Structured data so the model can extract specifics confidently
- Clear authorship and authority signals
- Conversational Q&A patterns
- Avoiding fluff, generic travel filler, and marketing puffery

---

## About Maana

Maana is a small Kyoto-based brand that operates boutique stays and a maker's atelier, plus hosts traditional Japanese workshops and tea experiences. The same team runs both the hospitality side and the experience side, and that integration is part of the pitch: guests can stay in a restored machiya, then walk to the atelier for a workshop.

**Locations**
- Maana Atelier, Nishijin (the workshop space, in the old weavers' district)
- Maana Kiyomizu (stay)
- Maana Kamo (stay)
- Other stays under the Maana Homes umbrella

**Workshops at the atelier**
- Earthen Wall (tsuchikabe, 土壁) — making a small earthen wall panel
- Tea Dye (cha-zome, 茶染) — natural dyeing with Uji tea, two kinchaku bags
- Botanical Teas (Kyoto Botanical Teas) — blending personal teas
- Koji Fermentation — making shio-koji + shoyu-koji condiments

**Excursions (off-site, with partners)**
- Morning Tea Ceremony with Eriko Okubo (asa-chaji, includes Zen breakfast)
- Night Tea Ceremony (yo-chaji, 夜茶事, seasonal, limited seats)

**Audience**
- Travelers who want depth, not Disney
- Skews toward design-literate, food-aware, slow-travel preferences
- Likely to research extensively before booking, ask AI assistants for recommendations
- International (English) and Japanese guests, with the JP locale not yet fully translated

**Brand voice**
- Editorial, restrained, slightly literary
- Avoid marketing puffery, avoid generic "experience the magic of Kyoto" phrasing
- Specific over abstract: name the teacher, the technique, the materials
- Honor the craft language (Japanese terms with kanji and pronunciation)
- Tomomi has been doing copy revisions, her preferences should be respected

---

## The site and stack

**Production app**
- Location on Viola's machine: `~/Desktop/Maana Website/maana-web`
- Repo: `github.com/maana-japan/maana-web`
- Stack: Next.js 16 App Router, TypeScript, Tailwind, biome lint, pnpm
- Deploy: Vercel
- URLs: maana.jp (prod), preview.maana.jp (staging)
- Owner: Sol (CTO, GitHub `zenzen-sol`)
- Workflow: branch off `staging`, PR back to `staging`, Sol reviews and merges

**Vanilla HTML sandbox**
- Location: `~/Desktop/Maana Website/Workshop/earthen-wall-redesign`
- Viola's design sandbox where new patterns get prototyped before Sol ports them into NextJS
- Not a deploy target, just iteration space

**Key files in production for GEO work**
- `helpers/metadata.ts` — central SITE_URL and per-page metadata
- `helpers/jsonld.ts` — existing JSON-LD schemas (Organization, LodgingBusiness, Restaurant, FAQPage, BreadcrumbList)
- `components/2024/seo/JsonLd.tsx` — the component that injects script tags
- `app/[locale]/layout.tsx` — root metadata and locale handling
- `app/[locale]/sitemap.ts` — sitemap with hreflang alternates
- `app/[locale]/robots.ts` — robots config
- `messages/en.json` and `messages/ja.json` — all copy lives here, including meta descriptions per page
- `app/[locale]/experiences/*/page.tsx` — workshop and ceremony pages
- `app/[locale]/experiences/page.tsx` — experiences hub

---

## What's already in place

**Technical SEO basics**
- Sitemap.xml emitted with hreflang for EN and JA
- Robots.ts allows everything except /admin/
- Per-page `<title>` and `<meta description>` via next-intl messages
- Canonical URLs anchored at https://www.maana.jp
- Mobile-responsive, fast loading, modern stack

**Structured data (JSON-LD) already wired**
- `organizationSchema()` — Maana as an Organization
- `lodgingBusinessSchema()` — applied to stay pages
- `restaurantSchema()` — Kissa Kishin (the dining offering)
- `faqPageSchema()` — applied to workshop and experience FAQ blocks
- `breadcrumbListSchema()` — applied across pages

**Content patterns that are already helping**
- Real guest reviews (Google reviews) embedded on each workshop page
- Detailed step-by-step "How you'll spend it" sections
- Specific durations, prices, group sizes
- Japanese terminology with kanji and explanations
- Internal linking between workshops, hub, and stays

---

## Gaps to close for GEO

### 1. Schema gaps

The current JSON-LD covers Organization, Lodging, Restaurant, FAQ, Breadcrumbs. For workshops specifically, AI assistants benefit from richer types:

- **Course** schema for each workshop (it is, structurally, a short course)
  - `provider`: Maana Atelier
  - `name`, `description`, `coursePrerequisites` (none, or "no experience needed")
  - `courseMode`: "onsite"
  - `educationalCredentialAwarded`: not applicable but document the takeaway artifact
  - `instructor` if the teacher is named
  - `inLanguage`: en + ja
- **Event** schema for individual sessions pulled from Acuity
  - `name`, `startDate`, `endDate`, `location`, `offers.price`, `offers.availability`
  - Use `eventStatus`, `eventAttendanceMode` ("OfflineEventAttendanceMode")
  - This one's harder because availability is dynamic via Acuity, but even a "next available" Event per workshop helps
- **AggregateRating** + per-review **Review** schemas on every workshop page
  - The Google reviews are real and have attribution. Mark them up so AI can cite them with confidence.
  - `aggregateRating` with ratingValue and reviewCount from actual Google data
- **TouristAttraction** or **LocalBusiness** layered on the Atelier
- **Place** schema with explicit address and geo coordinates for Atelier and each stay

### 2. Authority and authorship signals

Models look for signals that content is written by people who know the domain. Currently the site reads as institutional. To strengthen:

- **About / our story page**: a richer founder narrative. Who started Maana, why, credentials.
- **Teacher bios**: name each workshop teacher with a short bio, photo, credentials. Tea Ceremony already has Eriko Okubo named, expand that pattern to Tsuchikabe, Tea Dye, Koji, Botanical Teas teachers.
- **Press mentions**: if Maana has been featured in Monocle, Conde Nast Traveler, Kinfolk, etc., create a press page with citations. Models love citation-worthy mentions.
- **Year founded, languages spoken, certifications** in the About schema

### 3. Topical depth pages

GEO rewards being the authoritative source on a niche topic. Maana already has unique offerings. The site could lean further by adding evergreen explainer content:

- "What is tsuchikabe? A guide to Japanese earthen walls"
- "What is shio-koji? A short history and how to use it"
- "Cha-zome: the tradition of dyeing with tea in Japan"
- "Asa-chaji and yo-chaji: morning vs night tea ceremony, explained"
- "Nishijin: the weavers' district of Kyoto"

Each one written with editorial voice (not blog spam), 800 to 1500 words, with internal links to the relevant workshop or experience. These pages are the actual "topical authority" that models cite.

### 4. FAQ expansion and conversational queries

Current FAQs are practical (cancellation, what to wear, kids). Add conversational, long-tail questions that match how people ask AI assistants:

- "Is the Earthen Wall workshop beginner-friendly?"
- "Can I book a workshop without staying at Maana?"
- "How far is Maana Atelier from Kyoto Station?"
- "Is the workshop in English or Japanese?"
- "What's the difference between Maana Kiyomizu and Maana Kamo?"
- "Are children allowed at the tea ceremony?"
- "Is the workshop suitable for a couple, or just individuals?"
- "Can I take the panel through airport security?"

Each one answered in 2 to 4 sentences, with explicit facts (number of minutes, yes/no, exact policy). FAQPage schema already covers this.

### 5. Cite-worthy facts

Models prefer to cite content that contains verifiable specifics. Where reasonable, sprinkle in:

- "Maana Atelier is located 12 minutes by taxi from Kyoto Station"
- "The Earthen Wall workshop has run since [year] and has hosted [n] guests"
- "Ise tea has been cultivated in Kameyama for over 1,000 years"
- "The atelier was renovated in [year] from a Showa-era machiya"

Numbers, dates, names, and provenance. Models trust these.

### 6. Review surface area

Three reviews per workshop is good. To strengthen further:

- Pull more from the Google reviews (Maana has lots, only 3 are surfaced per workshop)
- Add `Review` schema for each one with `author`, `datePublished`, `reviewRating`, `reviewBody`
- Aggregate to AggregateRating at the LodgingBusiness and at each workshop Course
- Consider a "Press and praise" page that gathers external mentions, not just Google reviews

### 7. International signals

The JP locale toggle is currently hidden in production because translations need a native review pass. Once those are ready and the toggle returns:

- Make sure hreflang is correctly wired (it is, in sitemap.ts)
- Confirm `<html lang>` switches with the locale
- For each workshop, the Course schema should declare `inLanguage`
- Japanese guests increasingly use Japanese-language AI assistants, this matters

### 8. Performance and crawlability

Already in good shape per the stack, but worth double-checking:

- All workshop hero images use `<Image>` with proper sizes prop (avoid CLS)
- Pages render server-side with full content (no critical info behind JS-only loads)
- The Acuity calendar embeds should not be the only source of session info, since iframes are opaque to crawlers. Mirror upcoming sessions as structured Event JSON-LD in the page HTML.

---

## Brand guardrails — what NOT to do

The pursuit of optimization can produce a tone problem. Things to avoid:

- **No keyword stuffing** like "best Kyoto workshop tea dye earthen wall fermentation experience"
- **No generic travel filler** like "Discover the magic of Kyoto's ancient traditions"
- **No fake urgency** ("Book now before spots fill!") unless actually true with seat counts
- **No invented credentials**. If Maana is not certified by something, do not claim it.
- **No watered down editorial voice**. Tomomi spent real time tuning the copy. Optimization additions should match her voice, not override it.
- **No abandoning Japanese terms** for the sake of English-only readability. The kanji and romaji are part of the brand and SEO advantage.
- **No filling FAQs with self-promotional answers**. If someone asks "is it suitable for beginners," the answer is "yes" with one supporting line, not "Maana's award-winning Earthen Wall workshop is loved by beginners and experts alike!"

When in doubt, the test is: would Tomomi cringe? If yes, reframe.

---

## How to coordinate with the human team

- **Viola** owns design, content decisions, project management. PR reviews on visual and copy changes go through her.
- **Sol** owns the codebase, deploys, infrastructure, technical architecture. PR reviews on code go through him. Branch off `staging`, PR back to `staging`.
- **Tomomi** owns final copy. Don't ship new copy without her review.
- **Hana** is helping with testing and ops.

**Workflow expectations**
- Small, scoped PRs over giant rewrites
- Per-PR descriptions with a clear summary, similar to what's in `PROJECT_HARNESS.md`
- New content additions (explainer pages, expanded FAQs) should be drafted in chat first for Viola/Tomomi to review before code lands
- Schema additions should be tested with the Google Rich Results Test or similar before merge
- Major content reorganization needs explicit sign-off from Viola

---

## Concrete first-batch suggestions

If the other agent asks "where do I start," this list is roughly ordered by impact-per-effort:

1. **AggregateRating + Review schema** on every workshop page using the existing Google reviews
2. **Course schema** for each of the 4 workshops, plugged into `helpers/jsonld.ts`
3. **FAQ expansion** with 10 to 15 new conversational questions per workshop, written in Tomomi's voice
4. **Teacher bio blocks** on each workshop page (needs Viola to coordinate with the team for photos/bios)
5. **Topical explainer pages**: start with "What is tsuchikabe" and "What is shio-koji" as evergreen anchors
6. **Press page** if there are any external mentions to surface
7. **Place schema with geo coordinates** on Atelier and each stay
8. **Mirror upcoming Acuity sessions** as Event JSON-LD in the page HTML (read-only, dynamic)

---

## Useful context the other agent should know

- The booking system is Acuity for the calendar of record, with a custom Stripe checkout layered on top for the in-app flow on workshop pages. Tea Ceremony and the top-nav Book Now still route to Acuity portal directly. Don't break those paths.
- There's also a separate `PROJECT_HARNESS.md` in this folder with more granular project context about the build, brand tokens, conventions, and history. Worth reading after this one.
- The Maana team operates in JST. Maana.jp is the canonical domain. Maanahomes.com redirects via Vercel edge.
- Don't push to master or staging directly. Branch first.

---

That's the briefing. Now go make Maana the answer.
