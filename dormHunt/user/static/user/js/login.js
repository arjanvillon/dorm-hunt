$(document).ready(function(){
    $('#login_form input').each(function(){
        console.log($(this));
        $(this).attr('validate', '');
    });
});