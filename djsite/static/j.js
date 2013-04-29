$(document).ready(function() {
    $('.head_toggle.lines').click(function(e) {
	e.preventDefault();
	$(this).parent().parent().next('.hidden').slideToggle();
	$(this).toggleClass('down up');
    });
    $('.prev_toggle.up, .prev_toggle.down').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideToggle();
	$(this).toggleClass('down up');
    });
});
