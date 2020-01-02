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
  
  var mainView = app.views.create('.view-main');