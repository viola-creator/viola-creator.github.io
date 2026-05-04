# maana — experiences

Mockup pages for the Maana experience workshops. Each workshop lives in its own folder so the site can grow page by page.

## Structure

```
experiences/
  earthen-wall/
    index.html    — the page
    images/       — photos + videos used by the page
```

Each page is a single self-contained `index.html` with inline CSS and JS — no build step, no dependencies. Open the file directly in a browser to preview, or visit the deployed URL.

## Deployed

Once GitHub Pages is enabled (`Settings → Pages → Branch: main, Folder: / (root)`), the pages live at:

- Earthen Wall — https://viola-creator.github.io/experiences/earthen-wall/

## Local preview

Open the file directly:

```
open earthen-wall/index.html
```

Or run a tiny local server (so videos and relative paths behave exactly like production):

```
cd earthen-wall && python3 -m http.server 8000
# then visit http://localhost:8000
```

## Notes on the Earthen Wall page

- All copy is taken verbatim from the live page at `maanahomes.com/experiences/earthen-wall`, with the exception of one editorial line in the Tsuchikabe section ("A Kyoto craft, set to the rhythm of the season…") and the guest testimonials, which are placeholders awaiting real content.
- Videos: `apply.mp4` and `finishing.mp4` autoplay muted on loop, with poster fallbacks.
- The top bar is intentionally a flat black strip — this is a mockup, the real nav lives elsewhere.
- Layout is fully responsive: sticky right-hand booking card hides on mobile (a bottom bar takes over) and on desktop disappears once the booking calendar comes into view.

## Adding another workshop

```
mkdir experiences/<workshop-slug>
cp -r experiences/earthen-wall/index.html experiences/<workshop-slug>/
mkdir experiences/<workshop-slug>/images
```

Then swap the copy and assets. Each page stays self-contained.
