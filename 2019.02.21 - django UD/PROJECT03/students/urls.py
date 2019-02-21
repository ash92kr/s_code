from django.urls import path
from . import views
# urls.py만 앞에 /가 붙었다고 가정하고 나머지는 /를 앞에 붙여야 한다

urlpatterns = [
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('', views.index, name='index'),
]
