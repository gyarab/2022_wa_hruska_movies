from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Director

# Create your views here.

def homepage(request):
    context = {
        "Title": "Films",
        "movies": Movie.objects.all()
    }
    return render(request, "main.html", context)

def directors(request):
    context = {
        "Title": "Moji režiséři",
        "directors": Director.objects.all()
    }
    return render(request, "directors.html", context)
