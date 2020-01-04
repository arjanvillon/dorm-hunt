from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)

# SECTION Import Forms
from . forms import PropertiesForm

# SECTION Import Models
from . models import Properties


# Create your views here.
class Landlord(TemplateView):
    template_name = 'landlord/landlord_home.html'


class CreateProperties(CreateView):
    form_class = PropertiesForm
    model = Properties