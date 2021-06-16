from django.shortcuts import render,HttpResponse
from .models import Carreras

def index(request):
    carreras = Carreras.objects.all()
    return render(request,"first_website/index.html", {"Carreras":carreras})

def carreras(request, id):
    carrera = Carreras.objects.get(id=id)
    return render(request,"first_website/carreras.html", {"Carrera":carrera})

# Create your views here.
