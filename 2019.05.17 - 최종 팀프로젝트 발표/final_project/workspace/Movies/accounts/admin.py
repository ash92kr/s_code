from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User

class ProfileAdmin(admin.ModelAdmin):
    list_display =['nickname', 'introduction',]
                    
admin.site.register(Profile, ProfileAdmin)

admin.site.register(User, UserAdmin)