$(document).ready(function() {
    $('.toggle').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideToggle();
    });
});
