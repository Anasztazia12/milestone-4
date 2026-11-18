/* 404 page: count down from 10 and go back to the home page,
   unless the user chooses to stay. */
const redirectMessage = document.getElementById("redirect-message");
const secondsText = document.getElementById("redirect-seconds");
const stopButton = document.getElementById("redirect-stop");

if (redirectMessage && secondsText && stopButton) {
    const homeUrl = redirectMessage.dataset.homeUrl;
    let secondsLeft = 10;

    const timer = setInterval(function () {
        secondsLeft = secondsLeft - 1;
        secondsText.textContent = secondsLeft;

        if (secondsLeft <= 0) {
            clearInterval(timer);
            window.location.href = homeUrl;
        }
    }, 1000);

    /* Let the user stop the countdown and read the page. */
    stopButton.addEventListener("click", function () {
        clearInterval(timer);
        redirectMessage.textContent = "Countdown stopped. Use the buttons below when you are ready.";
        stopButton.remove();
    });
}
