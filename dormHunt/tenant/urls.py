from django.urls import path
from tenant import views

app_name = 'tenant'

urlpatterns = [
    path('', views.Tenant.as_view(), name='tenant'),
]
