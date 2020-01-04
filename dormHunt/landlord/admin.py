from django.contrib import admin
from landlord.models import Property
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'address', 'latitude', 'longitude', 'created_at')
    search_fields = ('owner', 'name')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Property, PropertyAdmin)

