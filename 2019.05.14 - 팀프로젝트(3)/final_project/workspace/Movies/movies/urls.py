from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('', views.list, name='list'),
]