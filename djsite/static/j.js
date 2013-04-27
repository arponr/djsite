$(document).ready(function() {
    $('.prev').hide();
    $('.toggle').click(function(e) {
	e.preventDefault();
	$(this).parent().parent().next('.prev').slideToggle(300);
    });
});
