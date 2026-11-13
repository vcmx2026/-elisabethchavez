# Bookstore map for libros.html: Mexico outline (Natural Earth 1:50m, pre-projected in mexico-map.json) with pins.
import json, os
S = os.path.dirname(os.path.abspath(__file__)) + '/'
m = json.load(open(S + 'mexico-map.json'))
W, H, PT = m['W'], m['H'], m['pts']

from urllib.parse import quote
SHOPS = [
    {'n': 'El Tecolote', 'c': 'Todos Santos, B.C.S.', 'lat': 23.4497, 'lng': -110.2256, 'q': 'Libreria El Tecolote Todos Santos Baja California Sur'},
    {'n': 'Allende Books', 'c': 'La Paz, B.C.S.', 'lat': 24.1597, 'lng': -110.3139, 'q': 'Allende Books La Paz Baja California Sur'},
    {'n': 'Verba Librería', 'c': 'La Paz, B.C.S.', 'lat': 24.1580, 'lng': -110.3110, 'q': 'Verba Libreria La Paz Baja California Sur'},
    {'n': 'Librería León', 'c': 'Puebla, Pue.', 'lat': 19.0440, 'lng': -98.2001, 'q': 'Libreria Leon, Av. 3 Poniente 318, Centro, 72000 Puebla, Pue.', 'url': 'https://maps.app.goo.gl/F52wzo7FtGjY1mWR7',
     'web': 'https://www.librerialeon.com.mx/', 'fb': 'https://www.facebook.com/LibreriaLeon'},
    {'n': 'Inédita', 'c': 'Puebla, Pue.', 'lat': 19.0352, 'lng': -98.2128, 'q': 'Libreria Inedita, Av. 33 Pte. 707, Chulavista, 72420 Puebla, Pue.', 'url': 'https://maps.app.goo.gl/GSqRd2LkfCyJNV447'},
    {'n': 'Centro Librero', 'c': 'Puebla, Pue.', 'lat': 19.0447, 'lng': -98.2003, 'q': 'Centro Librero, Av. 3 Poniente, Centro, 72000 Puebla, Pue.', 'url': 'https://maps.app.goo.gl/gpSh12hHwyFyc5z96'},
]
DIR = 'https://www.google.com/maps/dir/?api=1&destination='
EMB = 'https://maps.google.com/maps?hl=es&z=15&output=embed&q='
def dl(name):
    s = next(x for x in SHOPS if x['n'] == name)
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (s.get('url') or DIR + quote(s['q']), name)

def pin(k, label, sub, dx, dy):
    x, y = PT[k]
    return ('<g class="pin"><circle cx="%.1f" cy="%.1f" r="16" class="halo"/><circle cx="%.1f" cy="%.1f" r="7" class="dot"/>'
            '<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" class="lead"/>'
            '<text x="%.1f" y="%.1f" class="pl">%s</text><text x="%.1f" y="%.1f" class="ps">%s</text></g>') % (
        x, y, x, y, x + 8, y + dy * .15, x + dx - 8, y + dy, x + dx, y + dy + 9, label, x + dx, y + dy + 33, sub)

MAP = ('<svg class="mx-map" viewBox="-10 -10 %d %d" role="img" aria-label="Mapa de México con las librerías donde se encuentran los libros: Todos Santos y La Paz (dos librerías) en Baja California Sur, y Puebla (tres librerías)">' % (W + 20, H + 20)
       + '<defs><pattern id="dots" width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="7" cy="7" r="1.6" fill="#6A8BAF" opacity=".35"/></pattern></defs>'
       + '<path d="%s" class="land"/><path d="%s" fill="url(#dots)"/>' % (m['country'], m['country'])
       + pin('lp', 'La Paz', 'Allende Books · Verba Librería', 110, -60) + pin('ts', 'Todos Santos', 'El Tecolote', 110, 50)
       + pin('pu', 'Puebla', 'León · Inédita · Centro Librero', -110, 85) + '</svg>')

