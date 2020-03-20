//TOP SLIDER BANNER
$(document).ready(function() {
  $("#nav-toggle").click(function() {
    $("body, #nav-toggle, #nav-overlay, #nav-fullscreen").toggleClass("open");
  });

  $("#nav-menu a").on("click", function() {
    if (window.innerWidth <= 768) {
      $("#nav-toggle").click();
    }
  });
});
