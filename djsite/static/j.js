$(document).ready(function() {
    var post = $('.post');

    $('.prev').hide();    

    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = post.index($(this).closest('.post'));
	post.each(function(j, obj) {
	    if (j < i) {
		obj.parent().removeClass().addClass('colour' + (j+1));
	    }
	    else if (j > i) {
		obj.parent().removeClass().addClass('colour' + j);
	    }
	    else {
		obj.parent().removeClass();
	    }
	});
	$(this).closest('.actions').next('.prev').slideToggle(300);
    });
});
