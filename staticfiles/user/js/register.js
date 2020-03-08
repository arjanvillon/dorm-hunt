$(document).ready(function(){
    $('#registration_form input, #registration_form select').each(function(){
        console.log($(this));
        $(this).attr('validate', '');
    });
});