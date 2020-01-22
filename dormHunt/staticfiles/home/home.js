var app = new Framework7({
  // App root element
  root: '#app',
  // App Name
  name: 'My App',
  // App id
  id: 'com.dormhunt.app',
  // Enable swipe panel
  panel: {
    swipe: 'left',
  },
  // Add default routes
  routes: [
    {
      path: '/about/',
      url: 'about.html',
      options: {
        transition: 'f7-cover',
      },
    },
    {
      // Page main route
      path: '/templates/home/',
      // Will load page from tabs/index.html file
      url: 'home_tenant.html',
      // Pass "tabs" property to route, must be array with tab routes:
      tabs: [
        // First (default) tab has the same url as the page itself
        {
          // Tab path
          path: '/',
          // Tab id
          id: 'tab1',
          // Fill this tab content from content string
          content: `
            <div class="block">
              <h3>About Me</h3>
              <p>...</p>
            </div>
          `
        },
        // Second tab
        {
          path: '/tab2/',
          id: 'tab2',
          // Fill this tab content with Ajax request:
          url: './pages/tabs/tab2.html',
        },
        // Third tab
        {
          path: '/favorites/',
          id: 'tab3',
          // Load this tab content as a component with Ajax request:
          componentUrl: "{% url 'home:tenant_favorites' %}",
        },
        {
          path: '/tab4/',
          id: 'tab4',
          // Load this tab content as a component with Ajax request:
          componentUrl: './pages/tabs/tab4.html',
        },
      ],
    }
  ],
  // ... other parameters
});


var mainView = app.views.create('.view-main');

