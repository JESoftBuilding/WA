// Único lugar donde vive el número de WhatsApp de Grabarte. Generado por generar.py.
var GRABARTE_NUMERO = "5491140739342";
function grabarteIr(mensaje) {
  var url = "https://wa.me/" + GRABARTE_NUMERO + "?text=" + encodeURIComponent(mensaje);
  var a = document.getElementById("btn"); if (a) a.href = url;
  window.location.replace(url);
}