STORES = '''<p class="eyebrow" data-en="Where to find the books">Dónde encontrar los libros</p>
<h2 data-en="Bookstores">Librerías</h2>
<p class="lede" data-en="Physical copies are available in these bookstores.">Los ejemplares físicos se encuentran en estas librerías.</p>
<div class="map-wrap">''' + MAP + '''
  <div class="cities">
    <div class="city"><span class="st">Baja California Sur</span><h3>Todos Santos</h3><p>''' + dl('El Tecolote') + '''</p></div>
    <div class="city"><span class="st">Baja California Sur</span><h3>La Paz</h3><p>''' + dl('Allende Books') + ' · ' + dl('Verba Librería') + '''</p></div>
    <div class="city"><span class="st">Puebla</span><h3>Puebla</h3><p>''' + dl('Librería León') + ' · ' + dl('Inédita') + ' · ' + dl('Centro Librero') + '''</p></div>
  </div>
</div>
<div class="near">
  <div class="near-head">
    <div><h3 data-en="Which bookstore is closest to you?">¿Cuál librería te queda más cerca?</h3>
    <p data-en="We use your location only on this page to calculate the distance; it is not saved or sent anywhere.">Usamos tu ubicación solo en esta página para calcular la distancia; no se guarda ni se envía a ningún lado.</p></div>
    <button class="btn solid" id="near-btn" type="button"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/></svg><span data-en="Find my nearest bookstore">Ubicar mi librería más cercana</span></button>
  </div>
  <div id="near-out" aria-live="polite"></div>
  <div class="gmap">
    <div class="gmap-tabs" role="tablist" aria-label="Librerías">''' + ''.join('<button type="button" role="tab" data-shop="%d" aria-selected="%s">%s<small>%s</small></button>' % (i, 'true' if i == 0 else 'false', s['n'], s['c']) for i, s in enumerate(SHOPS)) + '''</div>
    <div class="gmap-frame"><a class="gmap-ph" id="gmap-ph" href="''' + 'https://www.google.com/maps/search/?api=1&query=' + quote(SHOPS[0]['q']) + '''" target="_blank" rel="noopener"><span data-en="Open map in Google Maps">Abrir mapa en Google Maps</span></a><iframe id="gmap-frame" title="Mapa de Google con la librería seleccionada" src="''' + EMB + quote(SHOPS[0]['q']) + '''" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
    <a class="btn solid" id="gmap-dir" href="''' + DIR + quote(SHOPS[0]['q']) + '''" target="_blank" rel="noopener"><span data-en="Get directions in Google Maps">Cómo llegar con Google Maps</span></a>
    <span class="shop-links" id="gmap-links"></span>
  </div>
</div>'''

