from django.contrib import admin
from tenant.models import Application, MessageRoom, Message
# Register your models here.
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'move_in_date', 'dorm', 'is_approved', 'is_disapproved', 'created_at')
    search_fields = ('tenant', 'dorm')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Application, ApplicationAdmin)

class MessageRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'dorm', 'created_at')
    search_fields = ('name', 'dorm', 'created_at')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(MessageRoom, MessageRoomAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('room', 'author', 'content', 'created_at')
    search_fields = ('room', 'author', 'content')
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Message, MessageAdmin)

