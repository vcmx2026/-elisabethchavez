# Builds the multi-page elisabethchavez.com from the one-page draft (fuente/borrador.html):
# shared css/site.css + js/site.js, and one page per section, with a curated home page.
import re, os, shutil
S = os.path.dirname(os.path.abspath(__file__)) + '/'
src = open(S + 'borrador.html', encoding='utf-8').read()
OUT = os.path.normpath(S + '../public') + '/'

def section(sid):
    m = re.search(r'<section id="%s"[^>]*>\s*<div class="wrap[^"]*">(.*?)</div>\s*</section>' % sid, src, re.S)
    assert m, sid
    return m.group(1)

def between(a, b, s=src):
    i = s.index(a); j = s.index(b, i)
    return s[i:j]

# ---------- css ----------
css = open(S + 'base.css', encoding='utf-8').read()
css += r'''
/* ===== multi-page layout ===== */
.skip{position:absolute;left:-9999px;top:8px;z-index:50;background:var(--ink);color:#fff;padding:10px 16px;border-radius:999px}
.skip:focus{left:16px}
footer a{color:var(--muted)}
main{animation:rise .6s cubic-bezier(.2,.7,.2,1) both}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){main{animation:none}html{scroll-behavior:auto}}
nav a[aria-current="page"]{background:var(--sand)}
nav a.nav-cta{border:1.5px solid var(--terra);color:var(--terra);font-weight:700}
nav a.nav-cta[aria-current="page"]{background:var(--terra);color:#fff}
.brand{text-decoration:none}
.page-head{padding:76px 0 8px}
.page-head h1{font-size:clamp(44px,6.4vw,76px);letter-spacing:-.01em;margin-bottom:16px}
.page-head .lede{font-size:19px}
.page-body{padding:48px 0 96px}
.rule{height:1px;background:var(--line);border:0;margin:0}
.more{display:inline-flex;align-items:center;gap:8px;font-weight:700;text-decoration:none;color:var(--terra);border-bottom:1.5px solid transparent;padding-bottom:2px}
.more:hover{border-color:var(--terra)}
.more::after{content:"→";transition:transform .2s}
.more:hover::after{transform:translateX(3px)}

/* home */
.home-hero{padding:64px 0 72px;background:radial-gradient(60% 70% at 85% 30%,rgba(232,216,196,.85),rgba(245,239,231,0) 70%)}
.home-hero .wrap{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:64px;align-items:center}
.home-hero .sub{font-size:20px;color:var(--muted);max-width:540px;margin:22px 0 32px}
.home-hero .ctas{display:flex;flex-wrap:wrap;gap:10px}
.home-hero figure{margin:0;position:relative}
.home-hero figure img{width:100%;height:auto;border-radius:4px;box-shadow:0 30px 60px -40px rgba(31,44,61,.6)}
.firma img{width:100%;max-width:600px;height:auto;margin-left:-8px}
.nextbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px 22px;padding:18px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);background:var(--card)}
.nextbar .wrap{display:flex;flex-wrap:wrap;align-items:center;gap:10px 22px;width:100%}
.nextbar .lbl{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--blue)}
.nextbar .what{font-family:var(--serif);font-size:22px;font-weight:600}
.nextbar .what small{font-family:var(--sans);font-size:15px;font-weight:400;color:var(--muted);margin-left:6px}
.nextbar .more{margin-left:auto}
.shelf{padding:96px 0}
.shelf-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:16px;margin-bottom:40px}
.shelf-head h2{margin:0}
.shelf-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:48px}
.shelf-grid a{text-decoration:none;color:var(--ink);display:flex;flex-direction:column;gap:14px}
.shelf-grid img{width:100%;height:auto;aspect-ratio:2/3;object-fit:cover;border-radius:4px 10px 10px 4px;box-shadow:inset 6px 0 0 rgba(0,0,0,.12),0 26px 40px -30px rgba(31,44,61,.7);transition:transform .35s ease,box-shadow .35s ease}
.shelf-grid a:hover img{transform:translateY(-6px);box-shadow:0 34px 50px -30px rgba(31,44,61,.7)}
.shelf-grid b{font-family:var(--serif);font-size:24px;font-weight:600;line-height:1.15}
.shelf-grid span{font-size:14px;color:var(--muted)}
.quote{background:var(--slate);color:#F3EFE6;padding:96px 0;text-align:center}
.quote p{font-family:var(--serif);font-style:italic;font-size:clamp(26px,3.4vw,40px);line-height:1.3;max-width:860px;margin:0 auto}
.quote span{display:block;margin-top:22px;font-size:12px;font-weight:700;letter-spacing:.2em;text-transform:uppercase;color:var(--cream)}
.tiles{padding:96px 0}
.tiles .wrap{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.tile{background:var(--card);border:1px solid var(--line);border-radius:24px;padding:36px;display:flex;flex-direction:column;gap:14px;text-decoration:none;color:var(--ink);transition:transform .3s ease,box-shadow .3s ease}
.tile:hover{transform:translateY(-4px);box-shadow:0 26px 40px -32px rgba(31,44,61,.55)}
.tile h3{font-size:34px}
.tile p{margin:0;color:var(--muted)}
.tile .more{margin-top:auto}
@media (max-width:880px){
  .home-hero .wrap{grid-template-columns:1fr;gap:40px}
  .home-hero figure{max-width:420px}
  .shelf-grid{grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
  .shelf-grid b{font-size:17px}.shelf-grid span{display:none}
  .tiles .wrap{grid-template-columns:1fr}
  .nextbar .more{margin-left:0}
}

/* home intro (first person) */
.intro{padding:96px 0 24px}
.intro .wrap{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:64px;align-items:start}
.intro-side{position:sticky;top:110px}
.intro-side h2{font-size:clamp(34px,4vw,48px)}
.themes-label{margin:28px 0 10px;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.themes{display:flex;flex-wrap:wrap;gap:8px}
.themes span{font-family:var(--serif);font-size:19px;font-weight:600;padding:6px 14px;border-radius:999px;border:1px solid var(--line);background:var(--card)}
.intro-text p{margin:0 0 20px;font-size:18px;line-height:1.75;color:var(--ink)}
.intro-text p.lead{font-family:var(--serif);font-size:clamp(24px,2.4vw,30px);line-height:1.4}
.intro-text .ctas{display:flex;flex-wrap:wrap;gap:10px;margin-top:30px}
@media (max-width:880px){.intro .wrap{grid-template-columns:1fr;gap:28px}.intro-side{position:static}.intro{padding:72px 0 8px}}
/* featured next presentation (home + agenda) */
.featured{padding:72px 0 8px}
.feat{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:56px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:28px;padding:32px}
.feat img{width:100%;height:auto;border-radius:14px;box-shadow:0 30px 50px -36px rgba(31,44,61,.7)}
.feat h2{font-size:clamp(34px,4.2vw,52px);margin:2px 0 18px}
.feat dl{margin:0 0 26px;border-top:1px solid var(--line)}
.feat dl div{display:grid;grid-template-columns:110px minmax(0,1fr);gap:16px;padding:12px 0;border-bottom:1px solid var(--line)}
.feat dt{font-size:12px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);padding-top:3px}
.feat dd{margin:0;font-family:var(--serif);font-size:21px;font-weight:600;line-height:1.3}
.feat .ctas{display:flex;flex-wrap:wrap;gap:10px}
.feature-agenda{margin:0 0 36px}
.agenda-page .feat{background:rgba(255,255,255,.06);border-color:rgba(255,255,255,.16)}
.agenda-page .feat .eyebrow,.agenda-page .feat dt{color:var(--cream)}
.agenda-page .feat dl,.agenda-page .feat dl div{border-color:rgba(255,255,255,.16)}
.agenda-page .feat .btn.ghost{color:#F3EFE6;border-color:rgba(255,255,255,.5)}
@media (max-width:880px){.feat{grid-template-columns:1fr;gap:28px;padding:20px}.feat img{max-width:420px}.feat dl div{grid-template-columns:90px minmax(0,1fr)}}

/* books page: editorial rows */
.books.rows{display:flex;flex-direction:column;gap:0;margin-top:0}
.books.rows .book{display:grid;grid-template-columns:minmax(0,300px) minmax(0,1fr);column-gap:64px;row-gap:12px;align-content:start;padding:64px 0;border-top:1px solid var(--line)}
.books.rows .book:first-child{border-top:0;padding-top:24px}
.books.rows .book > .cover{grid-column:1;grid-row:1 / span 8;align-self:start}
.books.rows .book > *:not(.cover){grid-column:2}
.books.rows .book .t{font-size:clamp(32px,3.6vw,44px);line-height:1.05}
.books.rows .book .meta{font-size:16.5px;line-height:1.7;max-width:620px}
.books.rows .book .actions{margin-top:10px}
.books.rows .book .actions .lbl{margin-top:8px}
@media (max-width:760px){
  .books.rows .book{grid-template-columns:1fr;padding:48px 0}
  .books.rows .book > .cover{grid-row:auto;max-width:240px}
  .books.rows .book > *:not(.cover){grid-column:1}
}
.stores-band{background:var(--card);border-top:1px solid var(--line);padding:64px 0}

/* author page */
.about .wrap{padding-top:0}
details.reveal{margin-top:28px;border-top:1px solid var(--line);padding-top:22px}
details.reveal summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:10px;font-family:var(--serif);font-size:26px;font-weight:600}
details.reveal summary::-webkit-details-marker{display:none}
details.reveal summary::after{content:"+";font-family:var(--sans);font-size:22px;color:var(--blue);transition:transform .25s}
details.reveal[open] summary::after{transform:rotate(45deg)}
details.reveal > div{padding-top:18px}
.bio-sub{display:none}

/* agenda page */
.agenda-page{background:radial-gradient(55% 60% at 88% 10%,rgba(232,216,196,.22),rgba(58,60,64,0) 70%),var(--slate);color:#F3EFE6}
.agenda-page .page-head .eyebrow{color:var(--cream)}
.agenda-page .lede{color:#D9E0D9}
.agenda-page details.reveal{border-color:rgba(255,255,255,.2)}
.agenda-page details.reveal summary{color:#F3EFE6}
.agenda-page .past-title{margin-top:56px}
'''
os.makedirs(OUT + 'css', exist_ok=True); os.makedirs(OUT + 'js', exist_ok=True)
import sys; sys.path.insert(0, S)
from map_part import CSS as _MAPCSS
css += _MAPCSS
from why_part import CSS as _WHYCSS, WHY as _WHY
css += _WHYCSS
from synopsis_part import CSS as _SYNCSS
css += _SYNCSS
from prensa_part import CSS as _PRCSS
css += _PRCSS
open(OUT + 'css/site.css', 'w', encoding='utf-8').write(css)

