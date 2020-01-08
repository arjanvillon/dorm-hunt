var today = new Date()

var moveInCalendar = app.calendar.create({
    inputEl: '#id_move_in_date',
    openIn: 'customModal',
    header: true,
    footer: true,
    dateFormat: 'yyyy-mm-dd',
    disabled: function (date) {
        if (date.getFullYear() < today.getFullYear()) {
            return true;
        }
        else {
            return false;
        }
    },
});
