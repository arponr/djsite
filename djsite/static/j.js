$(document).ready(function() {
    $('.toggle down').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideDown();
	$(this).removeClass('down').addClass('up');
    });
    $('.toggle up').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideUp();
	$(this).removeClass('up').addClass('down');
    });
});
