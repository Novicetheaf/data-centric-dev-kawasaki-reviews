$(document).ready(function(){
  $(window).scroll(function(){
  	var scroll = $(window).scrollTop();
	  if (scroll > 1) {
	    $("#navbar-scroll").removeClass('navbar-scroll');
      }
      
  })
})

// $(function () {
//             $(document).scroll(function () {
//                 var $nav = $("#mainNavbar");
//                 $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
//             });
//         });