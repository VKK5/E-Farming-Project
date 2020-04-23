
$('.navbar-nav li a').click(function() {
    $('.navbar-nav li a').removeClass('active');
    $(this).addClass('active');
  });

// Below Code to Change data-filter link colour when clicked

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

/*
var $temp = $('.navbar-nav[class]'),

$temp.on('click',function(d){
	d.preventDefault();
	var $this = $(this);
	$temp.removeClass('active');
	$this.addClass('active');
})*/


// Below Code to Change navigator link colour when clicked
$('.navbar-nav li a').click(function() {
  $('.navbar-nav li a').removeClass('active');
  $(this).addClass('active');
});



// Below Code to Change navigator link colour while scrolling
$( document ).ready(function() { // Tells the function to wait to preform until everything on the page has loaded.
		$(window).scroll(function() { // Says this function is preformed continuisly while scrolling.
		    var Scroll = $(window).scrollTop() + 1, // This variable finds the distance you have scrolled from the top.
						section1 = $('#section1').offset().top, // This variable finds the distance between #section-one and the top. Replace #section-one with the ID of your section.
						section2 = $('#section2').offset().top; // This variable finds the distance between #section-two and the top. Replace #section-two with the ID of your section. You can duplicate this for as many sections as you want.
                        section3 = $('#section3').offset().top;

		    if (Scroll >= section1) 
		    { // If you have scrolled past section one do this.
		        $(".a").addClass("active"); // Adds class of current-menu-item to the menu item with a class of menu-item-1
		    } 
		    else 
		    { // If you have not scrolled section one do this.
		        $(".a").removeClass("active"); // Removes class of current-menu-item to the menu item with a class of menu-item-1
		    }
			if (Scroll >= section2) 
			{ // If you have scrolled past section two do this.You can duplicate this for as many sections as you want.
		        $(".b").addClass("active"); // Adds class of current-menu-item to the menu item with a class of menu-item-2
				$(".a").removeClass("active"); // Removes class of current-menu-item to the menu item with a class of menu-item-1
		    } 

		    else 
		    { // If you have not scrolled section two do this.
		        $(".b").removeClass("active"); // Removes class of current-menu-item to the menu item with a class of menu-item-2
		    }
		    

		    if (Scroll >= section3) 
			{ // If you have scrolled past section two do this.You can duplicate this for as many sections as you want.
		        $(".c").addClass("active"); // Adds class of current-menu-item to the menu item with a class of menu-item-2
				$(".a").removeClass("active"); // Removes class of current-menu-item to the menu item with a class of menu-item-1
		        $(".b").removeClass("active");
		    } 
		    else 
		    { // If you have not scrolled section two do this.
		        $(".c").removeClass("active"); // Removes class of current-menu-item to the menu item with a class of menu-item-2
		    }
		});
});

$(window).on('beforeunload', function() {
  $('body').hide();
  $(window).scrollTop(0);
});




// Below Code to randomly change colours
var header1 = document.querySelector(".brandforcolours")
var header2 = document.querySelector("#section3 h1")

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
  header2.style.color = colorInput;
}

// Now perform the action over intervals (milliseocnds):
setInterval("changeHeaderColor()",500);
