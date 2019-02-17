from django.urls import path
from . import views   # 자신의 폴더에 있는 views를 부름

urlpatterns = [
    path('translated', views.translated, name='translated'),
    path('original/', views.original, name='original'),
    path('ascii_make/', views.ascii_make, name='ascii_make'),
    path('ascii_new/', views.ascii_new, name='ascii_new'),
    path('today/', views.today, name='today'),
    path('imagepick/', views.imagepick, name='imagepick'),
    path('graduation/', views.graduation, name='graduation'),
    path('bye/', views.bye, name='bye'),
    path('', views.index, name='index'),   # url 주소는 /utilities이고 뒤에 아무 것도 안 붙음
    ]



