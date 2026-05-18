"""Build the 5 new workshop pages from the earthen-wall template.
Run from the repo root:  python3 _build_workshops.py
"""
import re, os, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = open(os.path.join(ROOT, 'earthen-wall', 'index.html')).read()

# ---------------------------------------------------------------------------
# Bilingual helper. Emits dual <span class="lang-en|lang-jp"> markers so the
# language toggle script (./_partials/nav.js) can swap them via CSS. Falls
# back to the English string when no Japanese is provided.
# ---------------------------------------------------------------------------
def bi(en, jp=None):
    if jp is None or jp == en:
        return en
    return f'<span class="lang-en">{en}</span><span class="lang-jp">{jp}</span>'

def bi_data(data, key):
    """Look up data[key] and data[key + '_jp'] and emit bilingual markup."""
    return bi(data.get(key, ''), data.get(f'{key}_jp'))

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

# Two FAQ items that apply to every workshop / experience — auto-appended
# to each workshop's faq list at build time.
SHARED_FAQ_TAIL = [
    ('If I am running late, where should I contact?',
     'Please contact us via email at <a href="mailto:atelier@maana.jp">atelier@maana.jp</a> or via WhatsApp using the contact details provided in your confirmation email.'),
    ('Can I reschedule my workshop?',
     'Yes. You may reschedule your workshop through the link in your confirmation email up to 7 days prior to your scheduled date.'),
]
SHARED_FAQ_TAIL_JP = [
    ('遅れる場合の連絡先を教えてください。',
     'メールにて <a href="mailto:atelier@maana.jp">atelier@maana.jp</a> までご連絡いただくか、ご予約確認メールに記載のWhatsAppまでご連絡ください。'),
    ('ワークショップの日程変更はできますか。',
     'はい。開催日の7日前まで、ご予約確認メールのリンクから日程変更を承っております。'),
]

# All 6 workshop cards used by the "Other experiences" grid. Each page
# excludes its own slug from the grid.
EXPERIENCES_CARDS = [
    {'slug':'earthen-wall',     'title':'Earthen Wall',         'title_jp':'土壁',           'venue':'Maana Atelier',     'venue_jp':'Maana アトリエ',     'img':'showcase-earthen-wall.jpg',         'href':'../earthen-wall/'},
    {'slug':'tea-dye',          'title':'Tea Dye',              'title_jp':'茶染',           'venue':'Maana Atelier',     'venue_jp':'Maana アトリエ',     'img':'showcase-tea-dye.jpg',              'href':'../tea-dye/'},
    {'slug':'botanical-teas',   'title':'Botanical Teas',       'title_jp':'ボタニカルティー','venue':'Maana Atelier',    'venue_jp':'Maana アトリエ',     'img':'showcase-botanical-tea.jpg',        'href':'../botanical-teas/'},
    {'slug':'koji-fermentation','title':'Fermentation',         'title_jp':'コウジ発酵',     'venue':'Maana Atelier',     'venue_jp':'Maana アトリエ',     'img':'showcase-koji-fermentation.jpg',    'href':'../koji-fermentation/'},
    {'slug':'morning-tea',      'title':'Morning Tea Ceremony', 'title_jp':'朝の茶事',       'venue':'Private Tea House', 'venue_jp':'貸切茶室',           'img':'showcase-tea-ceremony-morning.jpg', 'href':'../morning-tea/'},
    {'slug':'night-tea',        'title':'Night Tea Ceremony',   'title_jp':'夜の茶事',       'venue':'Private Tea House', 'venue_jp':'貸切茶室',           'img':'showcase-tea-ceremony-night.jpg',   'href':'../night-tea/'},
]

