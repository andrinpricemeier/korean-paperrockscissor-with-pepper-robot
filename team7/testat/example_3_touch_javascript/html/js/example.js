$(document).ready(function () {
  $(function () {
    FastClick.attach(document.body);
  });
  $("#singen").on("touchstart", function () {
    $("#resultat").html("touchstart");
  });
  $("#singen").on("touchend", function () {
    $("#resultat").html("touchend");
  });
  $("#singen").on("touchcancel", function () {
    $("#resultat").html("touchcancel");
  });
  $("#singen").on("touchmove", function () {
    $("#resultat").html("touchmove");
  });
});
