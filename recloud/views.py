from django.shortcuts import render, HttpResponse
from . import models


# Create your views here.

def index(request):
    return render(request, 'html/index.html')


def about(request):
    return render(request, 'html/about.html')


def destinations(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'html/destinations.html', {'destination': all_destinations})
