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
