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
    "// NO se redirige solo: los navegadores sólo abren otra app (WhatsApp) cuando la persona TOCA algo.\n"
    "// Un salto automático por JavaScript o meta refresh deja al celular mostrando la URL sin abrir nada\n"
    "// (visto el 2026-09-21 al escanear el QR de la ferretería). Por eso: botón grande, un toque.\n"
    "function grabartePreparar(mensaje) {\n"
    '  var url = "https://wa.me/" + GRABARTE_NUMERO + "?text=" + encodeURIComponent(mensaje);\n'
    '  document.getElementById("btn").href = url;\n'
    '  document.getElementById("msg").textContent = "“" + mensaje + "”";\n'
    '  var n = GRABARTE_NUMERO.replace(/^549/, "");\n'
    '  document.getElementById("num").textContent = n.slice(0, 2) + " " + n.slice(2, 6) + "-" + n.slice(6);\n'
    "}\n")

PAGE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>Grabarte · Pedí el tuyo por WhatsApp</title>
  <!-- Código {code} · {nombre}. Generado por generar.py desde comercios.json: no editar a mano. -->
  <style>
    html, body {{ height: 100%; }}
    body {{ font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; margin: 0; background: #fafafa; color: #222;
           display: flex; align-items: center; justify-content: center; text-align: center; }}
    main {{ padding: 24px 20px; max-width: 420px; }}
    h1 {{ font-size: 40px; margin: 0 0 4px; letter-spacing: .5px; }}
    .lema {{ color: #666; margin: 0 0 28px; font-size: 15px; letter-spacing: 2px; text-transform: uppercase; }}
    a.btn {{ display: block; padding: 20px 18px; border-radius: 14px; background: #25D366; color: #fff; text-decoration: none;
             font-weight: 700; font-size: 22px; box-shadow: 0 4px 14px rgba(37,211,102,.35); }}
    a.btn:active {{ transform: scale(.98); }}
    .msg {{ color: #555; margin: 22px 0 0; font-size: 15px; line-height: 1.4; }}
    .alt {{ color: #888; margin: 18px 0 0; font-size: 14px; }}
  </style>
</head>
<body>
  <main>
    <h1>Grabarte</h1>
    <p class="lema">Ideas que dejan huella</p>
    <a id="btn" class="btn" href="#">Abrir WhatsApp</a>
    <p class="msg">Te va a quedar escrito:<br><span id="msg"></span></p>
    <p class="alt">¿No se abre? Escribinos al <strong id="num"></strong></p>
  </main>
  <script src="/WA/wa.js"></script>
  <script>grabartePreparar({mensaje_js});</script>
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
