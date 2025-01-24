from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie

# Create your views here.

def index (request):
    movies = Movie.objects.all()
    return render (request, 'index.html', {'movies' : movies})
    return HttpResponse("Holla ")
    pass