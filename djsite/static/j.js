$(document).ready(function() {
    var post = $('.post');

    $('.prev').hide();    

    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = post.index($(this).closest('.post'));
	alert(i);
	post.each(function(j, obj) {
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
	$(this).closest('.actions').next('.prev').slideToggle(300);
    });
});
