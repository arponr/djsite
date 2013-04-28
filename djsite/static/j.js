$(document).ready(function() {
    var post = $('.post');
    var prev = $('.prev');

    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = post.index($(this).closest('.post'));
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
	prev.hide('slide', {direction:'up'}, 300);
	$(this).closest('.actions').next('.prev').slideToggle(300);
    });

    prev.hide();    
    $('.toggle').eq(0).trigger('click');
});
