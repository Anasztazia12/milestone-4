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

    centreCard(cards[1], 'auto');
});