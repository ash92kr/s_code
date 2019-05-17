from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<int:movie_pk>/comments/<int:comment_pk>/edit/', views.comment_edit, name='comment_edit'),
    path('<int:movie_pk>/like/', views.like, name='like'),
    path('movielist/', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('<int:movie_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('', views.list, name='list'),
]