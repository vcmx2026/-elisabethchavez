# "Why work with Elisabeth" block for recursos.html: stats, literature × business Venn, path from manuscript to reader,
# and the fairs/channels her books have been through. Only facts from her bio and the site.

STATS = [
    ('3', 'libros publicados', 'published books'),
    ('2', 'ediciones en inglés', 'English editions'),
    ('25+', 'años dirigiendo equipos y negocios', 'years leading teams and businesses'),
    ('5', 'proyectos y empresas fundadas', 'projects and companies founded'),
]
stats = ''.join('<div class="stat"><b>%s</b><span data-en="%s">%s</span></div>' % (n, en, es) for n, es, en in STATS)

LIT = [('Escritura de novela y memoria', 'Writing novels and memoir'), ('Estructura y voz narrativa', 'Structure and narrative voice'),
       ('Ediciones en español e inglés', 'Spanish and English editions'), ('Presentaciones y ferias del libro', 'Book presentations and fairs')]
BIZ = [('Costos, precio y tiraje', 'Costs, pricing and print runs'), ('Venta en Amazon y Mercado Libre', 'Selling on Amazon and Mercado Libre'),
       ('Relación con librerías', 'Working with bookstores'), ('Marca personal de autor', 'Author personal brand')]
li = lambda xs: ''.join('<li data-en="%s">%s</li>' % (en, es) for es, en in xs)

STEPS = [('Idea', 'Idea', 'Qué quieres contar y para quién.', 'What you want to tell, and for whom.'),
         ('Manuscrito', 'Manuscript', 'Estructura, voz y constancia para terminarlo.', 'Structure, voice and the discipline to finish it.'),
         ('Revisión', 'Review', 'Una lectura experta antes de publicar.', 'An expert read before publishing.'),
         ('Publicación', 'Publishing', 'Impresión, plataformas y edición en inglés.', 'Printing, platforms and English editions.'),
         ('Venta', 'Sales', 'Amazon, tiendas en línea y librerías.', 'Amazon, online stores and bookstores.'),
         ('Lectores', 'Readers', 'Presentaciones, ferias y clubes de lectura.', 'Presentations, fairs and reading clubs.')]
steps = ''.join('<li><span class="n">%02d</span><b data-en="%s">%s</b><p data-en="%s">%s</p></li>' % (i + 1, ten, tes, pen, pes)
                for i, (tes, ten, pes, pen) in enumerate(STEPS))

PROOF = ['FIL Guadalajara 2026', 'FILIP 2026 · Puebla', 'FENALEM 2026 · Querétaro', 'Amazon', 'Mercado Libre',
         'Librerías de Baja California Sur y Puebla']
proof = ''.join('<span>%s</span>' % p for p in PROOF[:-1]) + '<span data-en="Bookstores in Baja California Sur and Puebla">%s</span>' % PROOF[-1]

WHY = '''
<section class="why"><div class="wrap">
  <div class="why-intro">
    <p class="eyebrow" data-en="Why consult Elisabeth">Por qué asesorarte con Elisabeth</p>
    <h2 data-en="Literature and business, from someone who has done both">Literatura y negocio, de quien ha recorrido los dos caminos</h2>
    <p class="lede" data-en="Writing a book is only half the journey. The other half is publishing it, pricing it, selling it and getting it into readers' hands. Elisabeth has lived both sides: as an author with three published books and as a businesswoman with more than two decades leading teams and companies.">Escribir un libro es solo la mitad del camino. La otra mitad es publicarlo, ponerle precio, venderlo y llevarlo a los lectores. Elisabeth ha vivido los dos lados: como autora con tres libros publicados y como empresaria con más de dos décadas dirigiendo equipos y empresas.</p>
  </div>
  <div class="stats">''' + stats + '''</div>

  <div class="venn-row">
    <div class="venn-list"><h3 data-en="Literature">Literatura</h3><ul>''' + li(LIT) + '''</ul></div>
    <svg class="venn" viewBox="0 0 420 300" role="img" aria-label="Diagrama: literatura y emprendimiento se unen en la asesoría de Elisabeth">
      <circle cx="150" cy="150" r="118" class="c1"/><circle cx="270" cy="150" r="118" class="c2"/>
      <text x="92" y="155" text-anchor="middle" class="vt" data-en="Literature">Literatura</text>
      <text x="334" y="155" text-anchor="middle" class="vt" data-en="Business">Emprendimiento</text>
      <text x="210" y="146" text-anchor="middle" class="vc" data-en="Your">Tu</text>
      <text x="210" y="170" text-anchor="middle" class="vc" data-en="book">libro</text>
    </svg>
    <div class="venn-list"><h3 data-en="Business">Emprendimiento</h3><ul>''' + li(BIZ) + '''</ul></div>
  </div>

  <div class="path">
    <h3 data-en="From manuscript to reader: she has walked every step">Del manuscrito al lector: ella ha recorrido cada paso</h3>
    <ol>''' + steps + '''</ol>
  </div>

  <div class="proof">
    <span class="plabel" data-en="Her books have been at">Sus libros han estado en</span>
    <div class="chips">''' + proof + '''</div>
  </div>
</div></section>
'''

