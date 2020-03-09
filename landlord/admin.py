from django.contrib import admin
from landlord.models import Property, AddTenant, Reminder, Expenses
# Register your models here.

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'address', 'latitude', 'longitude', 'created_at')
    search_fields = ('owner', 'name')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Property, PropertyAdmin)

class ReminderAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'category', 'sub_category', 'issue', 'next_service', 'description')
    search_fields = ('property_name', 'category', 'sub_category', 'next_service')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Reminder, ReminderAdmin)


class AddTenantAdmin(admin.ModelAdmin):
    list_display = ('account', 'dorm', 'room_description', 'is_paid', 'balance', 'is_inclusive', 'expense_balance')
    search_fields = ('account', 'dorm', 'room_description')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(AddTenant, AddTenantAdmin)


class AddExpensesAdmin(admin.ModelAdmin):
    list_display = ('property_name', 'name', 'amount')
    search_fields = ('property_name', 'name', 'amount')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Expenses, AddExpensesAdmin)


