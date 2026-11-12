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
    ['2026-12-04','FIL Guadalajara','Presentación de Las hijas de El Camalote · 19:30 h · Stand M10','Presentation of Las hijas de El Camalote · 7:30 pm · Booth M10'],
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
  if($('nextbar')){
    if(upcoming.length){var e=upcoming[0], d=new Date(e[0]+'T12:00:00');
      $('next-what').innerHTML=esc(e[1])+' <small data-en="'+d.getDate()+' '+MON[d.getMonth()]+' · '+esc(e[3])+'">'+d.getDate()+' '+MES[d.getMonth()]+' · '+esc(e[2])+'</small>';}
    else $('nextbar').hidden=true;
  }

  // where to buy each book: paste each store's link here ("" = link still pending)
  var BUY={
    'camalote-es':{amazon:'https://www.amazon.com.mx/dp/B0GMJ259QH',mercadolibre:'',tiktok:'', en:{title:"The Camalote's Daughters",amazon:'',mercadolibre:'',tiktok:''}},
    'mechuacan':  {amazon:'https://a.co/d/0aXuvbgF',mercadolibre:'https://www.mercadolibre.com.mx/mechuacan-sus-mujeres-y-el-silencio/up/MLMU5109051028?pdp_filters=item_id%3AMLM6166911532',tiktok:'', en:{title:'Michoacán: The Women Behind the Silence',amazon:'https://www.amazon.com/dp/B0G4R51GSW',mercadolibre:'',tiktok:''}},
    'emprende':   {amazon:'',mercadolibre:'',tiktok:''}
  };
  var STORES=[['amazon','Amazon'],['mercadolibre','Mercado Libre'],['tiktok','TikTok Shop']];
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
    if(q.get('servicio')){topic.selectedIndex=q.get('servicio')==='revision'?5:4;}
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var n=$('f-name').value.trim(), m=$('f-email').value.trim();
      if(!n||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(m)){var fn=$('f-note');fn.textContent=lang==='en'?'Please write your name and a valid email.':'Escribe tu nombre y un correo válido.';fn.style.color='#A4502F';return;}
      location.href='mailto:contacto@elisabethchavez.com?subject='+encodeURIComponent(topic.options[topic.selectedIndex].text+' · '+n)+'&body='+encodeURIComponent(msg.value+'\n\n'+n+' · '+m);
    });
  }
  if($('yr')) $('yr').textContent=new Date().getFullYear();
})();
