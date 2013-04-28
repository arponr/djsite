$(document).ready(function() {
    $('.post li:before').click(function(e) {
	e.preventDefault();
	$(this).find('.hidden').slideToggle();
    });

    $('.hidden').hide();    
    $('.post li:before').eq(0).trigger('click');
});
