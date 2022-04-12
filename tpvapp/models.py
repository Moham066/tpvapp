from asyncio.windows_events import NULL
import django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class depence(models.Model):
    description=models.CharField(max_length=500)
    montant=models.FloatField(default=0)
    date=models.DateField(default=None)
    par=models.CharField(max_length=500,default=NULL)

    def __str__(self):
        return 'Dépence'

class recette(models.Model):
    montant=models.FloatField(default=0)
    date=models.DateField(default=None)
    par=models.CharField(max_length=500,default=NULL)
    def __str__(self):
        return 'Recette'
