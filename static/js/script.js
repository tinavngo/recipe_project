document.addEventListener("scroll", function () {
    let parallaxIntensity = window.innerWidth > 475 ? 0.08 : 0.04;
    const translateY = window.pageYOffset;
    document.body.style.setProperty('--scroll', `${-translateY * parallaxIntensity}px`);
});

// Listen for the 'DOMContentLoaded' event to ensure the DOM is fully loaded before running the script.
document.addEventListener("DOMContentLoaded", function () {
    // Retrieves the modal, image, and selector elements by their IDs or class names.
    const modal = document.getElementById("chartModal");
    const img = document.getElementById("chartImage");
    const selector = document.getElementById("chartSelector");
    const span = document.getElementsByClassName("close")[0];

    // Checks if the chart selector exists to avoid errors in case it's not present in the DOM.
    if (selector) {
        // Adds an event listener to handle the change event on the selector.
        selector.addEventListener('change', function () {
            // Retrieves the selected chart value.
            const chartValue = selector.value;
            // Switches based on the selected chart value to update the image source.
            switch (chartValue) {
                case 'popularIngredients':
                    img.src = popularIngredientsChart;
                    break;
                case 'recipeDifficultyDistribution':
                    img.src = recipeDifficultyDistributionChart;
                    break;
                case 'cookingTimeByDifficulty':
                    img.src = cookingTimeByDifficultyChart;
                    break;
                default:
                    img.src = '';
            }
            // Displays the modal by changing its style to 'block'.
            modal.style.display = "block";
        });
    }

    // Checks if the close button (span) exists.
    if (span) {
        // Adds an onclick event listener to the close button to hide the modal.
        span.onclick = function () {
            if (modal) {
                modal.style.display = "none";
            }
        };
    }

    // Adds an onclick event listener to the window to close the modal when clicking outside of it.
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
