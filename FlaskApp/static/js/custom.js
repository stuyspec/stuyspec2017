var hamburgerBreakpoint = 768;

$(document).ready(function() {

    var $window = $(window),
        $topBar = $('.top-bar');

    var navType = $topBar.attr('data-nav-type');

    var fixmeTop = 110;//$('.fixed-controller').offset().top;

    if (navType == '1') {
        $topBar.attr('id', 'hamburger-menu');
    }

    /* Allows latch scrolling for regular navbar. */
    $window.scroll(function() {
        if ($topBar.attr('id') != 'hamburger-menu') {
            var currentScroll = $window.scrollTop();
            if (currentScroll > fixmeTop) {
                $('.fixed-controller').addClass('fixed-topnav');
                $('#content').css('margin-top', $('.fixed-controller').outerHeight(true) + 14);
            } else {
                $('.fixed-controller').removeClass('fixed-topnav');
                $('#content').css('margin-top', 0);
            }
        }
    });


    /* Adds responsive id hambureger-menu on navType=0's. */
    (function($) {
        function resize() {
            if ($window.width() < hamburgerBreakpoint) {
                $topBar.attr('id', 'hamburger-menu');
                return $topBar.attr('id', 'hamburger-menu');
            }
            $topBar.removeAttr('id');
        }
        if (navType == 0) { // home page
            $window
                .resize(resize)
                .trigger('resize');
        }

    })(jQuery);

});

function switchNavbar() {
    if ( $('.top-bar').attr("id") == "hamburger-menu") {
        $('.top-bar').attr("id", "");
    } else {
        $('.top-bar').attr("id", "hamburger-menu");
    }
}



