from django.shortcuts import render
from .models import Movie, Director

def directors(request):
    context = {
        'logic': True,
        'Title': "Režiséři",
        'directors': Director.objects.all()
    }
    print(context)
    return render(request, 'directors.html', context)


def homepage(request):
    context = {
        "Title": "Filmy",
        "movies": Movie.objects.all()
    }

    return render(request, 'main.html', context)
