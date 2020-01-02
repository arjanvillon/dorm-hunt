from django.shortcuts import render
from django.views.generic import (TemplateView)

# Create your views here.
class Tenant(TemplateView):
    template_name = 'tenant/tenant_home.html'