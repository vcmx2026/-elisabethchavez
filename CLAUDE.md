# Sitio web de Elisabeth Chávez Rivera (elisabethchavez.com)

Quien te escribe suele ser **Elisabeth**, la autora, o su hija **Victoria**. Ninguna de las dos es programadora: háblales en español, en palabras sencillas, sin términos técnicos. Haz el cambio, revisa que se vea bien y explícale en una o dos frases qué cambió. No le pidas que ejecute comandos.

## Cómo se publica
- Cloudflare publica el sitio automáticamente desde la rama `main` de este repositorio. Cada `git push` a `main` queda en vivo en 1–2 minutos.
- Lo que se publica es la carpeta `public/`. **No edites a mano los .html de `public/`**: se generan con `fuente/build.py` y tus cambios se perderían.

## Cómo hacer un cambio
1. Edita el archivo de `fuente/` que corresponda (tabla abajo).
2. Regenera el sitio: `python3 fuente/build.py`
3. Revisa el resultado (abre las páginas con Playwright o, como mínimo, busca el texto nuevo en `public/`), en español y en inglés (`?l=en`), en computadora y en celular.
4. Haz commit con un mensaje corto en español y `git push origin main`.

| Qué quiere cambiar | Dónde |
|---|---|
| Enlaces de compra (Amazon, Mercado Libre) | `fuente/build.py`, objeto `BUY` |
| Ficha técnica de un libro (ISBN, páginas, editorial, formato) | `fuente/synopsis_part.py`, `FICHAS` |
| Sinopsis de los libros | `fuente/synopsis_part.py` |
| Presentaciones y eventos de la Agenda | `fuente/build.py`, lista `EVENTS` |
| Librerías, mapa y buscador de la librería más cercana | `fuente/map_part.py` (`SHOPS`, `STORES`) |
| Redes sociales (página Media) | `fuente/prensa_part.py`, `SOCIAL` |
| Página Recursos ("Por qué asesorarte") | `fuente/why_part.py` |
| Textos de inicio, menú y pie de página | `fuente/build.py` |
| Textos de "Sobre la autora", servicios, contacto | `fuente/borrador.html` (secciones con `id`) |
| Fotos y portadas | `public/img/` (JPG, ancho máximo ~1200 px) |

## Reglas del sitio
- **Bilingüe:** todo texto visible va en español en la página y en inglés en el atributo `data-en="..."`. Si cambias un texto, actualiza los dos.
- **Logo de SEN Group:** no se modifica, ni colores ni forma. Usa los archivos `sen-group-logo*.webp` tal cual.
- **Estilo:** elegante y sobrio. Colores con poca saturación, líneas finas y la tipografía actual (Cormorant Garamond + Karla). No agregues colores llamativos ni emojis.
- **Datos reales:** no inventes fechas, premios, cifras, reseñas ni datos biográficos. Si falta un dato, pregúntalo.
- **Contacto:** el correo público es `info@elisabethchavez.com`. No publiques teléfonos personales ni otros correos.
- Nunca pongas contraseñas ni claves en el código.
