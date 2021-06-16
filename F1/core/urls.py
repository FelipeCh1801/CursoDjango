from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name="Inicio"),
    path('carreras/',views.carreras, name="Carreras"),
    path('pilotos/',views.pilotos, name="Pilotos"),
]