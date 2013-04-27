$(document).ready(function() {
    $('.hidden').hide();
    $('.toggle').click(function() {
	$(this).next('.hidden').hide();
    });
});
