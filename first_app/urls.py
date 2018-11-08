from django.urls import path
from first_app import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('help', views.showhelp, name='help')
]