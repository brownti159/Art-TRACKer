const carousel = document.querySelector('.carousel');
let isDown = false;
let startX;
let scrollLeft;

carousel.addEventListener('mousedown', e => {
    isDown = true;
    carousel.classList.add('active');
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
});

carousel.addEventListener('mouseleave', e => {
    isDown = false;
    carousel.classList.remove('active');
});

carousel.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    const slider = e.pageX - carousel.offsetLeft;
    const SCROLL_SPEED = 2;
    const walk = (slider - startX) * SCROLL_SPEED;
    carousel.scrollLeft = scrollLeft - walk;
});