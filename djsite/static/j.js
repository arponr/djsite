$(document).ready(function() {
    var post = $('.post');

    $('.prev').hide();    

    $('.toggle').click(function(e) {
	e.preventDefault();
	var i = post.index($(this).closest('.post'));
	post.each(function(j, obj) {
	    if (j < i) {
		alert(j);
	    }
	    else if (j > i) {
		alert(j-1);
	    }
	    else {
		alert("psoej");
	    }
	});
	$(this).closest('.actions').next('.prev').slideToggle(300);
    });
});
