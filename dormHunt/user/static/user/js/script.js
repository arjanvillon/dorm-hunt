var pickerDevice = app.picker.create({
    inputEl: '#id_user_type',
    cols: [
      {
        textAlign: 'center',
        values: ['Landlord', 'Tenant']
      }
    ]
  });