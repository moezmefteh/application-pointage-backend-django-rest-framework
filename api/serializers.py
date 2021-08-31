from api.models import *
from rest_framework import serializers 

class pointageSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = pointage
        fields = ('id',
                  'entre',
                  'sortie',
                  'retard',
                  'absance',
                  'user'
                  )


class salaireSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = salaire
        fields = ('id',
                  'mois',
                  'heurs_base',
                  'heurs_sup',
                  'primes',
                  'total',
                  'user'
                  )

class missionSerializer(serializers.ModelSerializer):

    class Meta:
        model = mission
        fields = ('id',
                  'description',
                  'date_debut',
                  'date_fin',
                  'lieu',
                  'état',
                  'user'
                 )
