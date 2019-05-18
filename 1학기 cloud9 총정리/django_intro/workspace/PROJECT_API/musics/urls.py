from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

urlpatterns = [
    path('musics/<int:music_pk>/comments/<int:comment_pk>/', views.comment_update_and_delete),
    path('musics/<int:music_pk>/comments/', views.comment_create),
    path('artists/<int:artist_pk>/', views.artist_detail),
    path('artists/', views.artist_list),
    path('docs/', get_swagger_view(title="Api Docs")),
    path('musics/<int:music_pk>/', views.music_detail),
    path('musics/', views.music_list),
]