from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.register(pointage)
admin.site.register(salaire)
admin.site.register(mission)