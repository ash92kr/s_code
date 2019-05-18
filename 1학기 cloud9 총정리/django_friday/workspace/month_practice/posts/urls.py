from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('', views.list, name='list'),
]