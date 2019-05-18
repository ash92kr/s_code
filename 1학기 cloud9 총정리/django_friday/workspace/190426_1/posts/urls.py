from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_pk>/like/', views.like, name='like'),
    path('<int:post_pk>/comment/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:post_pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.list, name='list'),
]