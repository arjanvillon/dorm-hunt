$(document).ready(function(){
    $('#create_property_form input, #create_property_form textarea').each(function(){
        console.log($(this).attr('type'));
        $(this).attr('validate', '');
        $(this).attr('required', '');
    });


});