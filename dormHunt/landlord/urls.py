from django.urls import path
from landlord import views

app_name = 'landlord'

urlpatterns = [
    path('', views.LandlordListView.as_view(), name='landlord_home'),
    path('properties/', views.LandlordProperties.as_view(), name='landlord_properties'),
    path('property/create', views.PropertyCreateView.as_view(), name='property_create'),
    path('property/detail/<int:pk>', views.PropertyDetailView.as_view(), name='property_detail'),

    # NOTE For viewing purposes only
    path('message/', views.LandlordMessages.as_view(), name='landlord_messages'),
    path('message/application/approve/<int:pk>/', views.approve_application, name='approve_application'),
    path('message/application/disapprove/<int:pk>/', views.disapprove_application, name='disapprove_application')
    path('message/individual', views.LandlordIndividualMessages.as_view(), name='individual_messages'),
    
    # Reminder
    path('reminder/create', views.ReminderCreateView.as_view(), name='reminder_create'),
]