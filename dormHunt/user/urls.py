from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('', views.register, name='register'),
    path('forgot-password/', views.user_forgot_password, name='user_forgot_password'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