CSS = '''
.stores-band{background:var(--card);border-top:1px solid var(--line);padding:88px 0}
.map-wrap{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(0,.7fr);gap:40px;align-items:center;margin-top:36px}
.mx-map{width:100%;height:auto;overflow:visible}
.mx-map .land{fill:#EFE4D6;stroke:#C9B79F;stroke-width:1.2}
.mx-map .halo{fill:var(--blue);opacity:.22;animation:pulse 2.8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.mx-map .dot{fill:var(--terra);stroke:#fff;stroke-width:3}
.mx-map .lead{stroke:var(--terra);stroke-width:1.2;opacity:.55}
.mx-map .pl{font-family:var(--serif);font-size:30px;font-weight:600;fill:var(--ink)}
.mx-map .ps{font-family:var(--sans);font-size:18px;fill:var(--muted)}
@keyframes pulse{0%,100%{transform:scale(1);opacity:.22}50%{transform:scale(1.5);opacity:.08}}
@media (prefers-reduced-motion:reduce){.mx-map .halo{animation:none}}
.cities{display:flex;flex-direction:column;border-top:1px solid var(--line)}
.city{padding:16px 0;border-bottom:1px solid var(--line)}
.city .st{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.city h3{font-size:26px;margin:2px 0}
.city p{margin:0;color:var(--muted)}
.city.other p{color:var(--ink);font-family:var(--serif);font-size:20px;font-weight:600;margin-top:4px}
.near{margin-top:44px;padding:28px 32px;border-radius:24px;background:var(--paper);border:1px solid var(--line)}
.near-head{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px 32px}
.near-head h3{font-size:28px;margin:0 0 4px}
.near-head p{margin:0;color:var(--muted);font-size:14px;max-width:520px}
#near-btn{display:inline-flex;align-items:center;gap:10px}
#near-out:not(:empty){margin-top:22px;padding-top:22px;border-top:1px solid var(--line)}
.near-res{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px}
.near-card{padding:18px 20px;border-radius:18px;background:var(--card);border:1px solid var(--line)}
.near-card.best{border-color:var(--terra);box-shadow:0 18px 34px -28px rgba(164,80,47,.7)}
.near-card .tag{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--terra)}
.near-card h4{font-family:var(--serif);font-size:24px;font-weight:600;margin:4px 0 2px}
.near-card p{margin:0 0 10px;color:var(--muted);font-size:14.5px}
.near-msg{margin:0 0 14px;color:var(--ink)}
.city p a{color:inherit;text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px}
.city p a:hover{color:var(--terra);text-decoration-color:currentColor}
.gmap{margin-top:26px;padding-top:26px;border-top:1px solid var(--line);display:grid;gap:16px}
.gmap-tabs{display:flex;flex-wrap:wrap;gap:8px}
.gmap-tabs button{cursor:pointer;display:flex;flex-direction:column;align-items:flex-start;gap:1px;padding:9px 16px;border-radius:14px;border:1px solid var(--line);background:var(--card);color:var(--ink);font-family:var(--serif);font-size:18px;font-weight:600;transition:background .25s,border-color .25s}
.gmap-tabs button small{font-family:var(--sans);font-size:12px;font-weight:500;color:var(--muted)}
.gmap-tabs button[aria-selected="true"]{background:var(--slate);border-color:var(--slate);color:var(--cream)}
.gmap-tabs button[aria-selected="true"] small{color:#D9E0D9}
.gmap-frame{position:relative;border-radius:18px;overflow:hidden;border:1px solid var(--line);aspect-ratio:16/7;background:var(--card)}
.gmap-frame iframe{position:relative;z-index:1;display:block;width:100%;height:100%;border:0;filter:saturate(.75)}
.gmap-ph{position:absolute;inset:0;display:grid;place-items:center;color:var(--blue);font-weight:700;text-decoration:underline;text-underline-offset:4px;background:repeating-linear-gradient(45deg,var(--card),var(--card) 12px,var(--paper) 12px,var(--paper) 24px)}
#gmap-dir{justify-self:start}
.gmap{grid-template-columns:auto 1fr;align-items:center}.gmap-tabs,.gmap-frame{grid-column:1/-1}
.shop-links{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14.5px}
.shop-links a{color:var(--terra);font-weight:600;text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:3px}
.near-card .shop-links{margin-top:10px}
@media (max-width:880px){.gmap-frame{aspect-ratio:4/3}.near{padding:22px 20px}}
@media (max-width:880px){.map-wrap{grid-template-columns:1fr;gap:24px}.mx-map .pl{font-size:40px}.mx-map .ps{font-size:26px}}
'''

