from django.contrib import admin
from landlord.models import Property, AddTenant
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'address', 'latitude', 'longitude', 'created_at')
    search_fields = ('owner', 'name')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Property, PropertyAdmin)

class AddTenantAdmin(admin.ModelAdmin):
    list_display = ('account_user', 'dorm', 'room_description')
    search_fields = ('account_user', 'dorm', 'room_description')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(AddTenant, AddTenantAdmin)

