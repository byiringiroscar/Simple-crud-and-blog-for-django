from django.contrib import admin
from django.urls import path, include
from . import views

name = 'recloud'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('destinations', views.destinations, name='destinations'),
]