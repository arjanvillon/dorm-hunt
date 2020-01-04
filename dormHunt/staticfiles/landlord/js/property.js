$(document).ready(function(){
    $('#create_property_form input, #create_property_form textarea').each(function(){
        $(this).attr('validate', '');
        $(this).attr('required', '');
    });
});