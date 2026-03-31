#!/usr/bin/env python3
import re, os

base = '/data/.openclaw/workspace/goat-streaming'
files = [
    'blog.html',
    'como-instalar-goat-tv-fire-stick.html',
    'como-ver-canales-mexicanos-desde-cualquier-pais.html',
    'como-ver-futbol-en-vivo-gratis.html',
    'contacto.html',
    'descargas.html',
    'goat-streaming-series-peliculas.html',
    'goat-streaming-vs-netflix-2026.html',
    'goat-tv-vs-netflix-2026.html',
    'index.html',
    'mejores-apps-streaming-gratis-2026.html',
    'panel.html',
    'precios.html',
]

# Pattern to match the entire <nav> block
NAV_PATTERN = re.compile(
    r'<nav class="navbar" id="navbar">.*?</nav>',
    re.DOTALL
)

for fname in files:
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build new navbar HTML for this file
    links = [
        ('index.html', 'Home'),
        ('descargas.html', 'Descargas'),
        ('precios.html', 'Precios'),
        ('panel.html', 'Panel de Revendedor'),
        ('blog.html', 'Blog'),
        ('contacto.html', 'Contacto'),
    ]
    links_html = '\n'.join(
        f'    <li><a href="{href}"{" class=\"active\"" if href == fname else ""}>{label}</a></li>'
        for href, label in links
    )

    new_navbar = f'''<nav class="navbar" id="navbar">
  <a href="index.html" class="nav-logo">
    <img src="logo.png" alt="Goat Streaming">
  </a>
  <button class="nav-toggle" onclick="document.querySelector('.nav-links').classList.toggle('open')">☰</button>
  <ul class="nav-links">
{links_html}
  </ul>
</nav>'''

    new_content = NAV_PATTERN.sub(new_navbar, content)

    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {fname}')
    else:
        print(f'No change: {fname}')
