function get_post() {
    return $(this).closest('.post');
}

$(document).ready(function() {
    $('.prev').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	var post = $('document.body.main.post');
	var i = post.index(get_post());
	alert(i);
	post.each(function(j, obj) {
	    if (j < i) {
		obj.get_post().removeClass().addClass('post '+'colour'+j);
	    }
	    else if (j > i) {
		obj.get_post().addClass('post '+'colour'+(j-1));
	    }
	    else {
		obj.get_post().addClass('post');
	    }
	});
	$(this).closest('.actions').next('.prev').slideToggle(300);
    });
});
