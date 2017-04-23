$(document).ready(function() {

    $(".navbar-toggle").click(function(){

    });

    var fixmeTop = $('.fixme').offset().top;

    $(window).scroll(function() {

        var currentScroll = $(window).scrollTop();
        if (currentScroll > fixmeTop) {
            $('.fixme').css({
                position: 'fixed',
                top: 0,
                margin: '0 auto',
            });
            // fixed elements don't affect the layout of other elements.
            // have to displace the element below to fake smooth transition when navbar collapses.
            $('.content').css('margin-top', $('.logo-container').height() + 10);
        } else {
            $('.fixme').css({
                position: 'static'
            });
            $('.content').css('margin-top', 0);
        }
    });

});
