function updateStep() {
  var Etapa = document.getElementById("Etapa");
  if (Etapa.innerHTML === "Sample") Etapa.innerHTML = "Metada";
  var ruta = document.getElementById("ruta");
  ruta.innerHTML =
    ruta.innerHTML +
    " =>" +
    "<a href='#' id='" +
    Etapa.innerHTML +
    "'>" +
    Etapa.innerHTML +
    "</a>";
}
