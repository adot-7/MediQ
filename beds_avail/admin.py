from django.contrib import admin
from .models import *


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'total_beds', 'available_beds', 'last_update', 'contact')
# Register your models here.
admin.site.register(Hospital, HospitalAdmin)

