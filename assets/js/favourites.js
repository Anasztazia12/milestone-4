/* Pub favourites slider: centres a dish and leaves the previous and next dishes in view. */
document.addEventListener('DOMContentLoaded', function () {
    const track = document.getElementById('favourites-track');
    const previousButton = document.getElementById('favourites-prev');
    const nextButton = document.getElementById('favourites-next');
    const cards = Array.from(track.querySelectorAll('.favourite-card'));
    const motion = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';

    function centreCard(card, behavior) {
        const left = card.offsetLeft - (track.clientWidth - card.offsetWidth) / 2;
        track.scrollTo({ left: left, behavior: behavior });
    }

    function currentIndex() {
        const middle = track.scrollLeft + track.clientWidth / 2;
        let closest = 0;
        let smallestGap = Infinity;
        cards.forEach(function (card, index) {
            const gap = Math.abs(card.offsetLeft + card.offsetWidth / 2 - middle);
            if (gap < smallestGap) {
                smallestGap = gap;
                closest = index;
            }
        });
        return closest;
    }

    function move(step) {
        const target = (currentIndex() + step + cards.length) % cards.length;
        centreCard(cards[target], motion);
    }

    previousButton.addEventListener('click', function () {
        move(-1);
    });
    nextButton.addEventListener('click', function () {
        move(1);
    });

    /* Move to the next dish. */
    const pauseButton = document.getElementById('favourites-pause');
    let timer = null;
    let pausedByUser = motion === 'auto';

    function startSlideshow() {
        if (pausedByUser || timer) {
            return;
        }
        timer = setInterval(function () {
            move(1);
        }, 5000);
    }

    function stopSlideshow() {
        clearInterval(timer);
        timer = null;
    }

    function updatePauseButton() {
        if (pausedByUser) {
            pauseButton.innerHTML = '&#9654;';
            pauseButton.setAttribute('aria-label', 'Play slideshow');
        } else {
            pauseButton.innerHTML = '&#10074;&#10074;';
            pauseButton.setAttribute('aria-label', 'Pause slideshow');
        }
    }

    pauseButton.addEventListener('click', function () {
        pausedByUser = !pausedByUser;
        updatePauseButton();
        if (pausedByUser) {
            stopSlideshow();
        } else {
            startSlideshow();
        }
    });

    /* Stop while the visitor is looking at or using the slider. */
    track.addEventListener('mouseenter', stopSlideshow);
    track.addEventListener('mouseleave', startSlideshow);
    track.addEventListener('focusin', stopSlideshow);
    track.addEventListener('focusout', startSlideshow);

    centreCard(cards[1], 'auto');
    updatePauseButton();
    startSlideshow();
});