const reviewPopup = document.getElementById("reviev_popup");
const revievButton = document.getElementById('reviev_popup_button');

revievButton.addEventListener("click", function() {
    reviewPopup.classList.toggle("reviev_popup_visible");

})