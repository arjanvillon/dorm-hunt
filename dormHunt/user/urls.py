from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('', views.register, name='register'),
    path('forgot-password/', views.user_forgot_password, name='user_forgot_password'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    # path('profile/<int:pk>', views.UserDetailView.as_view(), name='user_profile'),
    path('profile/<int:pk>', views.user_profile, name='user_profile'),
    path('profile/update/<int:pk>', views.UserProfileUpdateView.as_view(), name='edit_profile'),
    path('terms/', views.terms_of_services, name='terms'),
    path('privacy/', views.privacy_policy, name='privacy'),
]
