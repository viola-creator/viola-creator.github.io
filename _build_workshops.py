"""Build the 5 new workshop pages from the earthen-wall template.
Run from the repo root:  python3 _build_workshops.py
"""
import re, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(ROOT, 'earthen-wall', 'index.html')).read()

# ---------------------------------------------------------------------------
# Per-workshop data. Keep copy concise; pulled from the saved live pages.
# ---------------------------------------------------------------------------
SHARED_FACT_2 = (
    'Yours the same day',
    'You take it home the same afternoon — wrapped for travel, no fragile fuss.'
)
SHARED_FACT_3 = (
    'A piece of the season',
    'Handmade with seasonal Kyoto materials — one of a kind, made by you.'
)

WORKSHOPS = {
'tea-dye': {
    'title':   'Tea Dye Workshop',
    'desc':    'Design your own drawstring bags with natural dyes from wild tea leaves and shibori patterns. At Maana Atelier, Kyoto.',
    'h1':      'Tea Dye<br/>Workshop.',
    'hero_eyebrow': 'Maana Atelier · Workshop',
    'lede':    'Design your own bags with natural dyes from wild tea leaves and patterns from <em>shibori</em> techniques.',
    'duration':'2 hours', 'capacity':'Up to 8', 'price':'¥38,000',
    'price_note':'Materials included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'hero_bg': 'images/hero.webp',
    'craft_word':'Cha-zome',  'craft_kanji':'茶染',
    'craft_p1':'For centuries in Japan, tea has played an all-encompassing role — from the sacred and ceremonial to the modern daily ritual. Alongside that history, tea leaves have long been used to dye textiles, a quiet tradition of making the most of what nature provides.',
    'craft_p2':'Dyes extracted from tea are gentle on the earth, and every batch produces subtly different hues. In this playful workshop, you\'ll explore natural colour and pattern, designing and dyeing two drawstring bags to take home.',
    'craft_img1':'images/001.jpg',  'craft_img2':'images/002.jpg',
    'takehome_lede':'You leave with two drawstring bags — known in Japan as <em>kinchaku-bukuro</em> (巾着袋) — tea-dyed and folded by your own hands.',
    'fact1':('The bags','One small + one large kinchaku-bukuro, your own pattern, your own colour.'),
    'fact2':SHARED_FACT_2,
    'fact3':('Earth-friendly','Tea-dyeing uses no harmful synthetics — every drop of tea is preserved in the fabric.'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','You\'re greeted at the atelier with a seasonal cup of tea and a quiet introduction to the day.','images/004.jpg'),
        ('ii.','Shibori','Folding, binding, and tying your fabric — the small choices that shape the final pattern.','images/002.jpg'),
        ('iii.','Tea-dyeing','Hand-picked Ise tea (cultivated for over a thousand years in Kameyama) is steeped and your bags are dipped, folded, and re-dipped.','images/001.jpg'),
        ('iv.','Untying','The reveal — undo the ties and watch the design emerge. Pack the bags for the journey home.','images/003.jpg'),
    ],
    'partial':'atelier',
    'sessions_intro':'Tea Dye Workshop runs daily at four start times.',
    'session_times':['9:00 AM','10:00 AM','12:00 PM','3:00 PM'],
    'faq': [
      ('What is the cancellation policy?','0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('Children?','Children aged 6 and older are welcome to join. They will be charged the standard fee.'),
      ('What should I wear?','Please dress accordingly. We recommend wearing dark-coloured clothing. Refrain from wearing strong fragrances.'),
      ('Can I bring my own item to dye?','Yes — please email us in advance to ensure we have enough tea dye prepared. Up to 100g included; over 100g, a fee of ¥14,000 applies. Maximum allowable weight 250g. If you bring your own item, the drawstring bags are not included.'),
      ('What kind of textile?','White or undyed textile made from 100% natural fibre (cotton, linen, silk, hemp).'),
      ('Bilingual?','Conducted in English, with some Japanese if necessary.'),
      ('Private workshops?','Please email atelier@maana.jp with party size and dates.'),
    ],
},
'botanical-teas': {
    'title':   'Kyoto Botanical Teas Workshop',
    'desc':    'Blend your own personalized organic tea from farmed and foraged Japanese herbs. At Maana Atelier, Kyoto.',
    'h1':      'Kyoto Botanical<br/>Teas Workshop.',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'lede':    'Blend your own personalized organic tea from farmed and foraged heirloom herbs of Japan.',
    'duration':'2 hours', 'capacity':'Up to 8', 'price':'¥18,000',
    'price_note':'Tax included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'hero_bg':'images/hero.webp',
    'craft_word':'Sōmoku-cha',  'craft_kanji':'草木茶',
    'craft_p1':'Tea in Japan is far more than the green leaf the world knows. For centuries — long before the tea plant arrived from China — the islands brewed infusions from native flora: roots, leaves, twigs, and barks gathered from forest and field.',
    'craft_p2':'These botanical teas mirror the climate and the season, support physical and mental health, and tell the long story of Japanese agriculture and place. In this workshop, you\'ll smell, touch, and taste a selection of regional ingredients — and blend a tea that\'s entirely your own.',
    'craft_img1':'images/001.jpg', 'craft_img2':'images/002.jpg',
    'takehome_lede':'You leave with a personal tea blend — your hands\' work, the season\'s ingredients, ready to brew at home.',
    'fact1':('Your blend','A jar of your own personalized organic tea, sealed and labelled, ready to take home.'),
    'fact2':SHARED_FACT_2,
    'fact3':('Earth-friendly','Sourced from farmed and wild seasonal flora — no mono-cropping, no soil erosion.'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','A seasonal cup of tea on arrival, and a quiet introduction to the day\'s ingredients.','images/004.jpg'),
        ('ii.','Smell · touch · taste','Yamato Tachibana from Nara, Kuromoji from Yamanashi, Gettou from Okinawa — meet each ingredient on its own.','images/001.jpg'),
        ('iii.','Blending','Compose your own ratio. Layer florals, roots, and citrus until the cup matches your mood.','images/002.jpg'),
        ('iv.','Tasting · take home','Brew your blend. Share notes. Pack the rest in a jar to carry home.','images/003.jpg'),
    ],
    'partial':'atelier',
    'sessions_intro':'Kyoto Botanical Teas runs daily at four start times.',
    'session_times':['9:00 AM','10:00 AM','12:00 PM','3:00 PM'],
    'faq':[
      ('What is the cancellation policy?','0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('Children?','Children aged 6 and older are welcome. They will be charged the standard fee. At least one adult must accompany children under 13.'),
      ('What should I wear?','You\'ll be working with food. Please dress accordingly. Refrain from wearing fragrances.'),
      ('Food allergies?','Yes — please inform us in advance through the intake form when you apply.'),
      ('Bilingual?','Conducted in English, with some Japanese if necessary.'),
      ('Private workshops?','Please email atelier@maana.jp with party size and dates.'),
    ],
},
'koji-fermentation': {
    'title':   'Koji Fermentation Workshop',
    'desc':    'Make two seasonal pantry staples using koji-fermented rice. At Maana Atelier, Kyoto.',
    'h1':      'Koji Fermentation<br/>Workshop.',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'lede':    'Make your own Japanese kitchen condiments from koji-fermented rice — the quiet engine of every umami flavour.',
    'duration':'2 hours', 'capacity':'Up to 8', 'price':'¥18,000',
    'price_note':'Tax included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'hero_bg':'images/hero.webp',
    'craft_word':'Kōji',  'craft_kanji':'発酵',
    'craft_p1':'Miso, shoyu, mirin, pickles — the staples of the Japanese table, all built on a single quiet foundation: <em>koji</em>, the national mould of Japan. Inoculated onto rice, barley, or soy, koji is the starter that turns ingredients into the fermented umami the islands are known for.',
    'craft_p2':'In this workshop, you\'ll learn the spectrum of fermentation styles across Japan and koji\'s vital role — then make two personalized condiments for your own pantry: shoyu-koji rich with dried fruit, or shio-koji with aromatic spices.',
    'craft_img1':'images/001.jpg', 'craft_img2':'images/002.jpg',
    'takehome_lede':'You leave with two jars of your own fermented condiments — ready to settle and finish on your kitchen counter at home.',
    'fact1':('Two jars','Shoyu-koji + shio-koji, made with the koji of your choice and seasonal aromatics. Yours to keep.'),
    'fact2':('A few days to finish','Your jars are nearly there — they continue fermenting at home for 5–7 days, then keep in the fridge.'),
    'fact3':('Better cooking','One spoonful turns a bowl of rice, a piece of fish, or a dressing into something quietly transformed.'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','A seasonal cup of tea on arrival, and an introduction to fermentation across Japan.','images/004.jpg'),
        ('ii.','Meet the koji','Smell, touch, and taste rice koji — the starter that drives miso, soy sauce, and saké.','images/001.jpg'),
        ('iii.','Mix','Combine koji with salt, soy, dried fruit, or aromatics — your choice of shoyu-koji or shio-koji.','images/002.jpg'),
        ('iv.','Bottle','Spoon your blend into a jar to finish at home. Labelled, packed, ready to travel.','images/003.jpg'),
    ],
    'partial':'atelier',
    'sessions_intro':'Koji Fermentation runs daily at four start times.',
    'session_times':['9:00 AM','10:00 AM','12:00 PM','3:00 PM'],
    'faq':[
      ('What is the cancellation policy?','0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('Children?','Children aged 6 and older are welcome. They will be charged the standard fee. At least one adult must accompany children under 13.'),
      ('What should I wear?','You\'ll be working with food. Please dress accordingly. Refrain from wearing fragrances.'),
      ('What should I bring?','Nothing. We provide a workshop kit and all ingredients.'),
      ('Bilingual?','Conducted in English, with some Japanese if necessary.'),
      ('Private workshops?','Please email atelier@maana.jp with party size and dates.'),
    ],
},
'morning-tea': {
    'title':   'Morning Tea Ceremony & Breakfast',
    'desc':    'Asa-chaji at a private Kyoto tea house. Tea Master Eriko Okubo invites you to a Zen-monk breakfast and a morning tea ceremony.',
    'h1':      'Morning Tea Ceremony<br/>&amp; Breakfast.',
    'hero_eyebrow':'Private Tea House · Ceremony',
    'lede':    'Start the morning at a private tea house with a traditional tea ceremony and a Zen-monk\'s breakfast.',
    'duration':'1.5 hours', 'capacity':'Up to 6', 'price':'¥42,000',
    'price_note':'Tax included',
    'venue':'Hekishoken', 'venue_loc':'Private tea house, Kyoto',
    'hero_bg':'images/hero.jpg',
    'craft_word':'Asa-chaji',  'craft_kanji':'朝茶事',
    'craft_p1':'In this rare and intimate offering within the world of tea, Tea Master Eriko Okubo welcomes you to her private tea house, where the day begins with a quiet awakening of the senses.',
    'craft_p2':'You start with a seasonal breakfast inspired by the mindful simplicity of Zen monastic cuisine. Then a tea ceremony — paired with <em>wagashi</em> — unfolds in the still atmosphere of the tea room. The seamless progression from breakfast to tea is known as <em>asa-chaji</em>, rarely experienced outside private circles.',
    'craft_img1':'images/001.jpg', 'craft_img2':'images/002.jpg',
    'takehome_lede':'<em>Mugon</em> 無言 — through the wordlessness of the tea ceremony, body, mind, and spirit align with the natural harmony of the morning.',
    'fact1':('A still morning','Two hours that move at the pace of the tea, the breakfast, and the season outside the window.'),
    'fact2':('Authentic chanoyu','Conducted in the tradition of asa-chaji — rarely available outside invited circles.'),
    'fact3':('Hosted by Eriko Okubo','A Tea Master who has practised in this room for many years. The ceremony is hers to lead.'),
    'takehome_img':'images/003.jpg',
    'spend_steps':[
        ('i.','Arrive','Step into the tea house. Remove shoes. The morning slows immediately.','images/004.jpg'),
        ('ii.','Zen breakfast','A seasonal meal in the spirit of monastic cuisine — simple, careful, beautiful.','images/005.jpg'),
        ('iii.','Wagashi · matcha','The ceremony unfolds. Thin tea, then thick. Each pause is part of the form.','images/006.jpg'),
        ('iv.','Mugon','Leave in silence, the morning still ahead of you.','images/007.jpg'),
    ],
    'partial':'tea-house',
    'sessions_intro':'Held Tuesdays and Saturdays. Booking closes 2 days prior.',
    'session_times':['8:30 AM'],
    'faq':[
      ('What is the cancellation policy?','0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('Children?','Children aged 6 and older are welcome. They will be charged the standard fee. At least one adult must accompany children under 13.'),
      ('What should I wear?','Bring socks and remove any accessories before entering the tea room — this protects the ceramics. Refrain from wearing fragrances.'),
      ('Bilingual?','The ceremony is conducted primarily in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the wordless interaction.'),
      ('Private sessions?','Please email atelier@maana.jp with party size and dates.'),
    ],
},
'night-tea': {
    'title':   'Night Tea Ceremony & Dinner',
    'desc':    'A summer evening at Hekishoken — tea ceremony by candlelight followed by a seasonal multi-course meal.',
    'h1':      'Night Tea Ceremony<br/>&amp; Dinner.',
    'hero_eyebrow':'Private Tea House · Seasonal',
    'lede':    'Spend a summer evening at a private tea house with a candlelit tea ceremony and a seasonal meal.',
    'duration':'2 hours', 'capacity':'Up to 6', 'price':'¥47,500',
    'price_note':'Tax included',
    'venue':'Hekishoken', 'venue_loc':'Private tea house, Kyoto',
    'hero_bg':'images/hero.jpg',
    'craft_word':'Yoru-chaji',  'craft_kanji':'夜茶事',
    'craft_p1':'Tea Master Eriko Okubo invites you to a private tea house hidden in a quiet Kyoto neighbourhood. The night unfolds gently — beginning with a seasonal <em>shi-dashi</em> meal prepared in the tradition of tea, accompanied by selected Japanese saké.',
    'craft_p2':'After dinner, a tea ceremony is held by candlelight — <em>wagashi</em> and matcha, served as stillness descends. This sensory journey from meal to tea forms the <em>yoru-chaji</em>, an authentic evening ritual seldom available to the public.',
    'craft_img1':'images/001.jpg', 'craft_img2':'images/002.jpg',
    'takehome_lede':'<em>Yoin</em> 余韻 — in the quiet reflection of the tea ceremony, the impressions of the day settle within. We carry the lingering resonance.',
    'fact1':('A summer evening','Two hours that move at candlelight pace — meal, ceremony, then the garden settling into dusk.'),
    'fact2':('Seasonal meal','A shi-dashi meal in the tradition of tea, paired with selected Japanese saké.'),
    'fact3':('Hosted by Eriko Okubo','A Tea Master leading the ceremony in her own tea house — intimate, by candlelight.'),
    'takehome_img':'images/003.jpg',
    'spend_steps':[
        ('i.','Arrive at dusk','Step into the tea house as light fades. Remove shoes. The evening begins.','images/004.jpg'),
        ('ii.','Shi-dashi meal','A seasonal multi-course meal in the tradition of tea, with sake.','images/005.jpg'),
        ('iii.','Candlelit ceremony','Wagashi, then matcha. The ceremony unfolds as the room darkens.','images/006.jpg'),
        ('iv.','Yoin','Leave with the resonance of the evening still in you.','images/007.jpg'),
    ],
    'partial':'tea-house',
    'sessions_intro':'Held Tuesdays and Saturdays · July to September only. Booking closes 2 days prior.',
    'session_times':['6:00 PM'],
    'summer_only': True,
    'faq':[
      ('What is the cancellation policy?','0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('Children?','Children aged 6 and older are welcome. They will be charged the standard fee. At least one adult must accompany children under 13.'),
      ('What should I wear?','Bring socks and remove any accessories before entering the tea room — this protects the ceramics. Refrain from wearing fragrances.'),
      ('Bilingual?','The ceremony is conducted primarily in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the wordless interaction.'),
      ('Private sessions?','Please email atelier@maana.jp with party size and dates.'),
    ],
},
}


def build(slug, data):
    html = TEMPLATE
    # Title + meta
    html = html.replace(
        '<title>Earthen Wall Workshop — Maana</title>',
        f'<title>{data["title"]} — Maana</title>'
    )
    html = re.sub(
        r'<meta name="description" content="[^"]*"',
        f'<meta name="description" content="{data["desc"]}"',
        html
    )

    # Hero
    html = re.sub(
        r'<span class="eyebrow">Maana Atelier · Workshop</span>',
        f'<span class="eyebrow">{data["hero_eyebrow"]}</span>',
        html, count=1
    )
    html = html.replace('<h1>Earthen Wall<br/>Workshop.</h1>', f'<h1>{data["h1"]}</h1>')
    html = re.sub(
        r'<p class="lede">[^<]*<em>[^<]*</em>[^<]*</p>',
        f'<p class="lede">{data["lede"]}</p>',
        html, count=1
    )

    # Hero meta strip (4 cells)
    html = re.sub(
        r'<div class="hero-meta">.*?</div>\s*</div>\s*</section>',
        f'''<div class="hero-meta">
      <div><strong>{data["duration"]}</strong>One session</div>
      <div><strong>{data["venue"]}</strong>{data["venue_loc"]}</div>
      <div><strong>{data["capacity"]}</strong>Per session</div>
      <div><strong>{data["price"]}</strong>{data["price_note"]}</div>
    </div>
  </div>
</section>''',
        html, count=1, flags=re.DOTALL
    )

    # Hero background image — change in the .hero-bg CSS reference (inside shared.css we can't, but we use the .hero-bg style)
    # Easier: override via inline style on the hero-bg div
    html = html.replace(
        '<div class="hero-bg" aria-hidden="true"></div>',
        f'<div class="hero-bg" style="background-image:url(\'{data["hero_bg"]}\')" aria-hidden="true"></div>',
        1
    )

    # Craft section
    html = re.sub(
        r'<section class="craft reveal" aria-label="What is Tsuchikabe">.*?</section>',
        f'''<section class="craft reveal" aria-label="What is {data["craft_word"]}">
  <div class="container">
    <div class="craft-grid">
      <div class="craft-text">
        <span class="eyebrow">The craft</span>
        <h2><em>{data["craft_word"]}</em> <span class="kanji-accent">{data["craft_kanji"]}</span></h2>
        <p>{data["craft_p1"]}</p>
        <p>{data["craft_p2"]}</p>
      </div>
      <div class="craft-imgs">
        <div class="craft-img" style="background-image:url('{data["craft_img1"]}')" role="img" aria-label="{data["craft_word"]} material"></div>
        <div class="craft-img" style="background-image:url('{data["craft_img2"]}')" role="img" aria-label="{data["craft_word"]} process"></div>
      </div>
    </div>
  </div>
</section>''',
        html, count=1, flags=re.DOTALL
    )

    # Take home section
    fact = lambda i, f: f'''<li>
              <div class="fact-num">{i:02d}</div>
              <div class="fact-body">
                <h4>{f[0]}</h4>
                <p>{f[1]}</p>
              </div>
            </li>'''

    html = re.sub(
        r'<section class="takehome reveal" aria-label="What you\'ll take home">.*?</section>',
        f'''<section class="takehome reveal" aria-label="What you'll take home">
  <div class="container">
    <div class="takehome-head">
      <span class="eyebrow">Your keepsake</span>
      <h2 class="takehome-h2"><em>What you'll take home</em></h2>
    </div>
    <div class="takehome-grid">
      <div class="takehome-img" style="background-image:url('{data["takehome_img"]}')" role="img" aria-label="Take home"></div>
      <div class="takehome-text">
        <p class="takehome-lede">{data["takehome_lede"]}</p>
        <ul class="takehome-facts">
          {fact(1, data["fact1"])}
          {fact(2, data["fact2"])}
          {fact(3, data["fact3"])}
        </ul>
      </div>
    </div>
  </div>
</section>''',
        html, count=1, flags=re.DOTALL
    )

    # Spend section steps (4 cards)
    spend_card = lambda step: f'''      <article class="spend-card">
        <div class="spend-media">
          <div class="spend-img" style="background-image:url('{step[3]}')"></div>
        </div>
        <div class="spend-card-body">
          <div class="step">{step[0]}</div>
          <h3>{step[1]}</h3>
          <p>{step[2]}</p>
        </div>
      </article>'''
    cards = '\n'.join(spend_card(s) for s in data['spend_steps'])

    html = re.sub(
        r'<div class="spend-grid">.*?</div>\s*</div>\s*</section>\s*<!-- ========== SESSIONS',
        f'''<div class="spend-grid">
{cards}
    </div>
  </div>
</section>

<!-- ========== SESSIONS''',
        html, count=1, flags=re.DOTALL
    )

    # Replace atelier partial reference for tea-house workshops
    if data['partial'] == 'tea-house':
        html = html.replace(
            '<div data-include="../_partials/atelier.html"></div>',
            '<div data-include="../_partials/tea-house.html"></div>'
        )

    # Update the hero-bg CSS rule that lives in shared.css — instead, override via data already done above.
    # The .hero-bg in shared.css uses the earthen wall image as fallback; we override with inline style.
    # No further action needed here.

    # FAQ section — replace items
    faq_items = '\n      '.join(
        f'''<div class="faq-item">
        <button class="faq-q">{q}<span class="plus">+</span></button>
        <div class="faq-a">{a}</div>
      </div>'''
        for q, a in data['faq']
    )
    html = re.sub(
        r'<div class="faq-list">.*?</div>\s*</div>\s*</section>\s*<!-- ========== OTHER',
        f'''<div class="faq-list">
      {faq_items}
    </div>
  </div>
</section>

<!-- ========== OTHER''',
        html, count=1, flags=re.DOTALL
    )

    # Other Experiences — mark current one
    # The earthen-wall has its own card; we want to mark this workshop as "current"
    # but show the others. Simpler: in the experiences grid, swap which card is the "current" one.
    # Skip this for now — the grid would still show all 6, including the workshop you're on.

    # Write the file
    out_dir = os.path.join(ROOT, slug)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'index.html'), 'w') as f:
        f.write(html)
    print(f'  built {slug}/index.html ({len(html):,} bytes)')


def main():
    print('Building 5 workshop pages from earthen-wall template...')
    for slug, data in WORKSHOPS.items():
        build(slug, data)
    print('Done.')

if __name__ == '__main__':
    main()
