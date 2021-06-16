from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")

def carreras(request):
    return render(request, "core/carreras.html")

def pilotos(request):
    return render(request, "core/pilotos.html")