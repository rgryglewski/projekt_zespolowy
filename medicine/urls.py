from django.urls import path
from .views import MedicineList

app_name = 'medicine'

urlpatterns = [
    path('medicine_list', MedicineList.as_view(), name="medicine_list"),
]
