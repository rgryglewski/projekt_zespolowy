from django.contrib import admin
from .models import Patient, Doctor, Visit

# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name','surname')


admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Visit)
