document.addEventListener("scroll", function () {
    let parallaxIntensity = window.innerWidth > 475 ? 0.08 : 0.04;
    const translateY = window.pageYOffset;
    document.body.style.setProperty('--scroll', `${-translateY * parallaxIntensity}px`);
});

// Get modal and trigger elements
const modal = document.getElementById("registerModal");
const openModalButton = document.getElementById("registerLink");
const closeModalButton = document.getElementsByClassName("close")[0];

// Open model when the register link is clicked
openModalButton.onclick = function(event) {
    event.preventDefault();
    modal.style.display = "block";
}

closeModalButton.onclick = function() {
    modal.style.display = "none";
}


// Close modal when clicking outside the modal content
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}