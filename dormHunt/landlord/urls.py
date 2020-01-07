from django.urls import path
from landlord import views

app_name = 'landlord'

urlpatterns = [
    path('', views.LandlordListView.as_view(), name='landlord_home'),
    path('properties/', views.LandlordProperties.as_view(), name='landlord_properties'),
    path('property/create', views.PropertyCreateView.as_view(), name='property_create'),
    path('property/detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),
    path('property/favorites/<int:pk>', views.property_favorite, name='property_favorite'),
    path('property/try', views.index_view, name='try'),

]