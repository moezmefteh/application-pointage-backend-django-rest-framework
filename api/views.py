from Auth.models import *
from Auth.serializers import *
from api.models import *
from api.serializers import *

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateAPIView)

###############################################################################

class SalairesDefineAll(ListCreateAPIView):
        queryset =salaire.objects.all()
        serializer_class =salaireSerializer
        pagination_class = None
        salaire.objects

class SalaireRetrieve(ListCreateAPIView):
    serializer_class =salaireSerializer
    def get_queryset(self):
        return salaire.objects.filter(user=self.kwargs.get('pk', None)) 

###############################################################################

class PointageDefineAll(ListCreateAPIView):
        queryset =pointage.objects.all()
        serializer_class =pointageSerializer
        pagination_class = None
        pointage.objects

class PointageRetrieve(ListCreateAPIView):
    serializer_class =pointageSerializer
    def get_queryset(self):
        return pointage.objects.filter(user=self.kwargs.get('pk', None)) 

###############################################################################

class MissionDefineAll(ListCreateAPIView):
        queryset =mission.objects.all()
        serializer_class =missionSerializer
        pagination_class = None
        mission.objects

class MissionRetrieve(ListCreateAPIView):
    serializer_class =missionSerializer
    def get_queryset(self):
        user = self.request.user
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
