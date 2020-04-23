/*$('.navbar-nav li a').removeClass('active');
$('.navbar-nav li b').removeClass('active');
$('.navbar-nav li c').addClass('active');
$('.navbar-nav li d').removeClass('active');
$('.navbar-nav li e').removeClass('active');
*/



var $filters = $('.filter [data-filter]'),
$boxes = $('.boxes [data-category]');

$filters.on('click', function(e) {
e.preventDefault();
var $this = $(this);
$filters.removeClass('active');
$this.addClass('active');

var $filterColor = $this.attr('data-filter');

if ($filterColor == 'all') {
$boxes.removeClass('is-animated')
  .fadeOut().promise().done(function() {
    $boxes.addClass('is-animated').fadeIn();
  });
} else {
$boxes.removeClass('is-animated')
  .fadeOut().promise().done(function() {
    $boxes.filter('[data-category = "' + $filterColor + '"]')
      .addClass('is-animated').fadeIn();
  });
}
});




// Below Code to randomly change colours
var header1 = document.querySelector(".products h1")

function getRandomColor(){
var letters = "0123456789ABCDEF";
var color = '#';
for (var i = 0; i < 6; i++) {
color += letters[Math.floor(Math.random()*16)];
}
return color
}

// Simple function for clarity
function changeHeaderColor(){
colorInput = getRandomColor()
header1.style.color = colorInput;
}

// Now perform the action over intervals (milliseocnds):
setInterval("changeHeaderColor()",500);

