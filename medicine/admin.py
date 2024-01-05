from django.contrib import admin
from .models import Pharmacist, Medicine, Presciption

# Register your models here.

admin.site.register(Pharmacist)
admin.site.register(Medicine)
admin.site.register(Presciption)
