from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView
    )
import folium
import requests
import json

# SECTION Import Model
from landlord.models import Property
from tenant.models import Application
from tenant.forms import ApplicationForm


# Create your views here.
class Tenant(TemplateView):
    template_name = 'tenant/tenant_home_no_dorm.html'

class TenantFavorites(TemplateView):
    template_name = 'tenant/tenant_favorites.html'

    def get_context_data(self, **kwargs):
        user = self.request.user
        favorites = []

        properties = Property.objects.all()

        for p in properties:
            if p.favorite.filter(pk=user.pk).exists():
                favorites.append(p)
            else:
                pass
        print(favorites)

        context = super().get_context_data(**kwargs)
        context["favorites"] = favorites
        return context
    

class TenantDormSearch(ListView):
    model = Property
    template_name = 'tenant/tenant_search.html'

def tenant_map(request):
    url = "http://api.ipstack.com/check?access_key=41fc2af18a10d4c05cfa0d92f26ba0a8"
    location_request = requests.get(url)
    json_request = json.loads(location_request.text)
    latitude = json_request['latitude']
    longitude = json_request['longitude']

    tenant_map = folium.Map(location=[latitude, longitude], zoom_start=11)
    tooltip = 'Click for more info'

    marker_query = Property.objects.all()

    for marker in marker_query:
        folium.Marker([marker.latitude, marker.longitude], 
                      popup=marker.name,
                      icon=folium.Icon(icon='home', color='blue')).add_to(tenant_map),

    # folium.CircleMarker(location=[latitude, longitude], radius=30, popup='Your Location', color='#3186cc', fill=True, fill_color='#3186cc').add_to(tenant_map),

    tenant_map.save('tenant/templates/tenant/tenant_map.html')
    return render(request, 'tenant/tenant_map.html')

class ViewPropertyDetailView(DetailView):
    model = Property
    template_name = 'tenant/view_property.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        query = Property.objects.get(pk=pk)
        users = query.favorite.all()

        context = super().get_context_data(**kwargs)
        context["users"] = users
        return context

def favorite_property(request, pk):
    current_property = get_object_or_404(Property, pk=pk)
    this_property = Property.objects.get(pk=current_property.pk)

    if current_property.favorite.filter(pk=request.user.pk).exists():
        this_property.favorite.remove(request.user)
    else:
        this_property.favorite.add(request.user)
    return redirect('tenant:view_property', pk=current_property.pk)
    


# NOTE Temporary, created so i can view my template
class Application(CreateView):
    form_class = ApplicationForm
    model = Application
    template_name = 'tenant/application_form.html'

    def form_valid(self, form):
        form.instance.tenant = self.request.user
        pk = self.kwargs['pk']
        print(pk)
        query = Property.objects.get(pk=pk)
        print(query.name)
        form.instance.dorm = query

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        query = Property.objects.get(pk=pk)

        context = super().get_context_data(**kwargs)
        context["property"] = query
        return context

class TenantHome(TemplateView):
    template_name = 'tenant/tenant_home.html'
