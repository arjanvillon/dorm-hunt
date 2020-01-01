from django.shortcuts import render
from django.views.generic import (TemplateView)

class HomeView(TemplateView):
    template_name = 'home/home-tab.html'

class TestView(TemplateView):
    template_name = 'home/test.html'
