$(document).ready(function() {

    $(".navbar-toggle").click(function(){

    });

    var fixmeTop = $('.fixme').offset().top;

    $(window).scroll(function() {

        var currentScroll = $(window).scrollTop();
        if (currentScroll > fixmeTop) {
            $('.header-wrapper').css({
                position: 'fixed',
                width: "85%",
                margin: '0 auto',
                zIndex: 1000,
            });
            $('#logo').hide();
            // fixed elements don't affect the layout of other elements.
            // have to displace the element below to fake smooth transition when navbar collapses.
            $('.content').css('margin-top', $('.logo-container').height() + 150);
        } else {
            $('.header-wrapper').css({
                position: 'static',
                width: 'auto',
            });
            $('#logo').show();
            $('.fixme').css({
                position: 'static'
            });
            $('.content').css('margin-top', 0);
        }
    });

});
