
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #rota , view responsavel, nome de referencia
    path('home/', views.home, name='home' )
]