# ---------- js ----------
js = r'''(function(){
  var KEY='ec-lang', lang='es';
  try{ lang=new URLSearchParams(location.search).get('l')||localStorage.getItem(KEY)||((navigator.language||'').slice(0,2)==='en'?'en':'es'); }catch(e){}
  function $(id){return document.getElementById(id);}
  var MES=['Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'], MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];

  // 2026 literary calendar: [date, place, Spanish detail, English detail]
  var EVENTS=[
    ['2026-04-08','Plaza Amigos · Todos Santos, B.C.S.','Presentación de Las hijas de El Camalote','Presentation of Las hijas de El Camalote'],
    ['2026-06-26','Museo Universitario de Artes Populares','Presentación de Las hijas de El Camalote · 18:00 h','Presentation of Las hijas de El Camalote · 6 pm'],
    ['2026-08-16','FILIP · Puebla','Presentación de Las hijas de El Camalote · 11:00 h · Auditorio Palafox','Presentation of Las hijas de El Camalote · 11 am · Palafox Auditorium'],
    ['2026-09-11','FENALEM 2026 · Querétaro','Presentación de Las hijas de El Camalote · viernes · Amazcala','Presentation of Las hijas de El Camalote · Friday · Amazcala'],
    ['2026-12-04','FIL Guadalajara','Presentación de Las hijas de El Camalote · 19:30 h · EMXI Lecturas, Stand M10','Presentation of Las hijas de El Camalote · 7:30 pm · EMXI Lecturas, Booth M10',
     {poster:'img/fil-guadalajara-2026.jpg', w:900, h:1118, alt:'Cartel de la presentación de Las hijas de El Camalote en la FIL Guadalajara 2026',
      title:'FIL Guadalajara 2026', title_en:'FIL Guadalajara 2026',
      rows:[['Libro','Book','Las hijas de El Camalote','Las hijas de El Camalote'],['Fecha','Date','Viernes 4 de diciembre · 19:30 h','Friday, December 4 · 7:30 pm'],
            ['Lugar','Venue','EMXI Lecturas · Stand M10, Expo Guadalajara','EMXI Lecturas · Booth M10, Expo Guadalajara'],['Feria','Fair','28 de noviembre al 6 de diciembre de 2026','November 28 to December 6, 2026']],
      link:'https://emxi.org'}],
    ['2026-12-11','Librería El Tecolote','Presentación de The Camalote\'s Daughters, edición en inglés','Presentation of The Camalote\'s Daughters, English edition']
  ];
  var today=new Date(); today.setHours(0,0,0,0);
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;');}
  function evHTML(e,past){
    var d=new Date(e[0]+'T12:00:00'), m=d.getMonth();
    return '<li class="ev'+(past?' past':'')+'"><div class="d"><b>'+String(d.getDate()).padStart(2,'0')+'</b><span data-en="'+MON[m]+'">'+MES[m]+'</span></div><div><h3>'+esc(e[1])+'</h3><p data-en="'+esc(e[3])+'">'+esc(e[2])+'</p></div>'+
      (past?'<span class="tag" data-en="Done">Realizada</span>':'<span class="tag" data-en="Upcoming">Próxima</span>')+'</li>';
  }
  var upcoming=EVENTS.filter(function(e){return new Date(e[0]+'T23:59:00')>=today;});
  var past=EVENTS.filter(function(e){return new Date(e[0]+'T23:59:00')<today;}).reverse();
  if($('events')){
    $('events').innerHTML=upcoming.map(function(e){return evHTML(e,false);}).join('') || '<li class="ev"><div></div><div><p data-en="New dates coming soon.">Muy pronto, nuevas fechas.</p></div></li>';
    if(past.length){$('past').innerHTML=past.map(function(e){return evHTML(e,true);}).join(''); $('past-wrap').hidden=false;}
  }
  function featureHTML(e,home){
    var f=e[4];
    return '<div class="feat"><img src="'+f.poster+'" alt="'+esc(f.alt)+'" width="'+f.w+'" height="'+f.h+'" loading="lazy">'+
      '<div class="feat-body"><p class="eyebrow" data-en="Next presentation">Próxima presentación</p><h2 data-en="'+esc(f.title_en)+'">'+esc(f.title)+'</h2>'+
      '<dl>'+f.rows.map(function(r){return '<div><dt data-en="'+esc(r[1])+'">'+esc(r[0])+'</dt><dd data-en="'+esc(r[3])+'">'+esc(r[2])+'</dd></div>';}).join('')+'</dl>'+
      '<div class="ctas">'+(home?'<a class="btn solid" href="agenda.html" data-en="2026 calendar">Agenda 2026</a>':'')+
      (f.link?'<a class="btn ghost" href="'+f.link+'" target="_blank" rel="noopener">emxi.org</a>':'')+'</div></div></div>';
  }
  if(upcoming.length && upcoming[0][4]){
    if($('feature')){$('feature').innerHTML=featureHTML(upcoming[0],false);$('feature').hidden=false;}
    if($('next-feature')){$('next-feature').querySelector('.wrap').innerHTML=featureHTML(upcoming[0],true);$('next-feature').hidden=false; if($('nextbar')) $('nextbar').remove();}
  }
  if($('nextbar')){
    if(upcoming.length){var e=upcoming[0], d=new Date(e[0]+'T12:00:00');
      $('next-what').innerHTML=esc(e[1])+' <small data-en="'+d.getDate()+' '+MON[d.getMonth()]+' · '+esc(e[3])+'">'+d.getDate()+' '+MES[d.getMonth()]+' · '+esc(e[2])+'</small>';}
    else $('nextbar').hidden=true;
  }

  // where to buy each book: paste each store's link here ("" = link still pending)
  var BUY={
    'camalote-es':{amazon:'https://a.co/d/02llrWOl',mercadolibre:'https://meli.la/1YRX1Qf',tiktok:'', en:{title:"The Camalote's Daughters",amazon:'https://a.co/d/0hVcc72T',mercadolibre:'',tiktok:''}},
    'mechuacan':  {amazon:'https://a.co/d/0aXuvbgF',mercadolibre:'https://www.mercadolibre.com.mx/mechuacan-sus-mujeres-y-el-silencio/up/MLMU5109051028?pdp_filters=item_id%3AMLM6166911532',tiktok:'', en:{title:'Michoacán: The Women Behind the Silence',amazon:'https://www.amazon.com/dp/B0G4R51GSW',mercadolibre:'',tiktok:''}},
    'emprende':   {amazon:'https://a.co/d/0jktjajI',mercadolibre:'',tiktok:''}
  };
  var STORES=[['amazon','Amazon'],['mercadolibre','Mercado Libre']];
  var BAG='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8h12l-1 12H7z"/><path d="M9 8a3 3 0 0 1 6 0"/></svg>';
  function storeLink(url,label,title){
    var a=document.createElement('a'); a.className='store'+(url?'':' pending'); a.innerHTML=BAG+'<span>'+label+'</span>';
    if(url){a.href=url;a.target='_blank';a.rel='noopener';} else {a.href='contacto.html?libro='+encodeURIComponent(title);a.title='Enlace pendiente';}
    return a;
  }
  document.querySelectorAll('[data-buy]').forEach(function(box){
    var links=BUY[box.dataset.buy]||{}, first=box.firstChild, title=box.dataset.title||'';
    var lbl=document.createElement('span'); lbl.className='lbl'; lbl.textContent='Cómpralo en'; lbl.setAttribute('data-en','Buy it on'); box.insertBefore(lbl,first);
    STORES.forEach(function(s){box.insertBefore(storeLink(links[s[0]],s[1],title),first);});
    if(links.en){
      var l2=document.createElement('span'); l2.className='lbl'; l2.textContent='Edición en inglés'; l2.setAttribute('data-en','English edition'); box.appendChild(l2);
      STORES.forEach(function(s){box.appendChild(storeLink(links.en[s[0]],s[1],links.en.title));});
    }
  });

  // language: Spanish is in the page, English in data-en
  function apply(l){
    lang=l; document.documentElement.lang=l;
    document.querySelectorAll('[data-en]').forEach(function(el){
      if(el.dataset.es===undefined) el.dataset.es=el.innerHTML;
      el.innerHTML = l==='en' ? el.dataset.en : el.dataset.es;
    });
    var t=document.documentElement.dataset; if(t.titleEn){ if(!t.titleEs) t.titleEs=document.title; document.title= l==='en'?t.titleEn:t.titleEs; }
    var b=$('lang'); b.textContent=l==='en'?'ES':'EN'; b.setAttribute('aria-label', l==='en'?'Cambiar a español':'Switch to English');
    try{localStorage.setItem(KEY,l);}catch(e){}
  }
  $('lang').addEventListener('click',function(){apply(lang==='en'?'es':'en');});
  if(lang==='en') apply('en');

  // mobile menu
  var nav=$('nav'), mb=$('menu');
  mb.addEventListener('click',function(){var o=nav.classList.toggle('open'); mb.setAttribute('aria-expanded',o);});

  // contact page: prefill from ?libro= or ?servicio=, then open the visitor's email app
  var form=$('form');
  if(form){
    var q=new URLSearchParams(location.search), topic=$('f-topic'), msg=$('f-msg');
    if(q.get('libro')){topic.selectedIndex=0; msg.value=(lang==='en'?'Hi Elisabeth, I would like to order: ':'Hola Elisabeth, me gustaría pedir: ')+q.get('libro');}
    if(q.get('servicio')){topic.selectedIndex={revision:5,asesoria:4,prensa:1}[q.get('servicio')]||0;}
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var n=$('f-name').value.trim(), m=$('f-email').value.trim();
      if(!n||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m)){var fn=$('f-note');fn.textContent=lang==='en'?'Please write your name and a valid email.':'Escribe tu nombre y un correo válido.';fn.style.color='#A4502F';return;}
      location.href='mailto:info@elisabethchavez.com?subject='+encodeURIComponent(topic.options[topic.selectedIndex].text+' · '+n)+'&body='+encodeURIComponent(msg.value+'\n\n'+n+' · '+m);
    });
  }
  if($('yr')) $('yr').textContent=new Date().getFullYear();
})();
'''
from map_part import FINDJS
js = js.replace("  if($('yr'))", FINDJS + "  if($('yr'))", 1)
assert 'near-btn' in js
open(OUT + 'js/site.js', 'w', encoding='utf-8').write(js)

