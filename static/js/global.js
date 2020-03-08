// Scrolled navbar coloring
$(document).ready(function(){

    $(function () {

        $(document).scroll(function () {

            const navbar = $("#navbar-scroll");
            navbar.toggleClass("scrolled", $(this).scrollTop() > navbar.height());
           
        });

    });

});