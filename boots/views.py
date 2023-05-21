from django.shortcuts import render
from django.urls import reverse_lazy
from . import models
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def index(request):
    return render(request, 'base.html')


def destinations(request):
    all_destination = models.Destination.objects.all()
    return render(request, 'base.html', {'destinations': all_destination})


def DestinationDetail(request):
    return render(request, 'destination_detail.html')


class DestinationDetailView(generic.DetailView):
    template_name = 'destination_detail.html'
    model = models.Destination
    context_object_name = 'destination'
