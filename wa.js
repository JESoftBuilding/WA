// Único lugar donde vive el número de WhatsApp de Grabarte. Generado por generar.py.
var GRABARTE_NUMERO = "5491140739342";
// NO se redirige solo: los navegadores sólo abren otra app (WhatsApp) cuando la persona TOCA algo.
// Un salto automático por JavaScript o meta refresh deja al celular mostrando la URL sin abrir nada
// (visto el 2026-09-21 al escanear el QR de la ferretería). Por eso: botón grande, un toque.
function grabartePreparar(mensaje) {
  var url = "https://wa.me/" + GRABARTE_NUMERO + "?text=" + encodeURIComponent(mensaje);
  document.getElementById("btn").href = url;
  document.getElementById("msg").textContent = "“" + mensaje + "”";
  var n = GRABARTE_NUMERO.replace(/^549/, "");
  document.getElementById("num").textContent = n.slice(0, 2) + " " + n.slice(2, 6) + "-" + n.slice(6);
}
