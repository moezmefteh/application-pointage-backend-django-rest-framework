from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, PropertiesUserUpdate
from Auth import views
from django.conf.urls import url 

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    #path('update/',PropertiesUserUpdate.as_view()),
    url(r'^update/(?P<username>\w{0,50})/$', views.PropertiesUserUpdate),


]