$(document).ready(function() {

    $(".navbar-toggle").click(function(){

    });

    var fixmeTop = $('.fixed-controller').offset().top;
    var navType = $('.fixed-controller').attr('data-nav-type');

    if (navType == '1') {
        $('.fixed-controller').addClass('fixed-topnav');
        $('.content').css('margin-top', $('.navbar').height());
    }

    if (navType == '3') {
        $('.content').css('margin-top', $('.navbar').height());
    }

    $(window).scroll(function() {

        var currentScroll = $(window).scrollTop();

        if (navType == '0' && $(window).width() >= 768) {
            if (currentScroll > fixmeTop) {
                $('.fixed-controller').addClass('fixed-topnav');
                $('#content').css('margin-top', $('.fixed-controller').outerHeight(true) + 14);
            } else {
                $('.fixed-controller').removeClass('fixed-topnav');
                $('#content').css('margin-top', 0);
            }
        }
    });

});
