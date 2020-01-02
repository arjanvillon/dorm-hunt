var today = new Date()

var birthdayCalendar = app.calendar.create({
    inputEl: '#id_birthday',
    openIn: 'customModal',
    header: true,
    footer: true,
    dateFormat: 'yyyy-mm-dd',
    disabled:{
        from: new Date(today.getFullYear(), today.getMonth(), today.getDate())
    },
});

$(document).ready(function(){
    $('#edit_profile_form input').each(function(){
        if($(this).attr('id') == 'picture-clear_id' || $(this).attr('id') == 'id_picture' ){
            console.log($(this).attr('id'));
        }else{
            $(this).attr('validate', '');
            $(this).attr('required', '');
        }
    });
});