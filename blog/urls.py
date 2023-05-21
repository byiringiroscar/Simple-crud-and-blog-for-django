from django.urls import path, include
from .import views
name = 'blog'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]