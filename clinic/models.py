from django.conf import settings
from django.db import models


# Create your models here.


class Patient(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Imię i nazwisko")

    def __str__(self):
        return self.name


class Doctor(models.Model):
    account = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, help_text="Imię i nazwisko")

    def __str__(self):
        return self.name


class Visit(models.Model):
    doctor = models.OneToOneField(Doctor, on_delete=models.CASCADE, help_text="Doktor")
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, help_text="Zapisany pacjent")
    date = models.DateTimeField(help_text="Data i godzina wizyty")

    def __str__(self):
        return f"Wizyta {self.patient.name} u lekarza {self.doctor.name} dnia {self.date.__str__()}"
