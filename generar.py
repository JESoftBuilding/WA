"""Genera las páginas de redirección a WhatsApp a partir de comercios.json.

Uso:  python generar.py   (después: git add -A && git commit && git push)

- El NÚMERO vive sólo en wa.js (lo escribe este script desde comercios.json -> "numero").
- Cada código es una carpeta EN MAYÚSCULAS de hasta 2 caracteres: /WA/F1, /WA/CV...
  La URL completa HTTPS://JESOFTBUILDING.GITHUB.IO/WA/XX mide 38 caracteres, el máximo para
  que el QR siga siendo de 25 módulos (versión 2-M, modo alfanumérico). No usar '?' ni minúsculas.
- La raíz (/WA) es el código del cartel de Expo Madera: no cambiarle el sentido.
- Cambiar el mensaje de un código NO cambia su QR.
"""
import json, os, html

BASE = os.path.dirname(os.path.abspath(__file__))
cfg = json.load(open(os.path.join(BASE, "comercios.json"), encoding="utf-8"))

open(os.path.join(BASE, "wa.js"), "w", encoding="utf-8").write(
    "// Único lugar donde vive el número de WhatsApp de Grabarte. Generado por generar.py.\n"
    f'var GRABARTE_NUMERO = "{cfg["numero"]}";\n'
    "function grabarteIr(mensaje) {\n"
    '  var url = "https://wa.me/" + GRABARTE_NUMERO + "?text=" + encodeURIComponent(mensaje);\n'
    '  var a = document.getElementById("btn"); if (a) a.href = url;\n'
    "  window.location.replace(url);\n"
    "}\n")

PAGE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>Grabarte · WhatsApp</title>
  <!-- Código {code} · {nombre}. Generado por generar.py desde comercios.json: no editar a mano. -->
  <style>
    body {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 32px 16px; text-align: center; color: #222; background: #fafafa; }}
    a.btn {{ display: inline-block; margin-top: 16px; padding: 14px 22px; border-radius: 10px; background: #25D366; color: #fff; text-decoration: none; font-weight: 600; font-size: 18px; }}
    p {{ color: #666; }}
  </style>
</head>
<body>
  <h1>Grabarte</h1>
  <p>Te estamos llevando a WhatsApp…</p>
  <a id="btn" class="btn" href="#">Abrir WhatsApp</a>
  <script src="/WA/wa.js"></script>
  <script>grabarteIr({mensaje_js});</script>
</body>
</html>
"""

for code, c in cfg["codigos"].items():
    assert code == "" or (code.isupper() or code.isdigit() or code.isalnum()) and len(code) <= 2 and code == code.upper(), code
    d = os.path.join(BASE, code) if code else BASE
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(
        PAGE.format(code=code or "(raíz)", nombre=html.escape(c["nombre"]), mensaje_js=json.dumps(c["mensaje"], ensure_ascii=False)))
    print(f'/WA/{code:<3} {c["nombre"]:<40} -> {c["mensaje"]}')