CSS = '''
.why{padding:56px 0 72px}
.why-intro{max-width:760px}
.why-intro h2{font-size:clamp(32px,4.2vw,48px)}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));margin:44px 0 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stat{padding:28px 20px;border-left:1px solid var(--line);display:flex;flex-direction:column;gap:6px}
.stat:first-child{border-left:0;padding-left:0}
.stat b{font-family:var(--serif);font-size:clamp(46px,5.5vw,68px);font-weight:600;line-height:.9;color:var(--terra)}
.stat span{font-size:14.5px;color:var(--muted);max-width:170px}
.venn-row{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr) minmax(0,1fr);gap:28px;align-items:center;margin:72px 0}
.venn{width:100%;height:auto}
.venn .c1{fill:rgba(106,139,175,.22);stroke:var(--blue);stroke-width:1.5}
.venn .c2{fill:rgba(232,216,196,.65);stroke:#C9B79F;stroke-width:1.5}
.venn .vt{font-family:var(--sans);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;fill:var(--ink)}
.venn .vc{font-family:var(--serif);font-size:24px;font-style:italic;font-weight:600;fill:var(--terra)}
.venn-list h3{font-size:28px;margin-bottom:10px}
.venn-list ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.venn-list li{padding-left:22px;position:relative;font-size:15.5px;color:var(--muted)}
.venn-list li::before{content:"";position:absolute;left:0;top:.62em;width:10px;height:1.5px;background:var(--blue)}
.venn-row .venn-list:last-child{text-align:right}
.venn-row .venn-list:last-child li{padding-left:0;padding-right:22px}
.venn-row .venn-list:last-child li::before{left:auto;right:0}
.path h3{font-size:30px;margin-bottom:24px}
.path ol{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:0;position:relative}
.path ol::before{content:"";position:absolute;left:0;right:0;top:19px;height:1.5px;background:linear-gradient(90deg,var(--blue),var(--cream))}
.path li{position:relative;padding:0 14px 0 0}
.path .n{position:relative;display:inline-grid;place-items:center;width:40px;height:40px;border-radius:50%;background:var(--card);border:1.5px solid var(--blue);font-size:13px;font-weight:700;color:var(--terra);margin-bottom:14px}
.path b{display:block;font-family:var(--serif);font-size:22px;font-weight:600}
.path p{margin:4px 0 0;font-size:14px;color:var(--muted)}
.proof{margin-top:64px;padding:24px 28px;border-radius:20px;background:var(--card);border:1px solid var(--line);display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px}
.plabel{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chips span{font-family:var(--serif);font-size:18px;font-weight:600;padding:6px 14px;border-radius:999px;border:1px solid var(--line);background:var(--paper)}
.services-title{font-size:clamp(30px,3.6vw,42px);margin:0 0 4px}
@media (max-width:880px){
  .stats{grid-template-columns:repeat(2,minmax(0,1fr))}
  .stat:nth-child(3){border-left:0;padding-left:0}
  .stat:nth-child(n+3){border-top:1px solid var(--line)}
  .venn-row{grid-template-columns:1fr;margin:48px 0}
  .venn{max-width:380px;margin:0 auto;order:-1}
  .venn-row .venn-list:last-child{text-align:left}
  .venn-row .venn-list:last-child li{padding-left:22px;padding-right:0}
  .venn-row .venn-list:last-child li::before{left:0;right:auto}
  .path ol{grid-template-columns:1fr;gap:18px}
  .path ol::before{left:19px;right:auto;top:0;bottom:0;width:1.5px;height:auto;background:linear-gradient(180deg,var(--blue),var(--cream))}
  .path li{display:grid;grid-template-columns:40px minmax(0,1fr);column-gap:16px;padding:0}
  .path .n{grid-row:span 2;margin:0}
}
'''
