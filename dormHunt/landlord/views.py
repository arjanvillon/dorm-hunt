from django.shortcuts import render
from django.views.generic import (TemplateView)


# Create your views here.
class Landlord(TemplateView):
    template_name = 'landlord/landlord_home.html'


class LandlordProperties(TemplateView):
    template_name = 'landlord/landlord_properties.html'