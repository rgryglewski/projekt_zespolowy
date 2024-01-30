from django.shortcuts import render
from django.views.generic import ListView
from .models import Medicine
from .models import Pharmacist
from .models import Presciption

# Create your views here.


class MedicineList(ListView):
    model = Medicine
    context_object_name = 'medicine_list'

class PharmacistList(ListView):
    model = Pharmacist
    context_object_name = 'pharmacists_list'

class PresciptionList(ListView):
    model = Presciption
    context_object_name = 'presciptions_list'
