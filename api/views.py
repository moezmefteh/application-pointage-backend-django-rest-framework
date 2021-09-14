from Auth.models import *
from Auth.serializers import *
from api.models import *
from api.serializers import *

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView,ListAPIView)

###############################################################################

class SalairesDefineAll(ListCreateAPIView):
        queryset =salaire.objects.all()
        serializer_class =salaireSerializer
        pagination_class = None
        salaire.objects

class SalaireRetrieve(ListAPIView):
    serializer_class =salaireSerializer
    def get_queryset(self):
        return salaire.objects.filter(user=self.kwargs.get('pk', None)) 

###############################################################################

class PointageDefineAll(ListCreateAPIView):
        queryset =pointage.objects.all()
        serializer_class =pointageSerializer
        pagination_class = None
        pointage.objects

class PointageRetrieve(ListAPIView):
    serializer_class =pointageSerializer
    def get_queryset(self):
        return pointage.objects.filter(user=self.kwargs.get('pk', None)) 


class PointageUpdate(RetrieveUpdateAPIView):
    serializer_class =pointageSerializer
    def get_queryset(self):
        return pointage.objects.filter(user=self.kwargs.get('pk1', None),date=self.kwargs.get('pk2', None)) 
        
###############################################################################

class MissionDefineAll(ListCreateAPIView):
        queryset =mission.objects.all()
        serializer_class =missionSerializer
        pagination_class = None
        mission.objects

class MissionRetrieve(ListAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        return mission.objects.filter(user=self.kwargs.get('pk', None)) 

        #################################

class MissionStarted(RetrieveUpdateAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        return mission.objects.filter(id=self.kwargs.get('pk', None))


class MissioFinished(RetrieveUpdateAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        return mission.objects.filter(id=self.kwargs.get('pk', None))


class MissioCanceled(RetrieveUpdateAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        return mission.objects.filter(id=self.kwargs.get('pk', None)) 

class MissioWaited(RetrieveUpdateAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        return mission.objects.filter(id=self.kwargs.get('pk', None)) 

###############################################################################
