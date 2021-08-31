from django.db import models
from Auth.models import User
# Create your models here.

class pointage(models.Model):
    entre   = models.CharField(max_length=30)
    sortie  = models.CharField(max_length=30)
    retard  = models.CharField(max_length=30)
    absance = models.CharField(max_length=30)   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)


class salaire(models.Model):
    mois      = models.IntegerField()
    heurs_base= models.FloatField()
    heurs_sup = models.FloatField()
    primes    = models.FloatField()  
    total     = models.FloatField()   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

class mission(models.Model):
    description= models.CharField(max_length=30)
    date_debut = models.DateField()
    date_fin   = models.DateField()
    lieu       = models.CharField(max_length=30)   
    état       = models.CharField(max_length=30)   
    user       = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)