# ---------- shared page frame ----------
NAV = [('libros.html', 'Libros', 'Books'), ('autora.html', 'Sobre la autora', 'About the author'),
       ('agenda.html', 'Agenda 2026', '2026 events'), ('recursos.html', 'Recursos', 'Resources'), ('prensa.html', 'Media', 'Media')]
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Karla:wght@400;500;700&display=swap" rel="stylesheet">'
FAV = between('<link rel="icon"', '\n')
LD = between('<script type="application/ld+json">', '</script>') + '</script>'

def page(fname, title_es, title_en, desc, body, body_class='', ld=False):
    path = '' if fname == 'index.html' else fname.replace('.html', '')
    items = ''.join('<li><a href="%s" data-en="%s"%s>%s</a></li>' % (h, en, ' aria-current="page"' if h == fname else '', es) for h, es, en in NAV)
    items += '<li><a class="nav-cta" href="contacto.html" data-en="Contact"%s>Contacto</a></li>' % (' aria-current="page"' if fname == 'contacto.html' else '')
    return f'''<!doctype html>
<html lang="es" data-title-en="{title_en}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_es}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title_es}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://elisabethchavez.com/{path}">
<meta property="og:image" content="https://elisabethchavez.com/img/elisabeth-retrato.jpg">
<link rel="canonical" href="https://elisabethchavez.com/{path}">
{FAV}
{FONTS}
<link rel="stylesheet" href="css/site.css">
{LD if ld else ''}
</head>
<body class="{body_class}">
<a class="skip" href="#main" data-en="Skip to content">Saltar al contenido</a>
<header class="top">
  <div class="wrap">
    <a class="brand" href="./">Elisabeth Chávez<small data-en="Author">Autora</small></a>
    <nav id="nav" aria-label="Menú principal"><ul>{items}</ul></nav>
    <div style="display:flex;gap:8px;align-items:center">
      <button class="lang" id="lang" type="button" aria-label="Switch to English">EN</button>
      <button class="menu-btn" id="menu" type="button" aria-expanded="false" aria-controls="nav" data-en="Menu">Menú</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <span class="imprint"><img src="img/sen-group-logo-sm.webp" alt="SEN Group Editorial" width="71" height="60"><span>© <span id="yr">2026</span> Elisabeth Chávez Rivera<br><span data-en="Published by SEN Group Editorial">Una publicación de SEN Group Editorial</span></span></span>
    <span><a href="https://www.facebook.com/profile.php?id=61576454641839" target="_blank" rel="noopener">Facebook</a> · <a href="https://www.instagram.com/elisabethchavez_escritora/" target="_blank" rel="noopener">Instagram</a> · <a href="https://www.tiktok.com/@elisabeth.chari" target="_blank" rel="noopener">TikTok</a> · <a href="https://www.amazon.com.mx/stores/Elisabeth-Chavez-Rivera/author/B0FZCMRR3R" target="_blank" rel="noopener">Amazon</a> · <a href="https://listado.mercadolibre.com.mx/_CustId_247005184" target="_blank" rel="noopener">Mercado Libre</a> · <a href="https://elisabethchavez.substack.com/" target="_blank" rel="noopener">Substack</a> · <a href="contacto.html">info@elisabethchavez.com</a> · <span data-en="Todos Santos, Baja California Sur, Mexico">Todos Santos, Baja California Sur, México</span></span>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
'''

