from django.shortcuts import render
from django.views.generic import (TemplateView, CreateView)

# SECTION Import Forms
from landlord.forms import PropertyForm

#SECTION Import Models
from landlord.models import Property


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
        return super().form_valid(form)
    
