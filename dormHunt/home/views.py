from django.shortcuts import render
from django.views.generic import (TemplateView)

class HomeView(TemplateView):
    template_name = 'home/home-tab.html'

class UserView(TemplateView):
    template_name = 'home/view-user.html'

class UpdateUserView(TemplateView):
    template_name = 'home/update-user.html'