def head(eyebrow_es, eyebrow_en, h_es, h_en, lede_es, lede_en):
    return f'''<section class="page-head"><div class="wrap">
  <p class="eyebrow" data-en="{eyebrow_en}">{eyebrow_es}</p>
  <h1 data-en="{h_en}">{h_es}</h1>
  <p class="lede" data-en="{lede_en}">{lede_es}</p>
</div></section>'''

pages = {}

# ---- home ----
pages['index.html'] = page('index.html', 'Elisabeth Chávez Rivera · Autora', 'Elisabeth Chávez Rivera · Author',
  'Elisabeth Chávez Rivera, autora de Las hijas de El Camalote, Mechuacán, sus mujeres y el silencio y Emprende y fracasa como niña. Todos Santos, Baja California Sur.', f'''
<section class="home-hero"><div class="wrap">
  <div>
    <p class="eyebrow" data-en="Writer · Businesswoman · Cultural promoter">Escritora · Empresaria · Promotora cultural</p>
    <h1 class="firma"><img src="img/firma.svg" alt="Elisabeth Chávez Rivera, autora" width="1218" height="260"></h1>
    <p class="sub" data-en="I write true stories that have shaped my life and the way I understand the world.">Escribo historias reales que han marcado mi vida y mi manera de entender el mundo.</p>
    <div class="ctas">
      <a class="btn solid" href="libros.html" data-en="Discover my books">Descubre mis libros</a>
      <a class="btn ghost" href="autora.html" data-en="Read my story">Conoce mi historia</a>
    </div>
  </div>
  <figure><img src="img/elisabeth-retrato.jpg" alt="Retrato de Elisabeth Chávez Rivera en su estudio" width="900" height="1260"></figure>
</div></section>

<section class="nextbar" id="nextbar" style="padding:0"><div class="wrap" style="padding-top:18px;padding-bottom:18px">
  <span class="lbl" data-en="Next presentation">Próxima presentación</span>
  <span class="what" id="next-what"></span>
  <a class="more" href="agenda.html" data-en="2026 calendar">Agenda 2026</a>
</div></section>
<section class="featured" id="next-feature" hidden><div class="wrap"></div></section>

<section class="intro"><div class="wrap">
  <div class="intro-side">
    <p class="eyebrow" data-en="Writer · Businesswoman · Cultural promoter">Escritora · Empresaria · Promotora cultural</p>
    <h2>Elisabeth Chávez Rivera</h2>
    <p class="themes-label" data-en="My books explore">Mis libros exploran</p>
    <div class="themes"><span data-en="Family">Familia</span><span data-en="Migration">Migración</span><span data-en="Motherhood">Maternidad</span><span data-en="Mental health">Salud mental</span><span data-en="Entrepreneurship">Emprendimiento</span><span data-en="Everyday life">Vida cotidiana</span></div>
  </div>
  <div class="intro-text">
    <p class="lead" data-en="I was born in Michoacán, in a town marked by violence, migration and a social context where opportunities seemed limited. I became a mother as a teenager and, from a very young age, I learned to face responsibilities, make decisions and find my own path.">Nací en Michoacán, en un pueblo marcado por la violencia, la migración y un contexto social donde las oportunidades parecían limitadas. Fui madre adolescente y desde muy joven aprendí a enfrentar responsabilidades, tomar decisiones y buscar mi propio camino.</p>
    <p data-en="I have always had an artistic spirit and a particular duality between creativity and the practical sense of building projects. That combination has led me to grow in different fields, from art and literature to the business world, facing both the achievements and the failures that come with each experience.">Siempre he tenido un espíritu artístico y una particular dualidad entre la creatividad y el sentido práctico de construir proyectos. Esa combinación me ha llevado a desarrollarme en distintos sectores, desde el arte y la literatura hasta el mundo empresarial, enfrentando tanto los logros como los fracasos que vienen con cada experiencia.</p>
    <p data-en="Today I write about what I have lived, the women who have been part of my story and the social realities I have come to know. My books explore family, migration, motherhood, mental health, entrepreneurship and the contradictions of everyday life.">Hoy escribo sobre lo que he vivido, las mujeres que han formado parte de mi historia y las realidades sociales que me han tocado conocer. Mis libros exploran la familia, la migración, la maternidad, la salud mental, el emprendimiento y las contradicciones de la vida cotidiana.</p>
    <div class="ctas"><a class="btn solid" href="libros.html" data-en="Discover my books">Descubre mis libros</a><a class="btn ghost" href="autora.html" data-en="Read my story">Conoce mi historia</a></div>
  </div>
</div></section>

<section class="shelf"><div class="wrap">
  <div class="shelf-head">
    <div><p class="eyebrow" data-en="Her books">Sus libros</p><h2 data-en="Three books, one voice">Tres libros, una voz</h2></div>
    <a class="more" href="libros.html" data-en="See catalog and where to buy">Ver catálogo y dónde comprar</a>
  </div>
  <div class="shelf-grid">
    <a href="libros.html#mechuacan"><img src="img/mechuacan.jpg" alt="Portada de Mechuacán, sus mujeres y el silencio" width="600" height="900" loading="lazy"><b>Mechuacán, sus mujeres y el silencio</b><span data-en="2025 · Memoir · also in English">2025 · Autobiografía · también en inglés</span></a>
    <a href="libros.html#camalote"><img src="img/camalote.jpg" alt="Portada de Las hijas de El Camalote" width="400" height="609" loading="lazy"><b>Las hijas de El Camalote</b><span data-en="2026 · Choral novel · also in English">2026 · Novela coral · también en inglés</span></a>
    <a href="libros.html#emprende"><img src="img/emprende.jpg" alt="Portada de Emprende y fracasa como niña" width="600" height="957" loading="lazy"><b>Emprende y fracasa como niña</b><span data-en="2026 · Novelized chronicle · entrepreneurship">2026 · Crónica novelada · emprendimiento</span></a>
  </div>
</div></section>

<section class="quote"><div class="wrap">
  <p data-en="“Her voice comes from experience: building, going through loss, starting over and finding stories that deserve to be told.”">“Su voz nace de la experiencia: construir, atravesar pérdidas, comenzar de nuevo y encontrar historias que merecen ser contadas.”</p>
  <span>Elisabeth Chávez Rivera</span>
</div></section>

<section class="tiles"><div class="wrap">
  <a class="tile" href="autora.html">
    <p class="eyebrow" data-en="About the author">Sobre la autora</p>
    <h3 data-en="Writer, businesswoman and cultural promoter">Escritora, empresaria y promotora cultural</h3>
    <p data-en="Originally from Michoacán and based in Todos Santos, with more than a decade leading community, culinary and social entrepreneurship projects.">Originaria de Michoacán y radicada en Todos Santos, con más de una década liderando proyectos comunitarios, gastronómicos y de emprendimiento social.</p>
    <span class="more" data-en="Read her story">Leer su historia</span>
  </a>
  <a class="tile" href="recursos.html">
    <p class="eyebrow" data-en="For independent writers">Para escritores independientes</p>
    <h3 data-en="I'll help you publish your story">Te acompaño a publicar tu historia</h3>
    <p data-en="Coaching sessions and manuscript review, from the experience of publishing her own books and founding SEN Group Editorial.">Asesorías y revisión de manuscrito, desde la experiencia de publicar sus propios libros y fundar SEN Group Editorial.</p>
    <span class="more" data-en="See resources">Ver recursos</span>
  </a>
</div></section>
''', ld=True)

