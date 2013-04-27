$('.hidden').hide();

$('.toggle').click(function(event){
    event.preventDefault();
    $(this).next('.hidden').toggle();
}
