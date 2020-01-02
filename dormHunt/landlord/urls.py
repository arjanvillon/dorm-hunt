from django.urls import path
from landlord import views

app_name = 'landlord'

urlpatterns = [
    path('', views.Landlord.as_view(), name='landlord_home'),
    path('properties/', views.LandlordProperties.as_view(), name='landlord_properties'),

]