# ---- books ----
books = section('libros')
books = books[books.index('<div class="books">'):]
books = books.replace('<div class="books">', '<div class="books rows">', 1)
for title, aid in [('Las hijas de El Camalote', 'camalote'), ('Mechuacán, sus mujeres y el silencio', 'mechuacan'), ('Emprende y fracasa como niña', 'emprende')]:
    i = books.index('data-book="%s"' % title)
    j = books.rindex('<article class="book">', 0, i)
    books = books[:j] + '<article class="book" id="%s">' % aid + books[j + len('<article class="book">'):]
    books = books.replace('<a class="main" href="#contacto" data-book="%s"' % title, '<a class="main" href="contacto.html?libro=%s"' % title.replace(' ', '%20'))
    books = books.replace('<div class="actions" data-buy="', '<div class="actions" data-title="%s" data-buy="' % title, 1) if ('data-title="%s"' % title) not in books else books
books = books.replace('<div class="t">', '<h2 class="t">').replace('</div>\n        <p class="meta"', '</h2>\n        <p class="meta"')
import synopsis_part
books = synopsis_part.apply(books)
# order on the books page: Emprende, Camalote, Mechuacán
_arts = {m.group(1): m.group(0) for m in re.finditer(r'<article class="book" id="(\w+)">.*?</article>', books, re.S)}
assert set(_arts) == {'camalote', 'mechuacan', 'emprende'}, _arts.keys()
_s = books.index('<article class="book"'); _e = books.rindex('</article>') + len('</article>')
books = books[:_s] + '\n      '.join(_arts[k] for k in ['emprende', 'camalote', 'mechuacan']) + books[_e:]
import sys; sys.path.insert(0, S)
from map_part import STORES as stores, CSS as MAPCSS
pages['libros.html'] = page('libros.html', 'Libros · Elisabeth Chávez Rivera', 'Books · Elisabeth Chávez Rivera',
  'Los libros de Elisabeth Chávez Rivera: Las hijas de El Camalote, Mechuacán, sus mujeres y el silencio y Emprende y fracasa como niña. Dónde comprarlos.',
  head('Catálogo', 'Catalog', 'Libros', 'Books', 'Novelas y libros que exploran la memoria, la migración, las experiencias de las mujeres y los desafíos de emprender.', "Novels and books that explore memory, migration, women's experiences and the challenges of starting a business.")
  + '\n<section class="page-body" style="padding-top:24px"><div class="wrap">\n<p class="author-store" style="display:flex;flex-wrap:wrap;gap:10px 32px"><a class="more" href="https://www.amazon.com.mx/stores/Elisabeth-Chavez-Rivera/author/B0FZCMRR3R" target="_blank" rel="noopener" data-en="See her author page on Amazon">Ver su perfil de autora en Amazon</a><a class="more" href="https://listado.mercadolibre.com.mx/_CustId_247005184" target="_blank" rel="noopener" data-en="See her store on Mercado Libre">Ver su tienda en Mercado Libre</a><a class="more" href="#librerias" data-en="Find a bookstore near you">Ubicar mi librería más cercana</a></p>\n' + books + '\n</div></section>\n'
  + '<section class="stores-band" id="librerias"><div class="wrap">' + stores + '</div></section>')

