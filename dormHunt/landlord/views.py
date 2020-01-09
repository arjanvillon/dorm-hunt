from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist



# SECTION Import Forms
from landlord.forms import PropertyForm

#SECTION Import Models
from landlord.models import Property
from user.models import User

# Create your views here.
class LandlordListView(ListView):
    template_name = 'landlord/landlord_home.html'
    model = Property

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_numbers'] = Property.objects.all().filter(owner=self.request.user).count()
        return context

    def get_queryset(self):
        return Property.objects.all().filter(owner=self.request.user)

class LandlordProperties(TemplateView):
    template_name = 'landlord/landlord_properties.html'

class PropertyCreateView(CreateView):
    form_class = PropertyForm
    model = Property

    def form_valid(self, form):
        form.instance.owner = self.request.user
        # Address
        address = "{0}, {1}, {2}, Metro Manila, {3}, Philippines".format(form.instance.street, form.instance.barangay, form.instance.city, form.instance.zip_code)
        # Function to store Latitude and Longitude
        geolocator = Nominatim(user_agent="dormHunt", timeout=None)
        location = geolocator.geocode(address)

        if location.latitude != None and location.longitude != None:
            form.instance.latitude = location.latitude
            form.instance.longitude = location.longitude
        else:
            form.instance.latitude = None
            form.instance.longitude = None

        form.instance.address = "{0} {1}".format(form.instance.house_number, address)

        print(form.instance.street)
        return super().form_valid(form)

class PropertyDetailView(DetailView):
    model = Property


# NOTE For viewing purposes only
class LandlordMessages(ListView):
    template_name = 'landlord/landlord_messages.html'
    model = Property

    def get_queryset(self):
        return Property.objects.all().filter(owner=self.request.user)

class LandlordIndividualMessages(TemplateView):
    template_name = 'landlord/landlord_ind_messages.html'