# Nearest-bookstore finder (runs in the browser; the location never leaves the page).
FINDJS = r'''
  var nb=$('near-btn');
  if(nb){
    var SHOPS=__SHOPS__, DIR='__DIR__', EMB='__EMB__';
    function links(s){
      var o=SHOPS.filter(function(x){return x.n===s.n;})[0]||{}, a=[];
      if(o.web) a.push('<a href="'+o.web+'" target="_blank" rel="noopener">'+T('Sitio web','Website')+'</a>');
      if(o.fb) a.push('<a href="'+o.fb+'" target="_blank" rel="noopener">Facebook</a>');
      if(o.ig) a.push('<a href="'+o.ig+'" target="_blank" rel="noopener">Instagram</a>');
      return a.join('');
    }
    var cur=0;
    function show(i){
      cur=i; $('gmap-links').innerHTML=links(SHOPS[i]);
      document.querySelectorAll('.gmap-tabs button').forEach(function(b){b.setAttribute('aria-selected',String(+b.dataset.shop===i));});
      $('gmap-frame').src=EMB+encodeURIComponent(SHOPS[i].q); $('gmap-dir').href=SHOPS[i].url||DIR+encodeURIComponent(SHOPS[i].q); $('gmap-ph').href='https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(SHOPS[i].q);
    }
    document.querySelectorAll('.gmap-tabs button').forEach(function(b){b.addEventListener('click',function(){show(+b.dataset.shop);});});
    var out=$('near-out'), last=null;
    function km(a,b,c,d){var r=Math.PI/180,x=Math.sin((c-a)*r/2),y=Math.sin((d-b)*r/2);return 12742*Math.asin(Math.sqrt(x*x+Math.cos(a*r)*Math.cos(c*r)*y*y));}
    function T(es,en){return lang==='en'?en:es;}
    function card(s,best){
      var d=s.d==null?'':'<p>'+T('A unos ','About ')+(s.d<10?s.d.toFixed(1):Math.round(s.d).toLocaleString())+' km</p>';
      return '<div class="near-card'+(best?' best':'')+'">'+(best?'<span class="tag">'+T('La más cercana','Closest to you')+'</span>':'')
        +'<h4>'+s.n+'</h4><p>'+s.c+'</p>'+d
        +'<a class="more" target="_blank" rel="noopener" href="'+(s.url||DIR+encodeURIComponent(s.q))+'">'+T('Cómo llegar','Get directions')+'</a>'+(links(s)?'<div class="shop-links">'+links(s)+'</div>':'')+'</div>';
    }
    function render(){
      if(!last) return;
      if(last.err){
        out.innerHTML='<p class="near-msg">'+T('No pudimos obtener tu ubicación. Estas son todas las librerías; si ninguna te queda cerca, ','We could not get your location. These are all the bookstores; if none is near you, ')
          +'<a href="contacto.html?libro=">'+T('pídele tu libro directamente a la autora','order your book directly from the author')+'</a>.</p><div class="near-res">'+SHOPS.map(function(s){return card({n:s.n,c:s.c,q:s.q,url:s.url},false);}).join('')+'</div>';
        return;
      }
      var L=SHOPS.map(function(s){return {n:s.n,c:s.c,q:s.q,url:s.url,d:km(last.lat,last.lng,s.lat,s.lng)};}).sort(function(a,b){return a.d-b.d;});
      var far=L[0].d>150;
      out.innerHTML=(far?'<p class="near-msg">'+T('La librería más cercana está a más de 150 km. También puedes ','The nearest bookstore is more than 150 km away. You can also ')
          +'<a href="contacto.html?libro=">'+T('pedirle tu libro a la autora','order your book from the author')+'</a>'+T(' o comprarlo en Amazon y Mercado Libre.',' or buy it on Amazon and Mercado Libre.')+'</p>':'')
        +'<div class="near-res">'+L.slice(0,3).map(function(s,i){return card(s,i===0);}).join('')+'</div>';
    }
    nb.addEventListener('click',function(){
      if(!navigator.geolocation){last={err:1};render();return;}
      nb.disabled=true; out.innerHTML='<p class="near-msg">'+T('Buscando tu ubicación…','Finding your location…')+'</p>';
      navigator.geolocation.getCurrentPosition(function(p){nb.disabled=false;last={lat:p.coords.latitude,lng:p.coords.longitude};render();var L=SHOPS.map(function(s,i){return [km(last.lat,last.lng,s.lat,s.lng),i];}).sort(function(x,y){return x[0]-y[0];});show(L[0][1]);},
        function(){nb.disabled=false;last={err:1};render();},{enableHighAccuracy:false,timeout:12000,maximumAge:600000});
    });
    $('lang').addEventListener('click',function(){render();show(cur);});
    show(0);
  }
'''

import json as _j
FINDJS = FINDJS.replace('__SHOPS__', _j.dumps(SHOPS, ensure_ascii=False)).replace('__DIR__', DIR).replace('__EMB__', EMB)
