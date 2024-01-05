from django.db import models
from django.conf import settings
from clinic.models import Patient, Doctor

# Create your models here.


class Pharmacist(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Imię i nazwisko")

    def __str__(self):
        return self.name


class Medicine(models.Model):
    name = models.CharField(max_length=150, unique=True, help_text="Nazwa leku")
    description = models.CharField(max_length=200, help_text="Opis leku", null=True)
    needs_rx = models.BooleanField(help_text="Lek na receptę")  # czy na recepte
    stock = models.IntegerField(help_text="Ilość w magazynie")

    def __str__(self):
        return self.name


class Presciption(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.RESTRICT, help_text="Pacjent")
    doctor = models.ForeignKey(Doctor, on_delete=models.RESTRICT, help_text="Lekarz wystawiający")
    prescription = models.ManyToManyField(Medicine, help_text="Lista przepisanych leków")
    date_prescribed = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Recepta dla {self.patient} wystawiona {self.date_prescribed}"
