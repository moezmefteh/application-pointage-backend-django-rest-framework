from .views import *
from django.urls import path



urlpatterns = [

    path('salaires/list/',SalairesDefineAll.as_view() ),
    path('salaires/<str:pk>/',SalaireRetrieve.as_view()), 

    path('pointages/list/',PointageDefineAll.as_view() ),
    path('pointages/<str:pk>/',PointageRetrieve.as_view()), 

    path('missions/list/',MissionDefineAll.as_view() ),
    path('missions/<str:pk>/',MissionRetrieve.as_view()), 
    # path('missions/<str:pk>/<str:pk>/',MissionUpdate.as_view()), 

    path('mission/<int:pk>/start/' ,MissionStarted.as_view()), 
    path('mission/<int:pk>/finish/',MissioFinished.as_view()), 
    path('mission/<int:pk>/cancel/',MissioCanceled.as_view()), 
    path('mission/<int:pk>/wait/',MissioWaited.as_view()), 

  

]