from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movielist/', views.movie_list, name='movie_list'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:movie_pk>/comments/<int:comment_pk>/update/', views.comment_update, name='comment_update'),
    path('<int:movie_pk>/comments/', views.comment_create, name='comment_create'),
    # path('contact/', views.contact, name='contact'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    # path('detail/', views.detail, name='detail'),
    path('', views.list, name='list'),
]