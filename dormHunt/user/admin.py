from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User
# Register your models here.


class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_active', 'is_staff', 'is_admin', 'is_superuser')
    search_fields = ('username', 'email')
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
