# Long synopses for the books page (Spanish text from the author, English translation alongside).
import html, re

def _p(es, en, cls=''):
    return '<p class="%s" data-en="%s">%s</p>' % (cls, html.escape(en, quote=True), es)

MECHUACAN = {
    'tagline': ('Una autobiografía sobre migración, abuso, maternidad adolescente y la búsqueda de una identidad propia.',
                'A memoir about migration, abuse, teenage motherhood and the search for an identity of one\'s own.'),
    'hook': ('¿Qué sucede cuando intentas borrar tu propia historia para convertirte en alguien diferente?',
             'What happens when you try to erase your own story to become someone else?'),
    'visible': [
        ('En <em>Mechuacán, sus mujeres y el silencio</em>, la escritora mexicana Elisabeth Chávez Rivera comparte una historia real marcada por las experiencias que transformaron su vida.',
         'In <em>Mechuacán, sus mujeres y el silencio</em>, Mexican writer Elisabeth Chávez Rivera shares a true story shaped by the experiences that transformed her life.'),
        ('Desde su infancia en un pueblo de Michoacán, donde la violencia, la pobreza y la migración eran parte de la realidad cotidiana, hasta convertirse en madre adolescente y cruzar indocumentada la frontera hacia Estados Unidos.',
         'From her childhood in a town in Michoacán, where violence, poverty and migration were part of everyday life, to becoming a teenage mother and crossing the border into the United States undocumented.'),
    ],
    'more': [
        ('A través de sus recuerdos, la autora aborda experiencias difíciles, como haber sido víctima de grooming, las relaciones familiares, la salud mental y los intentos de dejar atrás un pasado que continuaba formando parte de su identidad.',
         'Through her memories, the author addresses difficult experiences, such as having been a victim of grooming, family relationships, mental health and her attempts to leave behind a past that remained part of her identity.'),
        ('Este libro no pretende ofrecer respuestas fáciles ni presentar una historia perfecta de superación. Es el relato de una mujer que intenta comprender sus decisiones, sus circunstancias y las experiencias que la llevaron a querer desescribirse de su propia vida.',
         'This book does not aim to offer easy answers or a perfect story of overcoming. It is the account of a woman trying to understand her decisions, her circumstances and the experiences that led her to want to unwrite herself from her own life.'),
        ('Una historia autobiográfica mexicana sobre crecer, migrar, sobrevivir y aprender a mirar el pasado sin ocultarlo.',
         'A Mexican autobiographical story about growing up, migrating, surviving and learning to look at the past without hiding it.'),
    ],
}

def block(d):
    out = _p(*d['tagline'], cls='tagline') + _p(*d['hook'], cls='hook')
    out += ''.join(_p(es, en, 'meta') for es, en in d['visible'])
    out += ('<details class="syn-more"><summary data-en="Read full synopsis">Leer sinopsis completa</summary><div>'
            + ''.join(_p(es, en, 'meta') for es, en in d['more']) + '</div></details>')
    return out

def apply(books):
    m = re.search(r'<p class="meta" data-en="The author recovers her own family history.*?</p>', books, re.S)
    assert m, 'mechuacan synopsis'
    return books[:m.start()] + block(MECHUACAN) + books[m.end():]

CSS = '''
.books.rows .book .tagline{font-family:var(--serif);font-size:22px;line-height:1.35;color:var(--ink);margin:2px 0 0;max-width:620px}
.books.rows .book .hook{font-family:var(--serif);font-style:italic;font-size:20px;color:var(--blue);margin:4px 0 2px;max-width:620px}
.syn-more summary{cursor:pointer;list-style:none;display:inline-flex;align-items:center;gap:8px;font-weight:700;color:var(--terra);font-size:15px}
.syn-more summary::-webkit-details-marker{display:none}
.syn-more summary::after{content:"+";font-size:18px;transition:transform .25s}
.syn-more[open] summary::after{transform:rotate(45deg)}
.syn-more > div{padding-top:10px;display:flex;flex-direction:column;gap:12px}
.syn-more .meta{margin:0}
'''