# ---- author ----
about = section('sobre')
k = about.index('<h3 class="bio-sub"')
e = about.index('<ul class="timeline">')
about = about[:k] + '<details class="reveal"><summary data-en="Career &amp; biography">Trayectoria y biografía</summary><div>' + about[k:e] + about[e:about.index('</ul>', e) + 5] + '</div></details>' + about[about.index('</ul>', e) + 5:]
about = about.replace('<h2 data-en="About the author">Sobre la autora</h2>', '<h1 data-en="About the author" style="font-size:clamp(44px,6.4vw,72px);margin-bottom:14px">Sobre la autora</h1>')
pages['autora.html'] = page('autora.html', 'Sobre la autora · Elisabeth Chávez Rivera', 'About the author · Elisabeth Chávez Rivera',
  'Elisabeth Chávez Rivera: escritora, empresaria y promotora cultural originaria de Michoacán, radicada en Todos Santos, B.C.S.',
  '<section id="sobre" class="about" style="padding-top:72px"><div class="wrap">' + about + '</div></section>')

# ---- agenda ----
ag = section('agenda')
clubs = ag[ag.index('<h3 class="past-title" data-en="Reading clubs">'):]
pages['agenda.html'] = page('agenda.html', 'Agenda 2026 · Elisabeth Chávez Rivera', '2026 events · Elisabeth Chávez Rivera',
  'Presentaciones, ferias del libro y clubes de lectura de Elisabeth Chávez Rivera en 2026.',
  '<div class="agenda-page">' + head('Agenda literaria', 'Literary calendar', 'Presentaciones 2026', '2026 presentations', 'Presentaciones, ferias del libro y clubes de lectura. Te espero.', 'Book presentations, fairs and reading clubs. See you there.')
  + '\n<section class="page-body" id="agenda" style="padding-top:24px;background:none;color:inherit"><div class="wrap">\n<div id="feature" class="feature-agenda" hidden></div>\n<ul class="events" id="events"></ul>\n'
  + '<details class="reveal" id="past-wrap" hidden><summary data-en="Already presented">Presentaciones realizadas</summary><div><ul class="events" id="past"></ul></div></details>\n'
  + clubs + '\n</div></section></div>', body_class='dark-page')

