// Feedster wants to add a notification menu and a +1 button to their news feed. Click on the notification bell at the top right to see the dropdown menu, and click on each post's +1 button.

var main = function() {
  $(".notification img").click(function(){
    $("ul.notification-menu").toggle();
  });
  
  $(".btn").click(function() {
    $(this).toggleClass("btn-like");
  });
};

$(document).ready(main);