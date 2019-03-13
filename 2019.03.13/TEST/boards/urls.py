from django.urls import path
from . import views

urlpatterns = [
    path('update/<int:id>/', views.update, name='update'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]