from django.urls import path
from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('', views.Tenant.as_view(), name='tenant'),
    path('favorites/', views.TenantFavorites.as_view(), name='tenant_favorites'),
    path('search/', views.TenantDormSearch.as_view(), name='dorm_search'),
    path('search/map', views.tenant_map, name='tenant_map'),
]
