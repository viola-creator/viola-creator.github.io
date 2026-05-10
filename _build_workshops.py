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

# All 6 workshop cards used by the "Other experiences" grid. Each page
# excludes its own slug from the grid.
EXPERIENCES_CARDS = [
    {'slug':'earthen-wall',     'title':'Earthen Wall',         'venue':'Maana Atelier',     'img':'showcase-earthen-wall.jpg',         'href':'../earthen-wall/'},
    {'slug':'tea-dye',          'title':'Tea Dye',              'venue':'Maana Atelier',     'img':'showcase-tea-dye.jpg',              'href':'../tea-dye/'},
    {'slug':'botanical-teas',   'title':'Botanical Teas',       'venue':'Maana Atelier',     'img':'showcase-botanical-tea.jpg',        'href':'../botanical-teas/'},
    {'slug':'koji-fermentation','title':'Fermentation',         'venue':'Maana Atelier',     'img':'showcase-koji-fermentation.jpg',    'href':'../koji-fermentation/'},
    {'slug':'morning-tea',      'title':'Morning Tea Ceremony', 'venue':'Private Tea House', 'img':'showcase-tea-ceremony-morning.jpg', 'href':'../morning-tea/'},
    {'slug':'night-tea',        'title':'Night Tea Ceremony',   'venue':'Private Tea House', 'img':'showcase-tea-ceremony-night.jpg',   'href':'../night-tea/'},
]

def build_experiences_grid(current_slug):
    """Return the HTML for the 5-card other-experiences grid, excluding current_slug."""
    cards = []
    for c in EXPERIENCES_CARDS:
        if c['slug'] == current_slug: continue
        cards.append(f"""      <a class="exp-card" href="{c['href']}">
        <div class="photo"><img src="../_partials/images/{c['img']}" alt="" loading="lazy"/></div>
        <div class="venue">{c['venue']}</div>
        <div class="title">{c['title']}</div>
      </a>""")
    return '\n'.join(cards)


