(function(){
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

  var nb=$('near-btn');
  if(nb){
    var SHOPS=[
      {n:'El Tecolote',c:'Todos Santos, B.C.S.',lat:23.4497,lng:-110.2256,q:'Libreria El Tecolote Todos Santos Baja California Sur'},
      {n:'Allende Books',c:'La Paz, B.C.S.',lat:24.1597,lng:-110.3139,q:'Allende Books La Paz Baja California Sur'},
      {n:'Verba Librería',c:'La Paz, B.C.S.',lat:24.1580,lng:-110.3110,q:'Verba Libreria La Paz Baja California Sur'},
      {n:'Librería León',c:'Puebla, Pue.',lat:19.0436,lng:-98.1983,q:'Libreria Leon Puebla'}];
    var out=$('near-out'), last=null;
    function km(a,b,c,d){var r=Math.PI/180,x=Math.sin((c-a)*r/2),y=Math.sin((d-b)*r/2);return 12742*Math.asin(Math.sqrt(x*x+Math.cos(a*r)*Math.cos(c*r)*y*y));}
    function T(es,en){return lang==='en'?en:es;}
    function card(s,best){
      var d=s.d==null?'':'<p>'+T('A unos ','About ')+(s.d<10?s.d.toFixed(1):Math.round(s.d).toLocaleString())+' km</p>';
      return '<div class="near-card'+(best?' best':'')+'">'+(best?'<span class="tag">'+T('La más cercana','Closest to you')+'</span>':'')
        +'<h4>'+s.n+'</h4><p>'+s.c+'</p>'+d
        +'<a class="more" target="_blank" rel="noopener" href="https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(s.q)+'">'+T('Cómo llegar','Get directions')+'</a></div>';
    }
    function render(){
      if(!last) return;
      if(last.err){
        out.innerHTML='<p class="near-msg">'+T('No pudimos obtener tu ubicación. Estas son todas las librerías; si ninguna te queda cerca, ','We could not get your location. These are all the bookstores; if none is near you, ')
          +'<a href="contacto.html?libro=">'+T('pídele tu libro directamente a la autora','order your book directly from the author')+'</a>.</p><div class="near-res">'+SHOPS.map(function(s){return card({n:s.n,c:s.c,q:s.q},false);}).join('')+'</div>';
        return;
      }
      var L=SHOPS.map(function(s){return {n:s.n,c:s.c,q:s.q,d:km(last.lat,last.lng,s.lat,s.lng)};}).sort(function(a,b){return a.d-b.d;});
      var far=L[0].d>150;
      out.innerHTML=(far?'<p class="near-msg">'+T('La librería más cercana está a más de 150 km. También puedes ','The nearest bookstore is more than 150 km away. You can also ')
          +'<a href="contacto.html?libro=">'+T('pedirle tu libro a la autora','order your book from the author')+'</a>'+T(' o comprarlo en Amazon y Mercado Libre.',' or buy it on Amazon and Mercado Libre.')+'</p>':'')
        +'<div class="near-res">'+L.slice(0,3).map(function(s,i){return card(s,i===0);}).join('')+'</div>';
    }
    nb.addEventListener('click',function(){
      if(!navigator.geolocation){last={err:1};render();return;}
      nb.disabled=true; out.innerHTML='<p class="near-msg">'+T('Buscando tu ubicación…','Finding your location…')+'</p>';
      navigator.geolocation.getCurrentPosition(function(p){nb.disabled=false;last={lat:p.coords.latitude,lng:p.coords.longitude};render();},
        function(){nb.disabled=false;last={err:1};render();},{enableHighAccuracy:false,timeout:12000,maximumAge:600000});
    });
    $('lang').addEventListener('click',render);
  }
  if($('yr')) $('yr').textContent=new Date().getFullYear();
})();