# ---- technical sheet (ficha técnica) per book; None = still to confirm ----
FICHAS = {
    'camalote': [('Autora', 'Author', 'Elisabeth Chávez Rivera', None), ('Año', 'Year', '2026', None),
                 ('Subtítulo', 'Subtitle', 'Mujeres de Michoacán, memoria y raíz', None),
                 ('Género', 'Genre', 'Novela coral', 'Choral novel'), ('Idioma', 'Language', 'Español', 'Spanish'),
                 ('Formato', 'Format', 'Tapa blanda y Kindle', 'Paperback and Kindle'),
                 ('ISBN', 'ISBN', '9786072991682', None),
                 ('ISBN Amazon (tapa blanda)', 'Amazon ISBN (paperback)', '9798247535928', None),
                 ('Edición en inglés', 'English edition', "The Camalote's Daughters", None),
                 ('Editorial', 'Publisher', 'Godesca', None), ('Páginas', 'Pages', '227', None)],
    'mechuacan': [('Autora', 'Author', 'Elisabeth Chávez Rivera', None), ('Año', 'Year', '2025', None),
                  ('Género', 'Genre', 'Autobiografía', 'Memoir'), ('Idioma', 'Language', 'Español', 'Spanish'),
                  ('Edición en inglés', 'English edition', 'Michoacán: The Women Behind the Silence', None),
                  ('Subtítulo en inglés', 'English subtitle', 'A Memoir of Resilience, Migration, and the Untold Stories of Mexican Women', None),
                  ('Formato en inglés', 'English format', 'Tapa blanda y Kindle', 'Paperback and Kindle'),
                  ('ISBN en inglés (tapa blanda)', 'English ISBN (paperback)', '9798276972787', None),
                  ('Editorial', 'Publisher', 'Godesca', None), ('Páginas', 'Pages', '56', None),
                  ('ISBN en español', 'Spanish ISBN', '9786072982475', None)],
    'emprende': [('Autora', 'Author', 'Elisabeth Chávez Rivera', None), ('Año', 'Year', '2026', None),
                 ('Género', 'Genre', 'Crónica novelada · emprendimiento', 'Novelized chronicle · entrepreneurship'), ('Idioma', 'Language', 'Español', 'Spanish'),
                 ('Subtítulo', 'Subtitle', 'De cómo construir un negocio a sostenerte en su caída', 'From building a business to holding yourself up when it falls'),
                 ('Editorial', 'Publisher', 'Godesca', None), ('Páginas', 'Pages', '90', None), ('Formato', 'Format', 'Pasta blanda', 'Paperback'), ('ISBN', 'ISBN', '9786076801048', None)],
}

def ficha(rows):
    cells = ''
    for les, len_, ves, ven in rows:
        if ves is None:
            v = '<dd class="tbd" data-en="To be confirmed">Por confirmar</dd>'
        elif ven:
            v = '<dd data-en="%s">%s</dd>' % (html.escape(ven, quote=True), ves)
        else:
            v = '<dd>%s</dd>' % ves
        cells += '<div><dt data-en="%s">%s</dt>%s</div>' % (len_, les, v)
    return ('<details class="ficha" open><summary data-en="Technical sheet">Ficha técnica</summary><dl>' + cells + '</dl></details>')

_apply_syn = apply
def apply(books):
    books = _apply_syn(books)
    for bid, rows in FICHAS.items():
        i = books.index('<article class="book" id="%s">' % bid)
        j = books.index('<div class="actions"', i)
        books = books[:j] + ficha(rows) + '\n        ' + books[j:]
    return books

CSS += '''
.ficha{margin-top:14px;border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:12px 0;max-width:620px}
.ficha summary{cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--blue)}
.ficha summary::-webkit-details-marker{display:none}
.ficha summary::after{content:"+";font-size:18px;letter-spacing:0;transition:transform .25s}
.ficha[open] summary::after{transform:rotate(45deg)}
.ficha dl{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 28px;margin:10px 0 0}
.ficha dl div{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:10px;padding:8px 0;border-top:1px dashed var(--line);font-size:14.5px}
.ficha dt{color:var(--muted)}
.ficha dd{margin:0;color:var(--ink);font-weight:500}
.ficha dd.tbd{color:#A39788;font-style:italic;font-weight:400}
@media (max-width:640px){.ficha dl{grid-template-columns:1fr}}
'''

