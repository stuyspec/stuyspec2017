var hamburgerBreakpoint = 768;

$(document).ready(function() {

    $(".navbar-toggle").click(function(){

    });

    var navType = $('.fixed-controller').attr('data-nav-type');

    var fixmeTop = 110;//$('.fixed-controller').offset().top;

    if (navType == '1') {
        $('.fixed-controller').addClass('fixed-topnav');
        $('#content').css('margin-top', $('.navbar').height());
    }

    if (navType == '3') {
        $('#content').css('margin-top', $('.navbar').height());
    }

    $(window).scroll(function() {

        var isHamburgerMenu = $(window).width <= 1200;

        if (!isHamburgerMenu) {
            var currentScroll = $(window).scrollTop();
            if (currentScroll > fixmeTop) {
                $('.fixed-controller').addClass('fixed-topnav');
                $('#content').css('margin-top', $('.fixed-controller').outerHeight(true) + 14);
            } else {
                $('.fixed-controller').removeClass('fixed-topnav');
                $('#content').css('margin-top', 0);
            }
        }
    });


    (function($) {
        var $window = $(window),
            $topBar = $('div.top-bar');

        function resize() {

            if ($window.width() < hamburgerBreakpoint) {
                $topBar.attr('id', 'hamburger-menu');
                console.log($topBar.attr('class'));
                return $topBar.attr('id', 'hamburger-menu');
            }
            $topBar.removeAttr('id');
        }

        $window
            .resize(resize)
            .trigger('resize');

    })(jQuery);

});

function switchNavbar() {
    if ( $('.top-bar').attr("id") == "hamburger-menu") {
        $('.top-bar').attr("id", "");
    } else {
        $('.top-bar').attr("id", "hamburger-menu");
    }
}


