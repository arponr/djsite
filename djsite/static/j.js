$(document).ready(function() {
    $('.prev').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	var post = $(document.body.main.post);
	alert("here 1");
	var i = post.index($(this).parent('.post'));
	alert("here 2");
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
