/**
 * deck-stage.js: Hub201 Workshop Deck Navigation
 *
 * Responsibilities:
 *  (a) Scale-on-load and resize: measures viewport, computes --deck-scale and --deck-w,
 *      sets them on :root so every .slide-frame + its 1920x1080 .slide renders correctly.
 *  (b) Keyboard navigation: Arrow keys, Page keys, Space, J/K, Home, End.
 *  (c) Slide counter: live "N / 45" text in the .deck-nav bar and in each .slide-counter.
 *  (d) Scroll-position tracking via IntersectionObserver: syncs current index with scroll.
 *  (e) Fullscreen toggle: F key.
 *  (f) Light/dark mode toggle: L key. Persists to localStorage. Adds .light-mode to body.
 *  (g) Print-friendly: beforeprint fires a layout adjustment so slides render at natural size.
 *
 * Pattern follows physact-fundraising/deck.html with additions.
 */

(function () {

  /* ─── Constants ─── */
  var DESIGN_W = 1920;
  var PADDING = 56;          /* horizontal gutter around slides */
  var MAX_W_FRACTION = 1;    /* allow full viewport width */
  var SCROLL_LOCK_MS = 900;  /* ignore scroll events while programmatic scroll settles */
  var STORAGE_KEY = 'hub201-w3-deck:slide';
  var LS_MODE_KEY = 'hub201-w3-deck:mode';

  /* ─── State ─── */
  var current = 0;
  var scrollingUntil = 0;

  /* ─── Helpers ─── */
  function frames() {
    return Array.prototype.slice.call(document.querySelectorAll('.slide-frame'));
  }

  function navEl() {
    return document.getElementById('deck-nav');
  }

  /* ─── Scale computation ─── */
  function updateScale() {
    var available = Math.max(320, window.innerWidth - PADDING);
    var scale = Math.min(MAX_W_FRACTION, available / DESIGN_W);
    var w = DESIGN_W * scale;
    document.documentElement.style.setProperty('--deck-scale', scale.toFixed(4));
    document.documentElement.style.setProperty('--deck-w', w.toFixed(1) + 'px');
  }

  /* ─── Slide marking ─── */
  function mark() {
    var all = frames();
    var total = all.length;

    all.forEach(function (f, i) {
      f.classList.toggle('is-current', i === current);
    });

    /* Update the fixed nav bar */
    var nav = navEl();
    if (nav) {
      nav.textContent = (current + 1) + ' / ' + total;
    }

    /* Update per-slide counters */
    all.forEach(function (f, i) {
      var counter = f.querySelector('.slide-counter');
      if (counter) {
        counter.textContent = (i + 1) + ' / ' + total;
      }
    });

    /* Persist */
    try { localStorage.setItem(STORAGE_KEY, current); } catch (e) { /* ignore */ }
  }

  /* ─── Navigation ─── */
  function goTo(i, behavior) {
    var all = frames();
    if (!all.length) return;
    var clamped = Math.max(0, Math.min(all.length - 1, i));
    if (clamped === current && behavior !== 'instant') return;
    current = clamped;
    scrollingUntil = Date.now() + SCROLL_LOCK_MS;

    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var scrollBehavior = (behavior === 'instant' || prefersReduced) ? 'instant' : 'smooth';

    all[current].scrollIntoView({ behavior: scrollBehavior, block: 'start' });
    mark();
  }

  /* ─── Keyboard navigation ─── */
  function handleKeydown(e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var tag = e.target && e.target.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

    switch (e.key) {
      case 'ArrowRight':
      case 'ArrowDown':
      case 'PageDown':
      case ' ':
      case 'j':
      case 'J':
        e.preventDefault();
        goTo(current + 1);
        break;

      case 'ArrowLeft':
      case 'ArrowUp':
      case 'PageUp':
      case 'k':
      case 'K':
        e.preventDefault();
        goTo(current - 1);
        break;

      case 'Home':
        e.preventDefault();
        goTo(0);
        break;

      case 'End':
        e.preventDefault();
        goTo(frames().length - 1);
        break;

      /* Fullscreen */
      case 'f':
      case 'F':
        e.preventDefault();
        toggleFullscreen();
        break;

      /* Light / dark mode */
      case 'l':
      case 'L':
        e.preventDefault();
        toggleLightMode();
        break;
    }
  }

  /* ─── Fullscreen ─── */
  function toggleFullscreen() {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(function () { /* ignore */ });
    } else {
      if (document.exitFullscreen) {
        document.exitFullscreen().catch(function () { /* ignore */ });
      }
    }
  }

  /* ─── Light mode ─── */
  function applyMode(light) {
    if (light) {
      document.body.classList.add('light-mode');
    } else {
      document.body.classList.remove('light-mode');
    }
  }

  function toggleLightMode() {
    var isLight = document.body.classList.contains('light-mode');
    var next = !isLight;
    applyMode(next);
    try { localStorage.setItem(LS_MODE_KEY, next ? 'light' : 'dark'); } catch (e) { /* ignore */ }
  }

  /* ─── IntersectionObserver for scroll tracking ─── */
  function setupObserver() {
    if (!window.IntersectionObserver) return;

    var io = new IntersectionObserver(function (entries) {
      if (Date.now() < scrollingUntil) return;
      entries.forEach(function (entry) {
        if (entry.isIntersecting && entry.intersectionRatio > 0.5) {
          var all = frames();
          var i = all.indexOf(entry.target);
          if (i >= 0 && i !== current) {
            current = i;
            mark();
          }
        }
      });
    }, { threshold: [0, 0.5, 1] });

    frames().forEach(function (f) { io.observe(f); });
  }

  /* ─── Print ─── */
  function handleBeforePrint() {
    /* Reset scale so slides print at 1920px natural size.
       Browser will shrink them to fit the page automatically. */
    document.documentElement.style.setProperty('--deck-scale', '1');
    document.documentElement.style.setProperty('--deck-w', '1920px');
  }

  function handleAfterPrint() {
    updateScale();
  }

  /* ─── Restore persisted state ─── */
  function restoreState() {
    try {
      var savedMode = localStorage.getItem(LS_MODE_KEY);
      if (savedMode === 'light') applyMode(true);

      var savedSlide = parseInt(localStorage.getItem(STORAGE_KEY), 10);
      if (!isNaN(savedSlide) && savedSlide > 0) {
        goTo(savedSlide, 'instant');
        return;
      }
    } catch (e) { /* ignore */ }
  }

  /* ─── Init ─── */
  function init() {
    updateScale();
    restoreState();
    setupObserver();
    mark();

    window.addEventListener('resize', updateScale);
    document.addEventListener('keydown', handleKeydown);
    window.addEventListener('beforeprint', handleBeforePrint);
    window.addEventListener('afterprint', handleAfterPrint);
  }

  /* Run on DOMContentLoaded (guaranteed since this script is at end of body) */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
