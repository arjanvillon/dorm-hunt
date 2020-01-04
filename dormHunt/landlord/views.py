from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)
from landlord.forms import PropertyForm
from landlord.models import Property
from geopy.geocoders import Nominatim

# Create your views here.
class Landlord(TemplateView):
    template_name = 'landlord/landlord_home.html'


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
        geolocator = Nominatim(user_agent="dormHunt")
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
    
