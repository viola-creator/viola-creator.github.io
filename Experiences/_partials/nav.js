/* Site nav: darken on scroll, language toggle (EN/JA) with localStorage. */
(function () {
  const LANG_KEY = 'maana-lang';

  function setLang(lang) {
    document.documentElement.setAttribute('lang', lang);
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* ignore */ }
  }

  function currentLang() {
    try {
      return localStorage.getItem(LANG_KEY) || 'en';
    } catch (e) { return 'en'; }
  }

  // Apply stored language on first paint (before partials, so static
  // content already in the DOM swaps without flicker).
  setLang(currentLang());

  function wireNav() {
    const nav = document.getElementById('site-nav');
    if (!nav) return;

    // Pages without a dark hero (like the hub) keep the nav darkened
    // permanently — light cream backgrounds need the contrast.
    const hasHero = document.querySelector('section.hero');
    if (!hasHero) {
      nav.classList.add('is-scrolled');
    } else {
      const onScroll = () => {
        if (window.scrollY > 40) nav.classList.add('is-scrolled');
        else nav.classList.remove('is-scrolled');
      };
      onScroll();
      window.addEventListener('scroll', onScroll, { passive: true });
    }

    // Language toggle
    const btn = document.getElementById('lang-toggle');
    if (btn) {
      btn.addEventListener('click', () => {
        const next = currentLang() === 'ja' ? 'en' : 'ja';
        setLang(next);
      });
    }
  }

  // Wait for partials (which include the nav) to load.
  if (document.querySelector('#site-nav')) wireNav();
  document.addEventListener('partials-loaded', wireNav);
})();
