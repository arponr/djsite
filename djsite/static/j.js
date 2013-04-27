$(document).ready(function() {
    $('.hidden').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	$(this).next('.hidden').slideToggle(300);
    });
});
