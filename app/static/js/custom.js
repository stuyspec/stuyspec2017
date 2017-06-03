$(document).ready(function() {

    $(".navbar-toggle").click(function(){

    });

    var fixmeTop = $('.fixme').offset().top;
    var navType = $('.fixme').attr('data-nav-type');

    if (navType == '1') {
        $('.fixme').addClass('fixed-topnav');
        $('.content').css('margin-top', $('.navbar').height());
    }

    if (navType == '3') {
        $('.content').css('margin-top', $('.navbar').height());
    }

    $(window).scroll(function() {

        var currentScroll = $(window).scrollTop();

        if (navType == '0') {
            if (currentScroll > fixmeTop)
            {
                $('.fixme').addClass('fixed-topnav');
                $('.content').css('margin-top', $('.logo-container').height() + 10);
            }
            else
            {
                $('.fixme').removeClass('fixed-topnav');
                $('.content').css('margin-top', 0);
            }
        }
    });

});
