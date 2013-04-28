$(document).ready(function() {
    $('.prev').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = $('.post').index($(this).parent('.post'));
	$('.post').each(function(j, obj) {
	    if (j < i) {
		obj.removeClass().addClass('post '+'colour'+j);
	    }
	    else if (j > i) {
		obj.removeClass().addClass('post '+'colour'+(j-1));
	    }
	    else {
		obj.removeClass().addClass('post');
	    }
	});
	$(this).closest('ul').next('.prev').slideToggle(300);
    });
});
