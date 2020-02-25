var app = new Framework7({
    // App root element
    root: '#landlordApp',
    // App Name
    name: 'Dorm App',
    // App id
    id: 'com.myapp.test',
    // Enable swipe panel
    panel: {
      swipe: 'left',
    },
    // Add default routes
    routes: [
    ],
    // ... other parameters
  });

  var $$ = Dom7;
  
  var mainView = app.views.create('.view-main');

  var smartSelect = app.smartSelect.get('.smart-select');

  var pickerDevice = app.picker.create({
    inputEl: '#id_category',
    cols: [
      {
        textAlign: 'center',
        values: ['Plumbing', 'Appliances', 'Household', 'Outdoors', 'Electrical', 'House Exterior']
      }
    ]
  });


  var pickerDevice = app.picker.create({
    inputEl: '#id_days_before',
    cols: [
      {
        textAlign: 'center',
        values: ['1 day', '2 days', '3 days', '5 days', '10 days', '30 days']
      }
    ]
  });

  var calendarDefault = app.calendar.create({
    inputEl: '#id_date',
    openIn: 'customModal',
    header: true,
    footer: true,
    dateFormat: 'yyyy-mm-dd',
  });
  
  var picker = app.picker.create({
    inputEl: '#id_is_inclusive',
    cols: [
      { 
        textAlign: 'center',
        values: ['Inclusive', 'Not Inclusive'],
        displayValues: ['Inclusive', 'Not Inclusive'],
      }
    ]
  });