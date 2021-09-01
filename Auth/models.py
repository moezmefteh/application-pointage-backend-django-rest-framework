from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    cin     = models.IntegerField()
    username= models.CharField(max_length=30,primary_key=True)   
    password= models.CharField(max_length=255)   
    codeQR  = models.CharField(max_length=255)
    poste   = models.CharField(max_length=30)
    image   = models.CharField(max_length=255,default="not saved")
    email   = models.EmailField()
    telephone= models.IntegerField()
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
