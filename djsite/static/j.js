$(document).ready(function() {
    $('.toggle').click(function(e) {
	e.preventDefault();
	$(this).next().find('.hidden').slideToggle();
    });

    $('.hidden').hide();    
    $('.toggle').eq(0).trigger('click');
});