# ---- resources ----
rec = section('recursos')
rec = rec[rec.index('<div class="services">'):]
rec = rec.replace('href="#contacto" data-svc="Asesoría para escritores independientes"', 'href="contacto.html?servicio=asesoria"').replace('href="#contacto" data-svc="Revisión de manuscrito"', 'href="contacto.html?servicio=revision"')
sen = section('sen').replace('<a class="btn solid" href="#recursos" data-en="See resources">Ver recursos</a>', '<a class="btn solid" href="contacto.html?servicio=asesoria" data-en="Write to SEN Group">Escribir a SEN Group</a>')
pages['recursos.html'] = page('recursos.html', 'Recursos para escritores · Elisabeth Chávez Rivera', 'Resources for writers · Elisabeth Chávez Rivera',
  'Asesoría para escritores independientes y revisión de manuscrito con Elisabeth Chávez Rivera y SEN Group Editorial.',
  head('Recursos para escritores independientes', 'Resources for independent writers', 'Te acompaño a publicar tu historia', "I'll help you publish your story", 'Desde la experiencia de escribir y publicar sus propios libros y fundar SEN Group Editorial.', 'From the experience of writing and publishing her own books and founding SEN Group Editorial.')
  + _WHY
  + '\n<section class="page-body" style="padding-top:24px;border-top:1px solid var(--line)"><div class="wrap"><p class="eyebrow" style="margin-top:56px" data-en="Services">Servicios</p><h2 class="services-title" data-en="How I can help you">Cómo puedo acompañarte</h2>' + rec.replace('margin-top:40px', '') + '</div></section>\n'
  + '<section id="sen" class="sen"><div class="wrap">' + sen + '</div></section>')

