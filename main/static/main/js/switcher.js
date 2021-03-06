/*-----------------------------------------------------------------------------------
/* Styles Switcher
-----------------------------------------------------------------------------------*/

window.console =
  window.console ||
  (function () {
    var c = {};
    c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile = c.clear = c.exception = c.trace = c.assert = function () {};
    return c;
  })();

jQuery(document).ready(function ($) {
  $("ul.pattern .color1").click(function () {
    $("#color-opt").attr("href", "css/colors/red.css");
    console.log("red");
    return false;
  });

  $("ul.pattern .color2").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/green.css");
    console.log("green");
    return false;
  });

  $("ul.pattern .color3").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/pink.css");
    return false;
  });

  $("ul.pattern .color4").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/cyan.css");
    return false;
  });

  $("ul.pattern .color5").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/purple.css");
    return false;
  });

  $("ul.pattern .color6").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/blue.css");
    return false;
  });

  $("ul.pattern .color7").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/orange.css");
    return false;
  });

  $("ul.pattern .color8").click(function () {
    $("#color-opt").attr("href", "static/main/css/colors/yellow.css");
    console.log("yellow");
    return false;
  });

  $("#style-switcher .bottom a.settings").click(function (e) {
    e.preventDefault();
    var div = $("#style-switcher");
    if (div.css("left") === "-189px") {
      $("#style-switcher").animate({
        left: "0px",
      });
    } else {
      $("#style-switcher").animate({
        left: "-189px",
      });
    }
  });

  $("ul.pattern li a").click(function (e) {
    e.preventDefault();
    $(this).parent().parent().find("a").removeClass("active");
    $(this).addClass("active");
  });

  $("#style-switcher").animate({
    left: "-189px",
  });
});
