from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.list, name='list'),
    path('new/', views.create, name='create'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/edit/', views.update, name='update'),
    path('<int:article_id>/comments/new/', views.comment_create, name='comment_create'),
    path('<int:article_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]
