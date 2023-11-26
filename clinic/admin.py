from django.contrib import admin
from .models import Patient,Doctor

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','surname')

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
