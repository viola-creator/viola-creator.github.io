/* Mobile primary navigation. Desktop menus retain their existing behavior. */
(() => {
  const mobile = matchMedia('(max-width: 800px)');
  function initialize() {
    document.querySelectorAll('.site-nav').forEach((nav, index) => {
      if (nav.dataset.mobileMenuReady) return;
      const links = nav.querySelector('.site-nav__links');
      if (!links) return;
      nav.dataset.mobileMenuReady = 'true';
      nav.classList.add('site-nav--mobile-ready');
      links.id ||= 'primary-menu-' + index;
      const toggle = document.createElement('button');
      toggle.type = 'button';
      toggle.className = 'site-nav__menu-toggle';
      toggle.setAttribute('aria-controls', links.id);
      toggle.setAttribute('aria-expanded', 'false');
      toggle.setAttribute('aria-label', 'Open menu');
      toggle.innerHTML = '<span></span><span></span><span></span>';
      nav.insertBefore(toggle, links);
      function close(returnFocus = false) {
        nav.classList.remove('is-menu-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open menu');
        nav.querySelectorAll('.site-nav__item.is-open').forEach(item => {
          item.classList.remove('is-open');
          item.querySelector('.site-nav__link')?.setAttribute('aria-expanded', 'false');
        });
        if (returnFocus) toggle.focus();
      }
      toggle.addEventListener('click', () => {
        const open = !nav.classList.contains('is-menu-open');
        if (!open) return close();
        nav.classList.add('is-menu-open');
        toggle.setAttribute('aria-expanded', 'true');
        toggle.setAttribute('aria-label', 'Close menu');
      });
      // Capture mobile submenu taps before the older inline dropdown handlers.
      nav.addEventListener('click', event => {
        if (!mobile.matches) return;
        const trigger = event.target.closest('.site-nav__item.has-dropdown > .site-nav__link');
        if (trigger) {
          event.preventDefault();
          event.stopImmediatePropagation();
          const item = trigger.parentElement;
          const open = item.classList.toggle('is-open');
          trigger.setAttribute('aria-expanded', String(open));
          return;
        }
        if (event.target.closest('a')) close();
      }, true);
      nav.querySelectorAll('.site-nav__item.has-dropdown').forEach(item => {
        const parent = item.querySelector('.site-nav__link');
        const dropdown = item.querySelector('.site-nav__dropdown');
        if (!parent || !dropdown) return;
        const overview = document.createElement('a');
        overview.href = parent.href;
        overview.className = 'site-nav__overview';
        overview.textContent = item.dataset.nav === 'stay' ? 'All properties' : 'All experiences';
        dropdown.prepend(overview);
      });
      document.addEventListener('click', event => {
        if (!nav.contains(event.target)) close();
      });
      document.addEventListener('keydown', event => {
        if (event.key === 'Escape' && nav.classList.contains('is-menu-open')) close(true);
      });
      nav.addEventListener('focusout', () => {
        setTimeout(() => { if (!nav.contains(document.activeElement)) close(); }, 0);
      });
      mobile.addEventListener('change', () => close());
    });
  }
  initialize();
  document.addEventListener('partials-loaded', initialize);
})();