EMPRENDE = {
    'tagline': ('La realidad de emprender siendo mujer en México, contada por alguien que ha vivido tanto el éxito como el fracaso empresarial.',
                'The reality of being a woman entrepreneur in Mexico, told by someone who has lived both business success and business failure.'),
    'hook': ('¿Qué pasa cuando haces todo lo posible por mantener un negocio y, aun así, fracasa?',
             'What happens when you do everything you can to keep a business alive, and it still fails?'),
    'visible': [
        ('Durante más de una década, Elisabeth Chávez Rivera ha construido empresas, dirigido equipos, generado empleos y enfrentado las decisiones que implica emprender en México. Pero detrás de cada negocio también hay una mujer, una madre y una persona que ha tenido que aprender a convivir con la incertidumbre, las pérdidas y sus propias limitaciones.',
         'For more than a decade, Elisabeth Chávez Rivera has built companies, led teams, created jobs and faced the decisions that come with running a business in Mexico. But behind every business there is also a woman, a mother and a person who has had to learn to live with uncertainty, loss and her own limits.'),
        ('<em>Emprende y fracasa como niña</em> no es un manual de negocios escrito desde un escritorio, ni una colección de consejos sobre cómo alcanzar el éxito. Es una crónica novelada basada en experiencias reales de emprendimiento, liderazgo, crecimiento empresarial y fracaso.',
         '<em>Emprende y fracasa como niña</em> is not a business manual written from behind a desk, nor a collection of tips on how to succeed. It is a novelized chronicle based on real experiences of entrepreneurship, leadership, business growth and failure.'),
    ],
    'more': [
        ('A través de su propia trayectoria, la autora cuenta lo que significa abrir un negocio, verlo crecer, equivocarse, perder dinero, enfrentar su cierre y, al mismo tiempo, intentar mantener en pie los proyectos que todavía dependen de ella.',
         'Through her own journey, the author tells what it means to open a business, watch it grow, make mistakes, lose money, face its closing and, at the same time, try to keep standing the projects that still depend on her.'),
        ('También aborda una realidad de la que se habla poco: ser mujer emprendedora en México mientras se sostiene una familia, se enfrentan problemas de salud, se administran responsabilidades y se toman decisiones que afectan la vida de otras personas.',
         'She also addresses a reality that is rarely talked about: being a woman entrepreneur in Mexico while supporting a family, facing health problems, managing responsibilities and making decisions that affect other people\'s lives.'),
        ('Con la autoridad que dan los años de experiencia, pero también con la vulnerabilidad de reconocer sus errores, Elisabeth comparte una historia que cuestiona los discursos tradicionales del emprendimiento y esa idea de que trabajar duro siempre garantiza buenos resultados.',
         'With the authority that comes from years of experience, and the vulnerability of owning her mistakes, Elisabeth shares a story that questions the traditional narratives about entrepreneurship and the idea that hard work always guarantees good results.'),
        ('Este libro no promete enseñarte a hacerte millonaria ni convertir cada fracaso en una historia inspiradora. Habla de las consecuencias reales de emprender, de las decisiones que no salieron como se esperaba y de lo que sucede cuando la vida personal y los negocios se derrumban al mismo tiempo.',
         'This book does not promise to teach you how to become a millionaire or to turn every failure into an inspiring story. It talks about the real consequences of entrepreneurship, the decisions that did not turn out as expected and what happens when personal life and business fall apart at the same time.'),
        ('Una historia sobre emprendimiento femenino, liderazgo empresarial, maternidad y fracaso en México, escrita desde la experiencia, con conocimiento, corazón y sin fórmulas inventadas.',
         'A story about women\'s entrepreneurship, business leadership, motherhood and failure in Mexico, written from experience, with knowledge, heart and no made-up formulas.'),
    ],
}

_apply_prev = apply
def apply(books):
    m = re.search(r'<p class="meta" data-en="An autobiographical story about women.*?</p>', books, re.S)
    assert m, 'emprende synopsis'
    books = books[:m.start()] + block(EMPRENDE) + books[m.end():]
    return _apply_prev(books)
