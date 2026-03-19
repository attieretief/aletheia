// Language toggle: switches between Afrikaans (default) and English
(function () {
  var STORAGE_KEY = 'aletheia-lang';

  function applyLang(lang) {
    var html = document.documentElement;
    if (lang === 'en') {
      html.classList.add('lang-en');
      html.setAttribute('lang', 'en');
    } else {
      html.classList.remove('lang-en');
      html.setAttribute('lang', 'af');
    }
  }

  function toggleLang() {
    var isEn = document.documentElement.classList.contains('lang-en');
    var newLang = isEn ? 'af' : 'en';
    localStorage.setItem(STORAGE_KEY, newLang);
    applyLang(newLang);
  }

  // Apply saved preference immediately (before DOMContentLoaded to avoid flash)
  var saved = localStorage.getItem(STORAGE_KEY);
  if (saved) {
    applyLang(saved);
  }

  // Expose toggle globally for the button
  window.toggleLang = toggleLang;
})();
