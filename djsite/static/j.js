$(document).ready(function() {
    $('.toggle').click(function(e) {
	e.preventDefault();
	/*
	var i = post.index($(this).closest('.post'));
	post.each(function(j, obj) {
	    if (j < i) {
		$(this).parent().removeClass().addClass('colour colour' + (j+1));
	    }
	    else if (j > i) {
		$(this).parent().removeClass().addClass('colour colour' + j);
	    }
	    else {
		$(this).parent().removeClass();
	    }
	});
	if (i != last) {	    
	    prev.slideUp(400);
	    last = i;
	}
	*/
	$(this).next('.hidden').slideToggle();
    });

    $('.hidden').hide();    
    $('.toggle').eq(0).trigger('click');
});