def build_experiences_grid(current_slug):
    """Return the HTML for the 5-card other-experiences grid, excluding current_slug."""
    cards = []
    for c in EXPERIENCES_CARDS:
        if c['slug'] == current_slug: continue
        cards.append(f"""      <a class="exp-card" href="{c['href']}">
        <div class="photo"><img src="../_partials/images/{c['img']}" alt="" loading="lazy"/></div>
        <div class="venue">{bi(c['venue'], c['venue_jp'])}</div>
        <div class="title">{bi(c['title'], c['title_jp'])}</div>
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
    'h1_jp': '茶染<br/>ワークショップ。',
    'hero_eyebrow': 'Maana Atelier · Workshop',
    'hero_eyebrow_jp': 'Maana アトリエ ・ ワークショップ',
    'lede':    'Design your own bags with natural dyes from wild tea leaves and patterns from <em>shibori</em> techniques.',
    'lede_jp': 'お茶の自然な染料と<em>絞り</em>の技法で、ご自身だけの巾着袋をデザインしましょう。',
    'duration':'2 hours',
    'duration_jp': '2時間', 'capacity':'Up to 8', 'capacity_jp': '最大8名', 'price':'¥38,000',
    'price_note':'Materials included',
    'price_note_jp': '材料費込み',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto', 'venue_loc_jp': '京都・西陣',
    'sessions_h2':'Tea Dye sessions.',
    'sessions_h2_jp': '茶染ワークショップの日程。',
    'gallery_count': 9,
    'hero_bg': 'images/hero.jpeg',
    'craft_word':'Cha-zome',  'craft_kanji':'茶染',
    'craft_p1':'For centuries in Japan, tea has played an all-encompassing role — from the sacred and ceremonial to the modern daily ritual. Alongside that history, tea leaves have long been used to dye textiles, a quiet tradition of making the most of what nature provides.',
    'craft_p1_jp': 'お茶は何世紀にもわたり、日本の暮らしのあらゆる場面に寄り添ってきました。神聖な儀礼から日々の習わしまで。その歴史と並んで、茶葉は布を染める素材としても古くから用いられ、自然の恵みを大切に使い切る、静かな伝統が受け継がれてきました。',
    'craft_p2':'Dyes extracted from tea are gentle on the earth, and every batch produces subtly different hues. In this playful workshop, you\'ll explore natural colour and pattern, designing and dyeing two drawstring bags to take home.',
    'craft_p2_jp': '茶から抽出した染液は地球にやさしく、染め上がりは一回ごとに少しずつ異なる、繊細な色合いを見せてくれます。本ワークショップでは、自然の色と模様を楽しみながら、ご自身の手で大小2つの巾着袋をデザイン・染色していただきます。',
    'craft_img':'images/001.jpeg',
    'takehome_lede':'You leave with two drawstring bags — known in Japan as <em>kinchaku-bukuro</em> (巾着袋) — tea-dyed and folded by your own hands.',
    'takehome_lede_jp': '2つの<em>巾着袋</em>を、ご自身の手で染め上げ、結んだままお持ち帰りいただけます。',
    'fact1':('The bags','One small + one large kinchaku-bukuro, your own pattern, your own colour.'),
    'fact2':('Yours the same day','You take it home once the workshop ends — packed for travel, no fragile fuss.'),
    'fact3':('Earth-friendly','Tea-dyeing uses no harmful synthetics, while tea\'s natural antibacterial properties make it ideal for storing everyday essentials.'),
    'fact1_jp':('巾着袋','大小の巾着袋を1つずつ。ご自身で選ぶ模様と色合いで。'),
    'fact2_jp':('当日お持ち帰り','ワークショップ終了後、そのままお持ち帰りいただけます。旅にも便利な仕様です。'),
    'fact3_jp':('地球にやさしく','化学染料は一切使用しません。茶葉が持つ自然の抗菌作用により、日々の小物を収納するのにも最適です。'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','You\'re greeted at the atelier with a seasonal cup of tea and a quiet introduction to the day.','images/003.jpeg'),
        ('ii.','Shibori','Folding, binding, and tying your fabric — the small choices that shape the final pattern.','images/004.jpg'),
        ('iii.','Tea-dyeing','Hand-picked Ise tea (cultivated for over a thousand years in Kameyama) is steeped and your bags are dipped, folded, and re-dipped.','images/005.jpg'),
        ('iv.','Untying','The reveal — undo the ties and watch the design emerge. Pack the bags for the journey home.','images/006.jpg'),
    ],
    'spend_steps_jp':[
        ('i.','ウェルカムティー','アトリエにて季節のお茶でお迎えし、本日の流れをゆっくりとご案内いたします。',''),
        ('ii.','絞り','布を折り、しばり、結びます。その小さな選択の一つひとつが、仕上がりの模様を形作っていきます。',''),
        ('iii.','茶で染める','千年以上にわたり亀山で育まれてきた伊勢茶を煎じ、布をくり返し浸し、ひらき、染め重ねていきます。',''),
        ('iv.','ほどく','結びをほどき、模様が現れる瞬間。旅にお持ち帰りいただきやすいよう包んでお渡しいたします。',''),
    ],
    'partial':'atelier',
    'sessions_intro':'Tea Dye Workshop runs daily at four start times.',
    'sessions_intro_jp': '茶染ワークショップは毎日4つの開始時間からお選びいただけます。',
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
    'faq_jp':[
      ('キャンセル規定について教えてください。', '開催日の7日前までは無料でキャンセルいただけます。それ以降は100%のキャンセル料を申し受けます。'),
      ('お子様の参加について教えてください。', '6歳以上のお子様はご参加いただけます（通常料金）。13歳未満のお子様は、保護者の方の同伴をお願いいたします。'),
      ('服装について教えてください。', '染色中にお洋服が汚れる場合がございます。汚れてもよい服装（できれば濃色のお召し物）でお越しください。香りの強い香水のご使用はお控えください。'),
      ('染める素材を持参してもよいですか。', 'はい、お持ち込みいただけます。お茶の染液をご準備する都合上、必ず事前にメールでご相談ください。100gまでは料金内、100gを超える場合は¥14,000を追加でいただきます（最大250gまで）。お持ち込みの場合、巾着袋は含まれません。'),
      ('どんな布を持って行けばよいですか。', '天然繊維100%（コットン、リネン、シルク、ヘンプ）の白または無染色の布をご用意ください。'),
      ('バイリンガル対応はしていますか。', 'ワークショップは基本的に英語で進行いたします。必要に応じて日本語でもご説明いたします。'),
      ('貸切のワークショップに対応していますか。', 'ご希望の人数とご来訪日を添えて、atelier@maana.jpまでご連絡ください。'),
    ],
},
'botanical-teas': {
    'wk_key':'botanical',
    'show_img':'../_partials/images/showcase-botanical-tea.jpg',
    'sessions_data':[('2026-05-06', '12:00 PM'), ('2026-05-09', '10:00 AM'), ('2026-05-13', '3:00 PM'), ('2026-05-16', '9:00 AM'), ('2026-05-20', '10:00 AM'), ('2026-05-23', '12:00 PM'), ('2026-05-27', '9:00 AM'), ('2026-05-30', '3:00 PM'), ('2026-06-03', '10:00 AM'), ('2026-06-06', '12:00 PM'), ('2026-06-10', '9:00 AM'), ('2026-06-13', '3:00 PM')],
    'title':   'Kyoto Botanical Teas Workshop',
    'desc':    'Blend your own personalized organic tea from farmed and foraged Japanese herbs. At Maana Atelier, Kyoto.',
    'h1':      'Kyoto Botanical<br/>Teas Workshop.',
    'h1_jp': '京都ボタニカル<br/>ティー・ワークショップ。',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'hero_eyebrow_jp': 'Maana アトリエ ・ ワークショップ',
    'lede':    'Blend your own personalized organic tea from farmed and foraged heirloom herbs of Japan.',
    'lede_jp': '日本各地で育まれた農の恵みと野草から、ご自身だけの和ハーブティーをブレンドしましょう。',
    'duration':'1.5 hours',
    'duration_jp': '1時間30分', 'capacity':'Up to 8', 'capacity_jp': '最大8名', 'price':'¥18,000',
    'price_note':'Tax included',
    'price_note_jp': '税込',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto', 'venue_loc_jp': '京都・西陣',
    'sessions_h2':'Botanical Teas sessions.',
    'sessions_h2_jp': 'ボタニカルティーの日程。',
    'hero_bg':'images/hero.jpeg',
    'craft_word':'Sōmoku-cha',  'craft_kanji':'草木茶',
    'craft_p1':'Tea in Japan is far more than the green leaf the world knows. For centuries — long before the tea plant arrived from China — the islands brewed infusions from native flora: roots, leaves, twigs, and barks gathered from forest and field.',
    'craft_p1_jp': '日本における「お茶」は、世界が知る緑茶だけにとどまりません。中国から茶の木が伝わるはるか以前から、日本列島では森や野に育つ草・葉・枝・樹皮を煎じ、土地ごとのお茶として暮らしに取り入れてきました。',
    'craft_p2':'These botanical teas mirror the climate and the season, support physical and mental health, and tell the long story of Japanese agriculture and place. In this workshop, you\'ll smell, touch, and taste a selection of regional ingredients — and blend a tea that\'s entirely your own.',
    'craft_p2_jp': 'こうした草木茶は、土地の気候と季節をそのまま映し、心身を整え、日本の農と風土の物語を静かに伝えます。本ワークショップでは、各地の素材を香り、触れ、味わっていただきながら、あなただけの一杯をブレンドしていただきます。',
    'craft_img':'images/001.jpg',
    'takehome_lede':'You leave with a personal tea blend — your hands\' work, the season\'s ingredients, ready to brew at home.',
    'takehome_lede_jp': 'ご自身でブレンドした和ハーブティーを、季節の素材とともにお持ち帰りいただきます。ご自宅でゆっくりと淹れてお楽しみください。',
    'fact1':('Your blend','A bag of your own personalized organic tea, sealed and labelled, ready to take home.'),
    'fact2':('Yours the same day','You take it home once the workshop ends — light for travel, easy to bring.'),
    'fact3':('Earth-friendly','Sourced from farmed and wild seasonal flora — no mono-cropping, no soil erosion.'),
    'fact1_jp':('あなたのブレンド','ご自身でブレンドした和ハーブティーを、密封・ラベル付きでお持ち帰りいただけます。'),
    'fact2_jp':('当日お持ち帰り','ワークショップ終了後、そのままお持ち帰りいただけます。軽くて旅にも便利です。'),
    'fact3_jp':('地球にやさしく','農地と野で採取した季節の植物を使用。単一作物に依存せず、土壌の負担も最小限に。'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','A seasonal cup of tea on arrival, and a quiet introduction to the day\'s ingredients.','images/003.jpg'),
        ('ii.','Smell · touch · taste','Yamato Tachibana from Nara, Kuromoji from Yamanashi, Gettou from Okinawa — meet each ingredient on its own.','images/004.jpg'),
        ('iii.','Blending','Compose your own ratio. Layer florals, roots, and citrus until the cup matches your mood.','images/005.jpg'),
        ('iv.','Tasting · take home','Brew your blend. Share notes. Pack the rest in a bag to carry home.','images/006.jpg'),
    ],
    'spend_steps_jp':[
        ('i.','ウェルカムティー','到着後、季節のお茶を一杯。本日扱う素材についてゆっくりとご紹介します。',''),
        ('ii.','香り・触れ・味わう','奈良の大和橘、山梨のクロモジ、沖縄の月桃──素材一つひとつにじっくりと向き合います。',''),
        ('iii.','ブレンド','配合はあなた次第。花、根、柑橘を重ねながら、その日の気分に合う一杯を組み立てていきます。',''),
        ('iv.','味わう ・ お持ち帰り','淹れて味わい、感想を分かち合います。残りは袋に詰めてお持ち帰りに。',''),
    ],
    'partial':'atelier',
    'sessions_intro':'Kyoto Botanical Teas runs daily at four start times.',
    'sessions_intro_jp': '京都ボタニカルティーは毎日4つの開始時間からお選びいただけます。',
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
    'faq_jp':[
      ('キャンセル規定について教えてください。', '開催日の7日前までは無料でキャンセルいただけます。それ以降は100%のキャンセル料を申し受けます。'),
      ('お子様の参加について教えてください。', '6歳以上のお子様はご参加いただけます（通常料金）。13歳未満のお子様は、保護者の方の同伴をお願いいたします。'),
      ('服装について教えてください。', '食材を扱いますので、汚れてもよい服装でお越しください。香水のご使用はお控えください。'),
      ('食物アレルギーには対応していますか。', 'はい、対応しております。ご予約時の事前フォームにて、アレルギーや食事制限を必ずお知らせください。'),
      ('持ち物について教えてください。', '特にご用意いただくものはございません。材料・道具一式はこちらでご用意いたします。'),
      ('バイリンガル対応はしていますか。', 'ワークショップは基本的に英語で進行いたします。必要に応じて日本語でもご説明いたします。'),
      ('貸切のワークショップに対応していますか。', 'ご希望の人数とご来訪日を添えて、atelier@maana.jpまでご連絡ください。'),
    ],
},
'koji-fermentation': {
    'wk_key':'fermentation',
    'show_img':'../_partials/images/showcase-koji-fermentation.jpg',
    'extras_intro':('In your kitchen', 'A few simple ways to put your jars to work — bright, fresh salads where shio-koji does the seasoning.'),
    'extras_cards':[
        {
            'title': 'Avocado salad',
            'ingredients': ['Cubed avocado', 'Cubed cucumber', 'Crushed cashews', 'Shio-koji', 'Fresh lemon juice'],
            'note': 'Toss and rest five minutes. The shio-koji softens the avocado and binds the cashews into a creamy dressing.',
            'img': 'images/008.jpg',
        },
        {
            'title': 'Tomato salad',
            'ingredients': ['Sliced tomatoes', 'Shio-koji', 'Torn basil', 'Crushed walnuts', 'Fresh lemon juice'],
            'note': 'Dress just before serving. Shio-koji draws the sweetness from the tomatoes; basil and walnuts round it out.',
            'img': 'images/009.jpg',
            'img_pos': 'center bottom',
        },
    ],
    'strip_voices_gallery': True,
    'sessions_data':[('2026-05-07', '12:00 PM'), ('2026-05-10', '10:00 AM'), ('2026-05-14', '3:00 PM'), ('2026-05-17', '9:00 AM'), ('2026-05-21', '10:00 AM'), ('2026-05-24', '12:00 PM'), ('2026-05-28', '9:00 AM'), ('2026-05-31', '3:00 PM'), ('2026-06-04', '10:00 AM'), ('2026-06-07', '12:00 PM'), ('2026-06-11', '9:00 AM'), ('2026-06-14', '3:00 PM')],
    'title':   'Koji Fermentation Workshop',
    'desc':    'Make two seasonal pantry staples using koji-fermented rice. At Maana Atelier, Kyoto.',
    'h1':      'Koji Fermentation<br/>Workshop.',
    'h1_jp': 'コウジ発酵<br/>ワークショップ。',
    'hero_eyebrow':'Maana Atelier · Workshop',
    'hero_eyebrow_jp': 'Maana アトリエ ・ ワークショップ',
    'lede':    'Make your own Japanese kitchen condiments from koji-fermented rice — the quiet engine of every umami flavour.',
    'lede_jp': '日本のうま味の源となる「麹」から、ご家庭で使える発酵調味料を仕込みます。',
    'duration':'1.5 hours',
    'duration_jp': '1時間30分', 'capacity':'Up to 8', 'capacity_jp': '最大8名', 'price':'¥18,000',
    'price_note':'Tax included',
    'price_note_jp': '税込',
    'venue':'Maana Atelier', 'venue_loc':'Nishijin, Kyoto', 'venue_loc_jp': '京都・西陣',
    'sessions_h2':'Koji Fermentation sessions.',
    'sessions_h2_jp': 'コウジ発酵ワークショップの日程。',
    'hero_bg':'images/hero.jpeg',
    'craft_word':'Kōji',  'craft_kanji':'発酵',
    'craft_p1':'Miso, shoyu, mirin, pickles — the staples of the Japanese table, all built on a single quiet foundation: <em>koji</em>, the national mould of Japan. Inoculated onto rice, barley, or soy, koji is the starter that turns ingredients into the fermented umami the islands are known for.',
    'craft_p1_jp': '味噌、醤油、味醂、漬物――日本の食卓を支える調味料はみな、ひとつの静かな存在に支えられています。それが<em>麹（こうじ）</em>、日本の「国菌」です。米や麦、大豆に種付けされる麹こそが、素材を日本ならではのうま味へと変えてくれる発酵の出発点です。',
    'craft_p2':'In this workshop, you\'ll learn the spectrum of fermentation styles across Japan and koji\'s vital role — then make two personalized condiments for your own pantry: shoyu-koji rich with dried fruit, and shio-koji with aromatic spices.',
    'craft_p2_jp': '本ワークショップでは、日本各地の発酵文化と麹の役割を学びながら、ご自分用の調味料を2瓶仕込んでいただきます。ドライフルーツの香る醤油麹、そして香辛料を効かせた塩麹。両方を持ち帰ってお楽しみください。',
    'craft_img':'images/001.jpg',
    'takehome_lede':'You leave with two jars of your own fermented condiments — ready to settle and finish on your kitchen counter at home.',
    'takehome_lede_jp': '醤油麹と塩麹を1瓶ずつ。ご自宅のキッチンで発酵を進めながら、味わいをじっくり熟成させてお楽しみください。',
    'fact1':('Two jars','Shoyu-koji + shio-koji, made with the koji of your choice and seasonal aromatics. Yours to keep.'),
    'fact2':('A few days to finish','Your jars are nearly there — they continue fermenting at home for 7–14 days, then keep in the fridge.'),
    'fact3':('Better cooking','One spoonful turns a bowl of rice, a piece of fish, or a dressing into something quietly transformed.'),
    'fact1_jp':('2つの瓶','醤油麹と塩麹を1瓶ずつ。お選びいただいた麹と季節の素材で仕込みます。'),
    'fact2_jp':('数日でできあがり','ご自宅で7〜14日ほどさらに発酵を進め、その後は冷蔵庫で保存してお使いください。'),
    'fact3_jp':('日々の料理に','ひとさじでご飯、魚、ドレッシング――いつもの一品が静かに変わります。'),
    'takehome_img':'images/take-home.jpg',
    'spend_steps':[
        ('i.','Welcome tea','A seasonal cup of tea on arrival, and an introduction to fermentation across Japan.','images/004.jpg'),
        ('ii.','Meet the koji','Smell and touch rice koji — the starter that drives miso, soy sauce, and saké. Taste a variety of koji-based seasonings.','images/005.jpg'),
        ('iii.','Mix','Combine koji with salt, soy sauce, dried fruit, or aromatics — your choice of shoyu-koji and shio-koji.','images/006.jpg'),
        ('iv.','Bottle','Spoon your blend into a jar to finish at home. Labelled, packed, ready to travel.','images/007.jpeg'),
    ],
    'spend_steps_jp':[
        ('i.','ウェルカムティー','到着後、季節のお茶を一杯。日本各地の発酵文化について簡単にご紹介します。',''),
        ('ii.','麹に出会う','米麹の香りと手触りを確かめます。味噌・醤油・酒の源となるその力に触れ、麹を使った調味料を少しずつ味わっていただきます。',''),
        ('iii.','仕込む','塩、醤油、ドライフルーツ、香辛料を麹と合わせていきます。醤油麹と塩麹をご自身で仕込んでいただきます。',''),
        ('iv.','瓶詰め','ブレンドを瓶に詰めて、ご自宅へ。ラベル付きで、旅の荷物にも収まる仕様です。',''),
    ],
    'partial':'atelier',
    'sessions_intro':'Koji Fermentation runs daily at four start times.',
    'sessions_intro_jp': 'コウジ発酵ワークショップは毎日4つの開始時間からお選びいただけます。',
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
    'faq_jp':[
      ('キャンセル規定について教えてください。', '開催日の7日前までは無料でキャンセルいただけます。それ以降は100%のキャンセル料を申し受けます。'),
      ('お子様の参加について教えてください。', '6歳以上のお子様はご参加いただけます（通常料金）。13歳未満のお子様は、保護者の方の同伴をお願いいたします。'),
      ('服装について教えてください。', '食材を扱いますので、汚れてもよい服装でお越しください。香水のご使用はお控えください。'),
      ('持ち物について教えてください。', '特にご用意いただくものはございません。材料・道具一式はこちらでご用意いたします。'),
      ('食物アレルギーには対応していますか。', 'はい、対応しております。ご予約時の事前フォームにて、アレルギーや食事制限を必ずお知らせください。'),
      ('バイリンガル対応はしていますか。', 'ワークショップは基本的に英語で進行いたします。必要に応じて日本語でもご説明いたします。'),
      ('貸切のワークショップに対応していますか。', 'ご希望の人数とご来訪日を添えて、atelier@maana.jpまでご連絡ください。'),
    ],
},
'morning-tea': {
    'wk_key':'morning',
    'show_img':'../_partials/images/showcase-tea-ceremony-morning.jpg',
    'sessions_data':[('2026-05-05', '8:30 AM'), ('2026-05-09', '8:30 AM'), ('2026-05-12', '8:30 AM'), ('2026-05-16', '8:30 AM'), ('2026-05-19', '8:30 AM'), ('2026-05-23', '8:30 AM'), ('2026-05-26', '8:30 AM'), ('2026-05-30', '8:30 AM'), ('2026-06-02', '8:30 AM'), ('2026-06-06', '8:30 AM'), ('2026-06-09', '8:30 AM'), ('2026-06-13', '8:30 AM')],
    'title':   'Morning Tea Ceremony & Breakfast',
    'desc':    'Asa-chaji at a private Kyoto tea house. Tea Master Eriko Okubo invites you to a Zen-monk breakfast and a morning tea ceremony.',
    'h1':      'Morning Tea Ceremony<br/>&amp; Breakfast.',
    'h1_jp': '朝の茶事<br/>＆ 朝食。',
    'hero_eyebrow':'Private Tea House · Excursion',
    'hero_eyebrow_jp': '貸切茶室 ・ 体験',
    'lede':    'Start the morning at a private tea house with a traditional tea ceremony and a Zen-monk\'s breakfast.',
    'lede_jp': '京都の貸切茶室にて、伝統の茶の湯と禅僧の朝食をご堪能ください。',
    'duration':'1.5 hours',
    'duration_jp': '1時間30分', 'capacity':'Up to 6', 'capacity_jp': '最大6名', 'price':'¥42,000',
    'price_note':'Tax included',
    'price_note_jp': '税込',
    'venue':'Hekishoken',
    'venue_jp': 'Hekishoken', 'venue_loc':'Private tea house, Kyoto', 'venue_loc_jp': '京都・貸切茶室',
    'sessions_h2':'Morning Tea Ceremony sessions.',
    'sessions_h2_jp': '朝の茶事の日程。',
    'spend_location':'a private tea house',
    'spend_bg':'images/atelier-2.jpg',
    'hero_bg':'images/hero.jpeg',
    'craft_word':'Asa-chaji',  'craft_kanji':'朝茶事',
    'craft_p1':'In this rare and intimate offering within the world of tea, Tea Master Eriko Okubo welcomes you to her private tea house, where the day begins with a quiet awakening of the senses.',
    'craft_p1_jp': '茶の湯の世界でも稀少で親密な「<em>朝茶事</em>」を、茶人・大久保恵理子がご自身の茶室にお招きいたします。一日が、感覚を静かに目覚めさせるところから始まります。',
    'craft_p2':'You start with a seasonal breakfast inspired by the mindful simplicity of Zen monastic cuisine. Then a tea ceremony — paired with <em>wagashi</em> — unfolds in the still atmosphere of the tea room. The seamless progression from breakfast to tea is known as <em>asa-chaji</em>, rarely experienced outside private circles.',
    'craft_p2_jp': 'まずは、禅寺の精進料理に倣った季節の朝食から。続いて、一服のお茶と<em>和菓子</em>とともに、茶室の静かな空気のなかで茶の湯が執り行われます。朝食からお茶へと続くこの一連の流れは<em>朝茶事</em>と呼ばれ、本来は限られた席でのみ味わうことのできる時間です。',
    'craft_img':'images/002.jpg',
    'takehome_lede':'<em>Mugon</em> 無言 — through the wordlessness of the tea ceremony, body, mind, and spirit align with the natural harmony of the morning.',
    'takehome_lede_jp': '<em>無言</em>――言葉のない茶の湯のなかで、身も心も、朝の自然な調和へと整えられていきます。',
    'fact1':('A still morning','1.5 hours that move at the pace of the tea, the breakfast, and the season outside the window.'),
    'fact2':('Authentic chanoyu','Conducted in the tradition of asa-chaji — rarely available outside invited circles.'),
    'fact3':('Hosted by Eriko Okubo','A Tea Master who has practiced tea ceremony for over 25 years. The ceremony is hers to lead.'),
    'fact1_jp':('静かな朝','1時間30分。お茶と朝食、そして窓の外の季節──そのすべての歩みに合わせて、ゆっくりと進みます。'),
    'fact2_jp':('正式な茶の湯','本来は招かれた者のみが体験できる「朝茶事」の作法に則って執り行われます。'),
    'fact3_jp':('亭主・大久保恵理子','茶の湯の修練を25年以上続ける茶人。本席は彼女が亭主を務めます。'),
    'takehome_img':'images/003.jpg',
    'spend_steps':[
        ('i.','Arrive','Step into the tea house. Remove shoes. The morning slows immediately.','images/004.jpg'),
        ('ii.','Zen breakfast','A seasonal meal in the spirit of monastic cuisine — simple, careful, beautiful.','images/005.jpg'),
        ('iii.','Wagashi · matcha','The ceremony unfolds. Thin tea, then thick. Each pause is part of the form.','images/006.jpg'),
        ('iv.','Mugon','Leave in silence, the morning still ahead of you.','images/007.jpg'),
    ],
    'spend_steps_jp':[
        ('i.','到着','茶室の暖簾をくぐり、靴を脱ぐ。その瞬間、朝の時間がゆっくりと流れ始めます。',''),
        ('ii.','精進朝食','禅僧の食事に倣った、季節の朝食を一品ずつ。慎ましく、丁寧に、美しく。',''),
        ('iii.','和菓子・抹茶','茶の湯が始まります。薄茶、続いて濃茶。間合いのひとつひとつが作法の一部です。',''),
        ('iv.','無言','言葉を交わさずに席を立ち、朝の時間をそのままお続けください。',''),
    ],
    'partial':'tea-house',
    'sessions_intro':'Please check our calendar for the latest schedule and note that booking closes 2 days prior to the event.',
    'sessions_intro_jp': '最新の日程はカレンダーをご確認ください。なお、ご予約は開催日の2日前までに承っております。',
    'session_times':['8:30 AM'],
    'faq':[
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the experience?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', 'We kindly ask you to bring socks and remove any accessories before entering the tea room — this protects the ceramics from damage. Please also refrain from wearing fragrances.'),
      ('Is the experience bilingual?', 'The tea ceremony will primarily be conducted in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the participants and the tranquility of wordless interaction. We invite you to experience the silent conversation by sensing the movements and the atmosphere.'),
      ('Do you accommodate private sessions?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
    'faq_jp':[
      ('キャンセル規定について教えてください。', '開催日の7日前までは無料でキャンセルいただけます。それ以降は100%のキャンセル料を申し受けます。'),
      ('お子様の参加について教えてください。', '6歳以上のお子様はご参加いただけます（通常料金）。13歳未満のお子様は、保護者の方の同伴をお願いいたします。'),
      ('服装について教えてください。', '茶室では靴下のご着用と、アクセサリーの取り外しをお願いしております（茶道具を傷つけないため）。香水のご使用もお控えください。'),
      ('バイリンガル対応はしていますか。', '茶の湯は主に日本語で進行し、必要に応じて英語でもご説明いたします。茶事の間は言葉を交わすことが少ないのが特徴です。所作と空気を感じる「無言の対話」をどうぞお楽しみください。'),
      ('貸切に対応していますか。', 'ご希望の人数とご来訪日を添えて、atelier@maana.jpまでご連絡ください。'),
    ],
},
'night-tea': {
    'wk_key':'night',
    'show_img':'../_partials/images/showcase-tea-ceremony-night.jpg',
    'sessions_data':[('2026-07-04', '6:00 PM'), ('2026-07-07', '6:00 PM'), ('2026-07-11', '6:00 PM'), ('2026-07-14', '6:00 PM'), ('2026-07-18', '6:00 PM'), ('2026-07-21', '6:00 PM'), ('2026-07-25', '6:00 PM'), ('2026-07-28', '6:00 PM'), ('2026-08-01', '6:00 PM'), ('2026-08-04', '6:00 PM'), ('2026-08-08', '6:00 PM'), ('2026-08-11', '6:00 PM')],
    'title':   'Night Tea Ceremony & Dinner',
    'desc':    'A summer evening at Hekishoken — tea ceremony by candlelight followed by a seasonal multi-course meal.',
    'h1':      'Night Tea Ceremony<br/>&amp; Dinner.',
    'h1_jp': '夜の茶事<br/>＆ 夕餉。',
    'hero_eyebrow':'Private Tea House · Excursion',
    'hero_eyebrow_jp': '貸切茶室 ・ 体験',
    'lede':    'Spend a summer evening at a private tea house with a candlelit tea ceremony and a seasonal meal.',
    'lede_jp': '京都の貸切茶室で過ごす夏の夕べ。ろうそくの灯りに包まれる茶の湯と、季節の懐石をご堪能ください。',
    'duration':'2 hours',
    'duration_jp': '2時間', 'capacity':'Up to 6', 'capacity_jp': '最大6名', 'price':'¥47,500',
    'price_note':'Tax included',
    'price_note_jp': '税込',
    'venue':'Hekishoken',
    'venue_jp': 'Hekishoken', 'venue_loc':'Private tea house, Kyoto', 'venue_loc_jp': '京都・貸切茶室',
    'sessions_h2':'Night Tea Ceremony sessions.',
    'sessions_h2_jp': '夜の茶事の日程。',
    'spend_location':'a private tea house',
    'spend_bg':'images/atelier-2.jpg',
    'hero_bg':'images/hero.jpeg',
    'craft_word':'Yoru-chaji',  'craft_kanji':'夜茶事',
    'craft_p1':'Tea Master Eriko Okubo invites you to a private tea house hidden in a quiet Kyoto neighbourhood. The night unfolds gently — beginning with a seasonal <em>shi-dashi</em> meal prepared in the tradition of tea, accompanied by selected Japanese saké.',
    'craft_p1_jp': '茶人・大久保恵理子が、京都の静かな町並みにある貸切の茶室にお招きいたします。夜の刻はゆっくりと進みます――まずは茶の湯の作法に則って仕立てられた、季節の<em>仕出し</em>料理と厳選された日本酒で。',
    'craft_p2':'After dinner, a tea ceremony is held by candlelight — <em>wagashi</em> and matcha, served as stillness descends. This sensory journey from meal to tea forms the <em>yoru-chaji</em>, an authentic evening ritual seldom available to the public.',
    'craft_p2_jp': 'お食事のあとは、ろうそくの灯りのもとで茶の湯が始まります。<em>和菓子</em>と抹茶を、静けさが満ちる一席で。料理から茶へと続くこの一連の流れは<em>夜茶事</em>と呼ばれ、本来一般には公開されない、夜の正式な茶事です。',
    'craft_img':'images/002.jpg',
    'takehome_lede':'<em>Yoin</em> 余韻 — in the quiet reflection of the tea ceremony, the impressions of the day settle within. We carry the lingering resonance.',
    'takehome_lede_jp': '<em>余韻</em>――茶の湯のあとの静かな佇まいのなかに、一日のひとときが内にゆっくりと残ります。',
    'fact1':('A summer evening','Two hours that move at candlelight pace — meal, ceremony, then the garden settling into dusk.'),
    'fact2':('Seasonal meal','A shi-dashi meal in the tradition of tea, paired with selected Japanese saké.'),
    'fact3':('Hosted by Eriko Okubo','A Tea Master leading the ceremony in her own tea house — intimate, by candlelight.'),
    'fact1_jp':('夏の夕べ','2時間。お食事、茶の湯、そして暮れゆく庭──ろうそくの灯りに合わせてゆっくりと進みます。'),
    'fact2_jp':('季節の懐石','茶の湯の伝統に倣った仕出し料理を、厳選された日本酒とともに。'),
    'fact3_jp':('亭主・大久保恵理子','茶人が自らの茶室でろうそくの灯りに包まれて点前を行う、親密なひととき。'),
    'takehome_img':'images/003.jpg',
    'spend_steps':[
        ('i.','Arrive at dusk','Step into the tea house as light fades. Remove shoes. The evening begins.','images/004.jpg'),
        ('ii.','Shi-dashi meal','A seasonal multi-course meal in the tradition of tea, with sake.','images/005.jpg'),
        ('iii.','Candlelit ceremony','Wagashi, then matcha. The ceremony unfolds as the room darkens.','images/006.jpg'),
        ('iv.','Yoin','Leave with the resonance of the evening still in you.','images/007.jpg'),
    ],
    'spend_steps_jp':[
        ('i.','夕暮れに到着','光が翳り始める頃、茶室へ。靴を脱ぎ、夜の刻が始まります。',''),
        ('ii.','仕出しの懐石','茶の湯の伝統に倣った、季節の多皿料理を日本酒とともに。',''),
        ('iii.','ろうそくの茶の湯','まずは和菓子、続いて抹茶。部屋が暮れていくなかで茶の湯が進みます。',''),
        ('iv.','余韻','夕暮れの余韻を心に残したまま、静かに席を立ちます。',''),
    ],
    'partial':'tea-house',
    'sessions_intro':'Held Tuesdays and Saturdays · July to September only. Booking closes 2 days prior.',
    'sessions_intro_jp': '火曜日・土曜日のみ開催 ・ 7月〜9月限定。ご予約は開催日の2日前までに承っております。',
    'session_times':['6:00 PM'],
    'summer_only': True,
    'faq':[
      ('What is the cancellation policy?', '0% cancellation fee if canceled more than 7 days in advance. 100% cancellation fee if canceled within 7 days in advance.'),
      ('What is your policy on children attending the experience?', 'Children aged 6 and older are welcome to join. They will be charged the standard fee. At least one adult must accompany children under 13 years old.'),
      ('What should I wear?', 'We kindly ask you to bring socks and remove any accessories before entering the tea room — this protects the ceramics from damage. Please also refrain from wearing fragrances.'),
      ('Is the experience bilingual?', 'The tea ceremony will primarily be conducted in Japanese, with some English. There is little verbal communication during the ceremony — the focus is on the participants and the tranquility of wordless interaction. We invite you to experience the silent conversation by sensing the movements and the atmosphere.'),
      ('Do you accommodate private sessions?', "Please contact atelier@maana.jp with the number of participants and the dates you'll be visiting."),
    ],
    'faq_jp':[
      ('キャンセル規定について教えてください。', '開催日の7日前までは無料でキャンセルいただけます。それ以降は100%のキャンセル料を申し受けます。'),
      ('お子様の参加について教えてください。', '本ワークショップでは日本酒をご提供するため、20歳以上の方にご参加いただいております。'),
      ('服装について教えてください。', '茶室では靴下のご着用と、アクセサリーの取り外しをお願いしております（茶道具を傷つけないため）。香水のご使用もお控えください。'),
      ('バイリンガル対応はしていますか。', '茶の湯は主に日本語で進行し、必要に応じて英語でもご説明いたします。茶事の間は言葉を交わすことが少ないのが特徴です。所作と空気を感じる「無言の対話」をどうぞお楽しみください。'),
      ('貸切に対応していますか。', 'ご希望の人数とご来訪日を添えて、atelier@maana.jpまでご連絡ください。'),
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

    # Hero — match by structural markers (hero-eyebrow div, then h1, then p.lede)
    html = re.sub(
        r'<div class="hero-eyebrow">\s*<span class="eyebrow">.*?</span>\s*</div>',
        f'<div class="hero-eyebrow">\n      <span class="eyebrow">{bi_data(data, "hero_eyebrow")}</span>\n    </div>',
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'<h1>.*?</h1>',
        f'<h1>{bi_data(data, "h1")}</h1>',
        html, count=1, flags=re.DOTALL
    )
    html = re.sub(
        r'<p class="lede">.*?</p>',
        f'<p class="lede">{bi_data(data, "lede")}</p>',
        html, count=1, flags=re.DOTALL
    )

    # Hero meta strip (4 cells)
    html = re.sub(
        r'<div class="hero-meta">.*?</div>\s*</div>\s*</section>',
        f'''<div class="hero-meta">
      <div><strong>{bi_data(data, "duration")}</strong>{bi("One session", "1回完結")}</div>
      <div><strong>{data["venue"]}</strong>{bi_data(data, "venue_loc")}</div>
      <div><strong>{bi_data(data, "capacity")}</strong>{bi("Per session", "1回あたり")}</div>
      <div><strong>{data["price"]}</strong>{bi_data(data, "price_note")}</div>
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

    # Spend-section background image — workshops without their own process.jpg
    # fall back to a shared image (atelier or tea-house).
    spend_bg = data.get('spend_bg', 'images/process.jpg')
    html = html.replace(
        "<div class=\"spend-bg\" style=\"background-image:url('images/process.jpg')\"",
        f"<div class=\"spend-bg\" style=\"background-image:url('{spend_bg}')\"",
        1
    )

    # Spend-section lede — swap duration + location per workshop.
    # Tea ceremony workshops use "a private tea house" instead of "the atelier".
    spend_location_en = data.get('spend_location', 'the atelier')
    spend_location_jp = data.get('spend_location_jp', 'アトリエ')
    dur_en = data['duration']
    dur_jp = data.get('duration_jp', dur_en)
    en_lede = f'A quiet {dur_en} at {spend_location_en} — guided, unhurried, made for arriving without a plan.'
    jp_lede = f'{spend_location_jp}で過ごす、静かな{dur_jp}。丁寧にご案内しますので、構えずにお越しください。'
    html = re.sub(
        r'<span class="lang-en">A quiet 2 hours at the atelier — guided, unhurried, made for arriving without a plan\.</span>\s*<span class="lang-jp">[^<]*</span>',
        f'<span class="lang-en">{en_lede}</span><span class="lang-jp">{jp_lede}</span>',
        html, count=1
    )

    # Craft section
    html = re.sub(
        r'<section class="craft reveal" aria-label="What is Tsuchikabe">.*?</section>',
        f'''<section class="craft reveal" aria-label="What is {data["craft_word"]}">
  <div class="container">
    <div class="craft-grid">
      <div class="craft-text">
        <span class="eyebrow">{bi("The craft", "工芸について")}</span>
        <h2><em>{data["craft_word"]}</em> <span class="kanji-accent">{data["craft_kanji"]}</span></h2>
        <p>{bi_data(data, "craft_p1")}</p>
        <p>{bi_data(data, "craft_p2")}</p>
      </div>
      <div class="craft-imgs">
        <div class="craft-img" style="background-image:url('{data["craft_img"]}')" role="img" aria-label="{data["craft_word"]}"></div>
      </div>
    </div>
  </div>
</section>''',
        html, count=1, flags=re.DOTALL
    )

    # Take home section
    def fact(i, key):
        en = data[key]
        jp = data.get(f'{key}_jp')
        if jp:
            title = bi(en[0], jp[0])
            body  = bi(en[1], jp[1])
        else:
            title, body = en[0], en[1]
        return f'''<li>
              <div class="fact-num">{i:02d}</div>
              <div class="fact-body">
                <h4>{title}</h4>
                <p>{body}</p>
              </div>
            </li>'''

    html = re.sub(
        r'<section class="takehome reveal" aria-label="What you\'ll take home">.*?</section>',
        f'''<section class="takehome reveal" aria-label="What you'll take home">
  <div class="container">
    <div class="takehome-head">
      <span class="eyebrow">{bi("Your keepsake", "持ち帰るもの")}</span>
      <h2 class="takehome-h2"><em>{bi("What you'll take home", "あなたが持ち帰るもの")}</em></h2>
    </div>
    <div class="takehome-grid">
      <div class="takehome-img" style="background-image:url('{data["takehome_img"]}')" role="img" aria-label="Take home"></div>
      <div class="takehome-text">
        <p class="takehome-lede">{bi_data(data, "takehome_lede")}</p>
        <ul class="takehome-facts">
          {fact(1, "fact1")}
          {fact(2, "fact2")}
          {fact(3, "fact3")}
        </ul>
      </div>
    </div>
  </div>
</section>''',
        html, count=1, flags=re.DOTALL
    )

    # Spend section steps (4 cards)
    def spend_card(i, step):
        en_title, en_body = step[1], step[2]
        jp_steps = data.get('spend_steps_jp')
        if jp_steps and i < len(jp_steps):
            jp_title, jp_body = jp_steps[i][1], jp_steps[i][2]
            title = bi(en_title, jp_title)
            body  = bi(en_body, jp_body)
        else:
            title, body = en_title, en_body
        return f'''      <article class="spend-card">
        <div class="spend-media">
          <div class="spend-img" style="background-image:url('{step[3]}')"></div>
        </div>
        <div class="spend-card-body">
          <div class="step">{step[0]}</div>
          <h3>{title}</h3>
          <p>{body}</p>
        </div>
      </article>'''
    cards = '\n'.join(spend_card(i, s) for i, s in enumerate(data['spend_steps']))

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

    # FAQ section — replace items (append the two shared FAQs at the end)
    full_faq = list(data['faq']) + SHARED_FAQ_TAIL
    jp_faq = None
    if data.get('faq_jp'):
        jp_faq = list(data['faq_jp']) + SHARED_FAQ_TAIL_JP
    def faq_html(i, qa):
        q, a = qa
        if jp_faq and i < len(jp_faq):
            q = bi(q, jp_faq[i][0])
            a = bi(a, jp_faq[i][1])
        return f'''<div class="faq-item">
        <button class="faq-q">{q}<span class="plus">+</span></button>
        <div class="faq-a">{a}</div>
      </div>'''
    faq_items = '\n      '.join(faq_html(i, qa) for i, qa in enumerate(full_faq))
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
    for img in ['atelier-2.jpg','kri.jpg','summer.jpg','summer.png',
                'showcase-tea-dye.jpg','showcase-botanical-tea.jpg',
                'showcase-koji-fermentation.jpg','showcase-earthen-wall.jpg',
                'showcase-tea-ceremony-morning.jpg','showcase-tea-ceremony-night.jpg']:
        html = html.replace(f"images/{img}", f"../_partials/images/{img}")
    # Guest panels (1-12)
    for i in range(1,13):
        html = html.replace(f"images/guest{i}.jpg", f"../_partials/images/guest{i}.jpg")

    # Sessions h2 + optional intro paragraph below the heading
    if 'sessions_h2' in data:
        intro_en = data.get('sessions_intro', '')
        intro_jp = data.get('sessions_intro_jp')
        intro_bi = bi(intro_en, intro_jp) if intro_en else ''
        intro_html = f'\n        <p class="sessions-intro">{intro_bi}</p>' if intro_en else ''
        html = html.replace(
            '<h2>Earthen Wall sessions.</h2>',
            f'<h2>{bi_data(data, "sessions_h2")}</h2>{intro_html}'
        )


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


    # If this workshop has extras_cards (e.g. koji recipes), insert a new section
    # just before the Guest Voices section.
    if 'extras_cards' in data:
        eyebrow_label, head_title = data['extras_intro']
        def _card(c):
            ing_html = '\n        '.join(f'<li>{i}</li>' for i in c['ingredients'])
            img_pos = c.get('img_pos', 'center')
            return f"""<article class="extra-card">
        <div class="extra-card__media"><div class="extra-card__img" style="background-image:url('{c['img']}');background-position:{img_pos}"></div></div>
        <div class="extra-card__body">
          <h3 class="extra-card__title">{c['title']}</h3>
          <ul class="extra-card__ingredients">
        {ing_html}
          </ul>
          <p class="extra-card__note">{c['note']}</p>
        </div>
      </article>"""
        cards_html = '\n'.join(_card(c) for c in data['extras_cards'])
        extras_block = f"""<!-- ========== EXTRAS (workshop-specific) ========== -->
<section class="extras reveal" id="extras">
  <div class="container">
    <div class="extras__head">
      <span class="eyebrow">{eyebrow_label}</span>
      <h2><em>{head_title.split(' — ')[0] if ' — ' in head_title else 'In your kitchen'}</em></h2>
      <p>{head_title}</p>
    </div>
    <div class="extras__grid">
      {cards_html}
    </div>
  </div>
</section>

"""
        html = re.sub(
            r'(<!-- ========== GUEST VOICES)',
            extras_block + r'\1',
            html, count=1
        )

    # Guest gallery handling — per workshop count
    # gallery_count = 0 (or strip_voices_gallery)  -> remove the gallery entirely
    # gallery_count = N                            -> rebuild the marquee with N items
    gallery_count = data.get('gallery_count', 0)
    if gallery_count == 0 or data.get('strip_voices_gallery'):
        html = re.sub(
            r'<div class="gallery-head">.*?<div class="gallery-marquee".*?</div>\s*</div>\s*</div>',
            '',
            html, count=1, flags=re.DOTALL
        )
    else:
        items = '\n        '.join(
            f'<div class="gallery-item"><img src="images/guest{i}.jpg" alt="Guest panel {i}" loading="lazy"/></div>'
            for i in range(1, gallery_count + 1)
        )
        items_dup = '\n        '.join(
            f'<div class="gallery-item" aria-hidden="true"><img src="images/guest{i}.jpg" alt="" loading="lazy"/></div>'
            for i in range(1, gallery_count + 1)
        )
        new_track = (
            f'<div class="gallery-track" id="gallery-track">\n'
            f'        {items}\n'
            f'        <!-- duplicate set for seamless loop, hidden from screen readers -->\n'
            f'        {items_dup}\n'
            f'      </div>'
        )
        html = re.sub(
            r'<div class="gallery-track" id="gallery-track">.*?</div>\s*(?=</div>\s*</div>\s*</section>)',
            new_track + '\n    ',
            html, count=1, flags=re.DOTALL
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
