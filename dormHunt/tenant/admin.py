from django.contrib import admin
from tenant.models import Application
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'move_in_date', 'dorm', 'created_at')
    search_fields = ('tenant', 'dorm')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Application, ApplicationAdmin)