WORKSHOPS = {
'tea-dye': {
    'wk_key':'tea-dye',
    'show_img':'../_partials/images/showcase-tea-dye.jpg',
    'sessions_data':[('2026-05-05', '12:00 PM'), ('2026-05-08', '10:00 AM'), ('2026-05-12', '3:00 PM'), ('2026-05-15', '9:00 AM'), ('2026-05-19', '10:00 AM'), ('2026-05-22', '12:00 PM'), ('2026-05-26', '9:00 AM'), ('2026-05-29', '3:00 PM'), ('2026-06-02', '10:00 AM'), ('2026-06-05', '12:00 PM'), ('2026-06-09', '9:00 AM'), ('2026-06-12', '3:00 PM')],
    'title':   'Tea Dye Workshop',
    'desc':    'Design your own drawstring bags with natural dyes from wild tea leaves and shibori patterns. At Maana Atelier, Kyoto.',
    'h1':      'Tea Dye<br/>Workshop.',
    'hero_eyebrow': 'Maana Atelier · Workshop',
    'lede':    'Design your own bags with natural dyes from wild tea leaves and patterns from <em>shibori</em> techniques.',
    'duration':'2 hours', 'capacity':'Up to 8', 'price':'¥38,000',
    'price_note':'Materials included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'sessions_h2':'Tea Dye sessions.',
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
    'faq':[
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the workshop?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', 'Clothing may get dirty during the dyeing. Please dress accordingly — we recommend dark-coloured clothing — and refrain from wearing strong fragrances.'),
      ('Can I bring my own item to dye?', "Yes — you're welcome to bring your own item. All items must be pre-approved by email before the workshop so we can prepare enough tea dye. Up to 100g is included; for items over 100g a fee of ¥14,000 applies, with a 250g maximum. Note that if you bring your own item, the drawstring bags are not included."),
      ('What kind of textile can I bring?', 'Please bring a white or undyed textile made from 100% natural fibre — cotton, linen, silk, or hemp.'),
      ('Is the workshop bilingual?', 'No, the workshop will be conducted in English, with some Japanese if necessary.'),
      ('Do you accommodate private workshops?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
},
'botanical-teas': {
    'wk_key':'botanical',
    'show_img':'../_partials/images/showcase-botanical-tea.jpg',
    'sessions_data':[('2026-05-06', '12:00 PM'), ('2026-05-09', '10:00 AM'), ('2026-05-13', '3:00 PM'), ('2026-05-16', '9:00 AM'), ('2026-05-20', '10:00 AM'), ('2026-05-23', '12:00 PM'), ('2026-05-27', '9:00 AM'), ('2026-05-30', '3:00 PM'), ('2026-06-03', '10:00 AM'), ('2026-06-06', '12:00 PM'), ('2026-06-10', '9:00 AM'), ('2026-06-13', '3:00 PM')],
    'title':   'Kyoto Botanical Teas Workshop',
    'desc':    'Blend your own personalized organic tea from farmed and foraged Japanese herbs. At Maana Atelier, Kyoto.',
    'h1':      'Kyoto Botanical<br/>Teas Workshop.',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'lede':    'Blend your own personalized organic tea from farmed and foraged heirloom herbs of Japan.',
    'duration':'1.5 hours', 'capacity':'Up to 8', 'price':'¥18,000',
    'price_note':'Tax included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'sessions_h2':'Botanical Teas sessions.',
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
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the workshop?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', "You'll be working with food. Please dress accordingly and refrain from wearing fragrances."),
      ('Do you accommodate food allergies?', 'Yes — we accommodate food allergies. Please inform us in advance of any dietary requirements or allergies through the intake form when you apply.'),
      ('What should I bring?', "You don't need to bring anything. We provide all ingredients and a workshop kit."),
      ('Is the workshop bilingual?', 'No, the workshop will be conducted in English, with some Japanese if necessary.'),
      ('Do you accommodate private workshops?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
},
'koji-fermentation': {
    'wk_key':'fermentation',
    'show_img':'../_partials/images/showcase-koji-fermentation.jpg',
    'sessions_data':[('2026-05-07', '12:00 PM'), ('2026-05-10', '10:00 AM'), ('2026-05-14', '3:00 PM'), ('2026-05-17', '9:00 AM'), ('2026-05-21', '10:00 AM'), ('2026-05-24', '12:00 PM'), ('2026-05-28', '9:00 AM'), ('2026-05-31', '3:00 PM'), ('2026-06-04', '10:00 AM'), ('2026-06-07', '12:00 PM'), ('2026-06-11', '9:00 AM'), ('2026-06-14', '3:00 PM')],
    'title':   'Koji Fermentation Workshop',
    'desc':    'Make two seasonal pantry staples using koji-fermented rice. At Maana Atelier, Kyoto.',
    'h1':      'Koji Fermentation<br/>Workshop.',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'lede':    'Make your own Japanese kitchen condiments from koji-fermented rice — the quiet engine of every umami flavour.',
    'duration':'1.5 hours', 'capacity':'Up to 8', 'price':'¥18,000',
    'price_note':'Tax included',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto',
    'sessions_h2':'Koji Fermentation sessions.',
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
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the workshop?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', "You'll be working with food. Please dress accordingly and refrain from wearing fragrances."),
      ('What should I bring?', "You don't need to bring anything. We provide a workshop kit and all ingredients."),
      ('Do you accommodate food allergies?', 'Yes — please inform us of any dietary requirements or allergies through the intake form when you apply.'),
      ('Is the workshop bilingual?', 'No, the workshop will be conducted in English, with some Japanese if necessary.'),
      ('Do you accommodate private workshops?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
},
'morning-tea': {
    'wk_key':'morning',
    'show_img':'../_partials/images/showcase-tea-ceremony-morning.jpg',
    'sessions_data':[('2026-05-05', '8:30 AM'), ('2026-05-09', '8:30 AM'), ('2026-05-12', '8:30 AM'), ('2026-05-16', '8:30 AM'), ('2026-05-19', '8:30 AM'), ('2026-05-23', '8:30 AM'), ('2026-05-26', '8:30 AM'), ('2026-05-30', '8:30 AM'), ('2026-06-02', '8:30 AM'), ('2026-06-06', '8:30 AM'), ('2026-06-09', '8:30 AM'), ('2026-06-13', '8:30 AM')],
    'title':   'Morning Tea Ceremony & Breakfast',
    'desc':    'Asa-chaji at a private Kyoto tea house. Tea Master Eriko Okubo invites you to a Zen-monk breakfast and a morning tea ceremony.',
    'h1':      'Morning Tea Ceremony<br/>&amp; Breakfast.',
    'hero_eyebrow':'Private Tea House · Excursion',
    'lede':    'Start the morning at a private tea house with a traditional tea ceremony and a Zen-monk\'s breakfast.',
    'duration':'1.5 hours', 'capacity':'Up to 6', 'price':'¥42,000',
    'price_note':'Tax included',
    'venue':'Hekishoken', 'venue_loc':'Private tea house, Kyoto',
    'sessions_h2':'Morning Tea Ceremony sessions.',
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
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the experience?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', 'We kindly ask you to bring socks and remove any accessories before entering the tea room — this protects the ceramics from damage. Please also refrain from wearing fragrances.'),
      ('Is the experience bilingual?', 'The tea ceremony will primarily be conducted in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the participants and the tranquility of wordless interaction. We invite you to experience the silent conversation by sensing the movements and the atmosphere.'),
      ('Do you accommodate private sessions?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
},
'night-tea': {
    'wk_key':'night',
    'show_img':'../_partials/images/showcase-tea-ceremony-night.jpg',
    'sessions_data':[('2026-07-04', '6:00 PM'), ('2026-07-07', '6:00 PM'), ('2026-07-11', '6:00 PM'), ('2026-07-14', '6:00 PM'), ('2026-07-18', '6:00 PM'), ('2026-07-21', '6:00 PM'), ('2026-07-25', '6:00 PM'), ('2026-07-28', '6:00 PM'), ('2026-08-01', '6:00 PM'), ('2026-08-04', '6:00 PM'), ('2026-08-08', '6:00 PM'), ('2026-08-11', '6:00 PM')],
    'title':   'Night Tea Ceremony & Dinner',
    'desc':    'A summer evening at Hekishoken — tea ceremony by candlelight followed by a seasonal multi-course meal.',
    'h1':      'Night Tea Ceremony<br/>&amp; Dinner.',
    'hero_eyebrow':'Private Tea House · Excursion',
    'lede':    'Spend a summer evening at a private tea house with a candlelit tea ceremony and a seasonal meal.',
    'duration':'2 hours', 'capacity':'Up to 6', 'price':'¥47,500',
    'price_note':'Tax included',
    'venue':'Hekishoken', 'venue_loc':'Private tea house, Kyoto',
    'sessions_h2':'Night Tea Ceremony sessions.',
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
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the experience?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', 'We kindly ask you to bring socks and remove any accessories before entering the tea room — this protects the ceramics from damage. Please also refrain from wearing fragrances.'),
      ('Is the experience bilingual?', 'The tea ceremony will primarily be conducted in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the participants and the tranquility of wordless interaction. We invite you to experience the silent conversation by sensing the movements and the atmosphere.'),
      ('Do you accommodate private sessions?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
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


    # Localize the calendar JS data block to this workshop ----------------------
    wk = data.get('wk_key','earthen')
    show_img = data.get('show_img', '../_partials/images/showcase-earthen-wall.jpg')

    # 1) Static <h3 id="ns-title"> placeholder
    html = re.sub(
        r'<h3 id="ns-title">[^<]*</h3>',
        f'<h3 id="ns-title">{data["title"]}</h3>',
        html, count=1
    )

    # 2) Drop the filter chip row entirely (single-workshop pages don't need it)
    html = re.sub(
        r'<div class="filter-row" id="filter-row">.*?</div>',
        '<div class="filter-row" id="filter-row" style="display:none"></div>',
        html, count=1, flags=re.DOTALL
    )

    # 3) Replace WORKSHOPS object with a single-entry one for this workshop
    name = data['title'].replace(' Workshop','').replace(' & ',' &amp; ')
    desc = data.get('lede','').replace("'", "\\'")
    workshops_block = (
        "const WORKSHOPS = {\n"
        f"  '{wk}': {{ name: '{name}', cls: '', "
        f"tint: '#ecd5bf', desc: '{desc}', "
        f"loc: '{data.get('venue','Maana Atelier')}, {data.get('venue_loc','Kyoto')}', "
        f"price: '{data.get('price','¥38,000')}', img: '{show_img}' }},\n"
        "};"
    )
    html = re.sub(
        r'const WORKSHOPS = \{[^}]*\}[^}]*\};',
        workshops_block,
        html, count=1, flags=re.DOTALL
    )

    # 4) Replace SESSIONS array
    sess_lines = ',\n  '.join(
        f"{{ date:'{d}', time:'{t}', wk:'{wk}' }}"
        for d, t in data.get('sessions_data', [])
    )
    html = re.sub(
        r'const SESSIONS = \[[^\]]*\];',
        f'const SESSIONS = [\n  {sess_lines}\n];',
        html, count=1, flags=re.DOTALL
    )

    # 5) activeFilter default
    html = re.sub(
        r"let activeFilter = '[^']*';",
        f"let activeFilter = '{wk}';",
        html, count=1
    )

    # 6) Side-panel default image
    html = html.replace(
        "../_partials/images/showcase-earthen-wall.jpg",
        show_img
    )

    # Rewrite shared-image refs to use ../_partials/images/
    for img in ['atelier-2.jpg','kri.jpg','summer.jpg',
                'showcase-tea-dye.jpg','showcase-botanical-tea.jpg',
                'showcase-koji-fermentation.jpg','showcase-earthen-wall.jpg',
                'showcase-tea-ceremony-morning.jpg','showcase-tea-ceremony-night.jpg']:
        html = html.replace(f"images/{img}", f"../_partials/images/{img}")
    # Guest panels (1-12)
    for i in range(1,13):
        html = html.replace(f"images/guest{i}.jpg", f"../_partials/images/guest{i}.jpg")

    # Sessions h2 — replace the calendar's "Earthen Wall sessions." heading
    if 'sessions_h2' in data:
        html = html.replace('<h2>Earthen Wall sessions.</h2>',
                            f'<h2>{data["sessions_h2"]}</h2>')


    # Replace the experiences grid with per-workshop cards (excludes current slug)
    grid_html = build_experiences_grid(slug)
    html = re.sub(
        r'<div class="exp-grid">.*?</div>\s*</div>\s*</section>',
        f'<div class="exp-grid">\n{grid_html}\n    </div>\n  </div>\n</section>',
        html, count=1, flags=re.DOTALL
    )

    # Voices section: change h2 to "What people say" — or remove entire section for night-tea
    if slug == 'night-tea':
        html = re.sub(
            r'<!-- ========== GUEST VOICES.*?</section>\s*',
            '',
            html, count=1, flags=re.DOTALL
        )
    else:
        html = html.replace(
            '<h2><em>What people carry home</em></h2>',
            '<h2><em>What people say</em></h2>'
        )

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
