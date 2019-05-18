from django.contrib import admin
from .models import Musician

# Register your models here.
class MusicianAdmin(admin.ModelAdmin):
    list_display = ['pk', 'first_name', 'last_name',]
    
admin.site.register(Musician, MusicianAdmin)