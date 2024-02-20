$(document).ready(function () {
    // ... existing code remains the same until this point
    
    // Show the first image immediately but keep its opacity at 0.9 (almost fully visible)
    $('.carousel-item').first().css("opacity", 0.9);
    
    // Function for changing the slide
    function changeSlide() {
        var activeSlide = $('.carousel-item.active'),
            nextSlide;
        
        // Hide the current image before removing the "active" class
        activeSlide.fadeOut(900, function () {
            $(this).hide().removeClass('active');
        });
        
        // Check which slide should be shown next
        if (activeSlide.next('.carousel-item').length) {
            nextSlide = activeSlide.next('.carousel-item');
        } else {
            nextSlide = $('.carousel-item').first();
        }
        
        // Set the opacity of the next slide to 0.9 (almost fully visible)
        nextSlide.css({ opacity: 0.9 }).addClass('active');
        
        // Make the next slide appear after hiding the previous one
        nextSlide.fadeTo(900, 1);
    };
    
    // Change the slide every 2 seconds
    setInterval(changeSlide, 13000);
});