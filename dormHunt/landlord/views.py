from django.http import JsonResponse
from django.contrib import messages


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist



# SECTION Import Forms
from landlord.forms import PropertyForm, ReminderForm, AddTenantForm

#SECTION Import Models
from landlord.models import Property, Reminder, AddTenant
from user.models import User, UserProfile
from tenant.models import Application

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
        # address = "{0}, {1}, {2}, Metro Manila, {3}, Philippines".format(form.instance.street, form.instance.barangay, form.instance.city, form.instance.zip_code)
        # address = form.instance.address
        # # Function to store Latitude and Longitude
        # geolocator = Nominatim(user_agent="dormHunt", timeout=None)
        # location = geolocator.geocode(address)

        # if location.latitude != None and location.longitude != None:
        #     form.instance.latitude = location.latitude
        #     form.instance.longitude = location.longitude
        # else:
        #     form.instance.latitude = None
        #     form.instance.longitude = None

        # form.instance.address = "{0} {1}".format(form.instance.house_number, address)
        return super().form_valid(form)

class PropertyDetailView(DetailView):
    model = Property


class LandlordMessages(ListView):
    template_name = 'landlord/landlord_messages.html'
    model = Property

    def get_queryset(self):
        return Property.objects.all().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        properties = self.request.user.property_set.all()
        application_list = []

        try:
            for p in properties:
                applications = Application.objects.filter(dorm=p, is_approved=False, is_disapproved=False)
                for application in applications:
                    application_list.append(application)
            print(len(application_list))
            application_count = len(application_list)

        except ObjectDoesNotExist:
            application_list = ''

        context = super().get_context_data(**kwargs)
        context["application_list"] = application_list
        context["application_count"] = application_count
        return context

def approve_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.approve()
    return redirect('landlord:landlord_messages')

def disapprove_application(request, pk):
    application = get_object_or_404(Application, pk=pk)
    application.disapprove()
    return redirect('landlord:landlord_messages')
class LandlordIndividualMessages(TemplateView):
    template_name = 'landlord/landlord_ind_messages.html'

# Reminders

class ReminderCreateView(CreateView):
    form_class = ReminderForm
    model = Reminder


# Add to Tenant
class TenantAddCreateView(CreateView):
    model = AddTenant
    form_class = AddTenantForm

    def form_valid(self, form):
        
        try:
            query = User.objects.get(email=form.instance.account_user)
        except ObjectDoesNotExist:
            messages.add_message(self.request, messages.INFO, 'The email you entered is not yet a user of this application. Do advise your tenant to sign up to our application for your convenience. Thank you!')
            return redirect('landlord:add_tenant')
        return super().form_valid(form)



