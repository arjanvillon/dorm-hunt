$(document).ready(function(){
    $('#create_property_form input, #create_property_form textarea').each(function(){
        if($(this).attr('type') === 'checkbox'){
            console.log('test');
        }
        else{
            $(this).attr('validate', '');
            $(this).attr('required', '');
        }
    });

    $('#id_latitude').parent().parent().parent().hide()
    $('#id_longitude').parent().parent().parent().hide();
    
    $('#id_address').attr('autocomplete', 'off');
    $('#id_address').attr('type', 'search');
});


var address = places({
    appId: 'plG0SZE6PIBV',
    apiKey: 'dea587bdeb69aa54404efbc5b73b6f62',
    container: document.querySelector('#id_address'),
});

// const fixedOptions = {
//     appId: 'plG0SZE6PIBV',
//     apiKey: 'dea587bdeb69aa54404efbc5b73b6f62',
//     container: '#id_address',
// };

// const reconfigurableOptions = {
//     useDeviceLocation: true,
// };

// address = places(fixedOptions).configure(reconfigurableOptions);

address.on('change', e => document.getElementById('id_latitude').value = e.suggestion.latlng.lat);
address.on('change', e => document.getElementById('id_longitude').value = e.suggestion.latlng.lng);

$("#algolia-places-listbox-0").on("click", function(){
    alert("hello");
});