# ---- contact ----
ct = section('contacto')
ct = ct.replace('<h2 data-en="Let\'s talk">Escríbeme</h2>', '<h1 data-en="Let\'s talk" style="font-size:clamp(44px,6.4vw,72px);margin-bottom:14px">Escríbeme</h1>')
pages['contacto.html'] = page('contacto.html', 'Contacto · Elisabeth Chávez Rivera', 'Contact · Elisabeth Chávez Rivera',
  'Escríbele a Elisabeth Chávez Rivera: presentaciones, entrevistas, clubes de lectura, librerías, pedidos y asesorías.',
  '<section id="contacto" style="padding-top:72px;min-height:70vh"><div class="wrap contact">' + ct + '</div></section>')

# ---- press & social ----
import prensa_part
pages['prensa.html'] = page('prensa.html', 'Media · Elisabeth Chávez Rivera', 'Media · Elisabeth Chávez Rivera',
  'Redes sociales de Elisabeth Chávez Rivera y contacto para prensa: entrevistas, reseñas, dossier y fotografías.',
  head('Media', 'Media', 'Sigue su historia', 'Follow her story', 'Encuentra a Elisabeth en redes sociales y, si eres medio de comunicación, solicita su dossier de prensa.', 'Find Elisabeth on social media and, if you are a journalist, request her press kit.')
  + prensa_part.BODY)

# ---- 404 ----
pages['404.html'] = page('404.html', 'Página no encontrada · Elisabeth Chávez Rivera', 'Page not found · Elisabeth Chávez Rivera', 'Página no encontrada.',
  head('Error 404', 'Error 404', 'Esta página no existe', 'This page does not exist', 'Quizá el enlace cambió. Vuelve al inicio o explora sus libros.', 'The link may have changed. Go back home or explore her books.')
  + '<section class="page-body"><div class="wrap" style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn solid" href="./" data-en="Home">Inicio</a><a class="btn ghost" href="libros.html" data-en="Books">Libros</a></div></section>')

for name, html in pages.items():
    open(OUT + name, 'w', encoding='utf-8').write(html)

open(OUT + 'sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(
    '<url><loc>https://elisabethchavez.com/%s</loc></url>' % p for p in ['', 'libros', 'autora', 'agenda', 'recursos', 'prensa', 'contacto']) + '</urlset>\n')
print('built', ', '.join(pages))
