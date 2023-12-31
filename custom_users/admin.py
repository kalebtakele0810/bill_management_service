from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','created','updated','last_login','is_admin','is_active','is_staff','is_superuser')
    search_fields = ('email','username')
    readonly_fields = ('created','updated','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)