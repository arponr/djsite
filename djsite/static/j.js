$(document).ready(function() {
    var post = $('.post');
    var prev = $('.prev');
    var last = -1;

    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = post.index($(this).closest('.post'));
	if (i === last) {
	    return;
	}
	post.each(function(j, obj) {
	    if (j < i) {
		$(this).parent().removeClass().addClass('colour' + (j+1));
	    }
	    else if (j > i) {
		$(this).parent().removeClass().addClass('colour' + j);
	    }
	    else {
		$(this).parent().removeClass();
	    }
	});
	prev.slideUp(300);
	$(this).closest('.actions').next('.prev').slideToggle(300);
	last = i;
    });

    prev.hide();    
    $('.toggle').eq(0).trigger('click');
});
