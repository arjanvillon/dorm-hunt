from django.urls import path
from tenant import views

app_name = 'tenant'

urlpatterns = [
    # Home
    path('', views.Home_Tenant, name='tenant'),
    path('no-dorm', views.no_dorm.as_view(), name='no_dorm'),
    path('dorm/', views.has_dorm.as_view(), name='has_dorm'),

    # Messages
    path('messages/', views.Messages_Tenant, name='messages'),
    path('no-dorm/messages', views.No_Dorm_Messages.as_view(), name='no_dorm-messages'),
    path('dorm/messages', views.Has_Dorm_Messages.as_view(), name='has_dorm-messages'),
    path('dorm/messages/list', views.messages_list, name='messages_list'),

    path('favorites/', views.TenantFavorites.as_view(), name='tenant_favorites'),
    path('search/<int:order>/', views.TenantDormSearch.as_view(), name='dorm_search'),
    path('search/map/', views.tenant_map, name='tenant_map'),
    path('search/property/<int:pk>/', views.ViewPropertyDetailView.as_view(), name='view_property'),
    path('search/property/favorite/<int:pk>/', views.favorite_property, name='favorite_property'),

    # NOTE Temporary, created so i can view my template
    path('search/property/application/<int:pk>', views.ApplicationCreateView.as_view(), name='application_form'),
    path('dorm/request', views.Request.as_view(), name='request'),
    
    # path('dorm/messages/individual', views.TenantIndMessages.as_view(), name='individual_messages'),
    path('dorm/messages/<str:room_name>/', views.tenant_ind_messages, name='room'),
    path('dorm/messages/room/create/', views.create_room, name='create_room'),

]
