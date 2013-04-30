$(document).ready(function() {
    $('.lines').click(function(e) {
	e.preventDefault();
	$(this).parent().parent().next('.hidden').slideToggle(300);
    });
    $('.title').click(function(e) {
	e.preventDefault();
	$(this).parent().next('.hidden').slideToggle(300);
    });
});
