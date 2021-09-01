from django.db import models
from Auth.models import User
# Create your models here.

class pointage(models.Model):
    entre   = models.CharField(max_length=30,default="None")
    sortie  = models.CharField(max_length=30,default="None")
    date    = models.CharField(max_length=30,default="None")
    retard  = models.CharField(max_length=30,default="None")
    absance = models.CharField(max_length=30,default="None")   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)


class salaire(models.Model):
    mois      = models.IntegerField()
    heurs_base= models.FloatField(default=0)
    heurs_sup = models.FloatField(default=0)
    primes    = models.FloatField(default=0)  
    total     = models.FloatField(default=0)   
    user    = models.ForeignKey(User, on_delete=models.CASCADE)

class mission(models.Model):
    description= models.CharField(max_length=30,default="None")
    date_debut = models.DateField(default="None")
    date_fin   = models.DateField(default="None")
    lieu       = models.CharField(max_length=30,default="None")   
    état       = models.CharField(max_length=30,default="None")   
    user       = models.ForeignKey(User, on_delete=models.SET_NULL , null=True)

