from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]