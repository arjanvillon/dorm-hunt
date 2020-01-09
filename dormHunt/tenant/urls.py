from django.urls import path
from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('', views.Tenant.as_view(), name='tenant'),
    path('favorites/', views.TenantFavorites.as_view(), name='tenant_favorites'),
    path('search/', views.TenantDormSearch.as_view(), name='dorm_search'),
    path('search/map/', views.tenant_map, name='tenant_map'),
    path('search/property/<int:pk>/', views.ViewPropertyDetailView.as_view(), name='view_property'),
    path('search/property/favorite/<int:pk>/', views.favorite_property, name='favorite_property'),

    # NOTE Temporary, created so i can view my template
    path('search/property/application/<int:pk>', views.Application.as_view(), name='application_form'),
    path('home/', views.TenantHome.as_view(), name='tenant_home'),
]
