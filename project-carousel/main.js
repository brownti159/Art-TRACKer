document.addEventListener('DOMContentLoaded', function() {
    let elems = document.querySelectorAll('.carousel');
    let instances = M.Carousel.init(elems);
    console.log("instances ", instances)
    console.log("elems ", elems)
    
    let instance = M.Carousel.getInstance(elems);
    console.log("instance ", instance)
});


// instance.next();
// instance.prev();
