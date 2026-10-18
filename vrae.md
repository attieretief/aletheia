---
layout: course
course_name: vrae
title: "Goeie Vrae"
title_en: "Good Questions"
description: "Die vrae wat jy op kampus, aanlyn en by die braai hoor, kort en eerlik beantwoord, met 'n pad na die dieper gesprek."
description_en: "The questions you hear on campus, online and round the braai, answered briefly and honestly, with a way into the deeper conversation."
order: -1
---
<div class="lang-af" markdown="1">

# Goeie Vrae

Iemand sê iets in die klas, of onder 'n video, of by die braai, en skielik weet jy nie wat om te sê nie. Dit gebeur met almal.

'n Vraag is nie 'n aanval nie. Die meeste van hierdie vrae is goeie vrae, en die geloof is oud genoeg om hulle al baie keer gehoor te hê. Hier is kort, eerlike antwoorde. Elkeen neem vyf minute om te lees, en elkeen wys jou waar om verder te lees as jy wil.

</div>

<div class="lang-en" markdown="1">

# Good Questions

Someone says something in class, or under a video, or round the braai, and suddenly you don't know what to say. It happens to everyone.

A question is not an attack. Most of these are good questions, and the faith is old enough to have heard them many times. Here are short, honest answers. Each takes five minutes to read, and each shows you where to go further if you want to.

</div>

{% assign vrae = site.pages | where: "course", "vrae" | where_exp: "item", "item.lesson != nil" | sort: "lesson" %}
{% assign temas = vrae | map: "tema" | uniq %}

<div class="vrae-filter" role="group" aria-label="Tema">
  <button type="button" class="vrae-chip is-active" data-tema="alles"><span class="lang-af">Alles</span><span class="lang-en">All</span></button>
  {% for t in temas %}{% assign tp = vrae | where: "tema", t | first %}<button type="button" class="vrae-chip" data-tema="{{ t }}"><span class="lang-af">{{ t }}</span><span class="lang-en">{{ tp.tema_en }}</span></button>{% endfor %}
</div>

{% for t in temas %}{% assign tp = vrae | where: "tema", t | first %}{% assign groep = vrae | where: "tema", t %}
<section class="vrae-groep" data-tema="{{ t }}">
<h2 class="vrae-groep-kop"><span class="lang-af">{{ t }}</span><span class="lang-en">{{ tp.tema_en }}</span></h2>
<div class="vrae-grid">
{% for v in groep %}
  <a class="vraag-kaart" href="{{ v.url | prepend: site.baseurl }}">
    <span class="vraag-teks"><span class="lang-af">“{{ v.vraag }}”</span><span class="lang-en">“{{ v.vraag_en }}”</span></span>
    <span class="vraag-antwoord"><span class="lang-af">{{ v.title }}</span><span class="lang-en">{{ v.title_en }}</span> →</span>
  </a>
{% endfor %}
</div>
</section>
{% endfor %}

<style>
.vrae-filter { display:flex; flex-wrap:wrap; gap:8px; margin:1.5rem 0 1rem; }
.vrae-chip { font:inherit; font-size:.9rem; padding:6px 14px; border-radius:999px; border:1.5px solid #b08d57; background:none; color:#7a5c2e; cursor:pointer; }
.vrae-chip.is-active { background:#b08d57; color:#fff; }
.vrae-grid { display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:16px; margin-bottom:2rem; }
.vraag-kaart { display:flex; flex-direction:column; gap:10px; padding:18px; border:1px solid #e5e0d8; border-radius:10px; text-decoration:none; color:inherit; background:#fffdf9; transition:transform .15s, box-shadow .15s; }
.vraag-kaart:hover { transform:translateY(-2px); box-shadow:0 6px 18px rgba(122,92,46,.12); text-decoration:none; }
.vraag-teks { font-size:1.2rem; line-height:1.35; font-weight:600; }
.vraag-antwoord { font-size:.95rem; color:#7a5c2e; margin-top:auto; }
.vrae-groep[hidden] { display:none; }
.vrae-groep-kop { font-size:.85rem; letter-spacing:.08em; text-transform:uppercase; color:#b08d57; margin:1.5rem 0 .75rem; border:none; }
</style>

<script>
(function () {
  var chips = document.querySelectorAll('.vrae-chip');
  var groups = document.querySelectorAll('.vrae-groep');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var t = chip.getAttribute('data-tema');
      chips.forEach(function (c) { c.classList.toggle('is-active', c === chip); });
      groups.forEach(function (g) { g.hidden = t !== 'alles' && g.getAttribute('data-tema') !== t; });
    });
  });
})();
</script>
