document.addEventListener("DOMContentLoaded", function() {
  const hamburger = document.querySelectorAll(".hamburger");
  const hiddenMenu = document.getElementById("header_full_menu");

  hamburger.forEach(function(hamburger) {
    hamburger.addEventListener("click", function() {
      hamburger.classList.toggle("active");
      console.log('togled')
      hiddenMenu.classList.toggle("opened");
    });
  });
});
