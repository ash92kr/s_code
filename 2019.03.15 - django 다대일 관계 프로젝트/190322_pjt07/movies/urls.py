from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [
    path('<int:movie_pk>/scores/<int:score_pk>/delete/', views.comments_delete, name="comments_delete"),
    path('<int:movie_pk>/scores/new/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]