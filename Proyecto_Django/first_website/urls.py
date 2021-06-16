from django.urls import path
from . import views
from .models import Carreras

urlpatterns = [
    path('',views.index, name="Formula 1"),
    path('first_website/<id>',views.carreras,name="Carreras"),
]
