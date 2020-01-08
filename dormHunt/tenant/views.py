from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
    )
import folium
import requests
import json

# SECTION Import Model
from landlord.models import Property


# Create your views here.
class Tenant(TemplateView):
    template_name = 'tenant/tenant_home.html'

class TenantFavorites(TemplateView):
    template_name = 'tenant/tenant_favorites.html'

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