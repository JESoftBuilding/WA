# WA

Redirección al WhatsApp de Grabarte. El QR grabado o impreso codifica `HTTPS://JESOFTBUILDING.GITHUB.IO/WA` o `.../WA/XX`, todo en mayúsculas a propósito: así el QR queda de 25 módulos. GitHub Pages distingue mayúsculas en la ruta, por eso el repo se llama `WA` y las carpetas de código van en mayúsculas.

- **El número vive sólo en `comercios.json`** (de ahí sale `wa.js`).
- **Un código por lugar donde hay un QR**, de hasta 2 caracteres (`CV`, `F1`…). Con 2 caracteres la URL mide 38, el máximo para seguir en 25 módulos.
- La raíz `/WA` es el cartel de Expo Madera.
- Cambiar el mensaje de un código no cambia su QR.

Para agregar un comercio o cambiar el número: editar `comercios.json`, correr `python generar.py`, commit y push. No renombrar el repo ni la organización: rompe todos los QR.
