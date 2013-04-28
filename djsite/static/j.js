$(document).ready(function() {
    $('.toggle.up, .toggle.down').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideToggle();
	$(this).toggleClass('down up');
    });
});
