from django.contrib import admin
from django.urls import path, include
from . import views

name = 'boots'

urlpatterns = [
    path('', views.destinations, name='destinations'),
    path('destination_detail/', views.DestinationDetail, name='DestinationDetail'),
    path('destination/<int:pk>', views.DestinationDetailView.as_view(), name='destination_detail'),


]