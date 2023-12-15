from django.shortcuts import render
from django.views.generic import ListView
from .models import Medicine

# Create your views here.


class MedicineList(ListView):
    model = Medicine
    context_object_name = 'medicine_list'
