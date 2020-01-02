from django.urls import path
from . import views 

app_name = 'home'

urlpatterns =[
    path('test/', views.TestView.as_view(), name='test_view'),
    path('', views.HomeView.as_view(), name='view_home'),

    # TODO Temporary
    path('user/', views.UserView.as_view(), name='view_user'),
    path('edit-user/', views.UpdateUserView.as_view(), name='update_user'),
]