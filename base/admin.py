from django.contrib import admin

# Register your models here.
from .models import Bill,Payment

admin.site.register(Bill)
admin.site.register(Payment)
