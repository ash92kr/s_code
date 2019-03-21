from django.urls import path
from . import views

app_name = 'votes'

urlpatterns = [
    path('<int:question_pk>/answers/<int:answer_pk>/delete/', views.answers_delete, name='answers_delete'),
    path('<int:question_pk>/answers/', views.answers_create, name='answers_create'),
    path('<int:question_pk>/edit/', views.edit, name='edit'),
    path('<int:question_pk>/delete/', views.delete, name='delete'),
    path('<int:question_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]