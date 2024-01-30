from django.urls import path
from .views import MedicineList
from .views import PharmacistList
from .views import PresciptionList

app_name = 'medicine'

urlpatterns = [
    path('medicine_list', MedicineList.as_view(), name="medicine_list"),
    path('pharmacist_list', PharmacistList.as_view(), name="pharmacist_list"),
    path('presciption_list', PresciptionList.as_view(), name="presciption_list"),
]
