$(document).ready(function() {
    $('.hidden').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideToggle(300);
    });
});
