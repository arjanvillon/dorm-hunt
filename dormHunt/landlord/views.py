from django.http import JsonResponse

from django.shortcuts import render, get_object_or_404
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)
from geopy.geocoders import Nominatim
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
    # context = {}
    # property_numbers =  Property.objects.all().count()

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

class PropertyDetailView(DetailView):
    model = Property




# favorite
def index_view(request):
    context = {
        "table_list": Property.objects.all(),
        "title": "Table_List"
    }
    return render(request, 'landlord/try.html', context)


def property_favorite(request, pk):
    property_favorite = get_object_or_404(Property, pk=pk)
    # print(request.user)
    # print(request.user.pk)
    # print(property_favorite.favorite.all())
    # try:
    #     property_favorite.favorite.filter(pk=request.user.pk)
    #     p = Property.objects.get(pk=property_favorite.pk)
    #     # print(p)
    #     u = User.objects.get(pk=request.user.pk)
    #     # p.favorite.remove(u)
    #     # property_favorite.favorite.remove(p)
    #     # print(u)
    #     # property_favorite.favorite.add(request.user)
    #     # property_favorite.favorite.exclude(u)
    #     allQ = property_favorite.favorite.all()
    #     for e in allQ:
    #         print(e)

    #     # print(property_favorite.favorite.all())
    #     # print(u)
    #     # print('hello')
    # except ObjectDoesNotExist:
    #     property_favorite.favorite.add(request.user)
    #     print('bye')
    

    if property_favorite.favorite.filter(pk=request.user.pk).exists():
        p = Property.objects.get(pk=property_favorite.pk)
        print('Property Name:', p)
        print('remove')
        print(property_favorite.favorite.all())
        property_favorite.favorite.remove(request.user)
        print('...')
        print(property_favorite.favorite.all())
    else:
        p = Property.objects.get(pk=property_favorite.pk)
        print('Property Name:', p)
        print('add:')
        print(property_favorite.favorite.all())
        property_favorite.favorite.add(request.user)
        print('...')
        print(property_favorite.favorite.all())
    return HttpResponseRedirect(property_favorite.get_absolute_url())


    # property_favorite = get_object_or_404(Property, pk=pk)
    # try:
    #     if property_favorite.is_favorite:
    #         property_favorite.is_favorite = False
    #     else:
    #         property_favorite.is_favorite = True
    #     property_favorite.save()
    # except (KeyError, property_favorite.DoesNotExist):
    #     print('false')
    #     return JsonResponse({'success': False})
    # else:
    #     # return JsonResponse({'success': True})
    #     return render(request, 'landlord/try.html')



