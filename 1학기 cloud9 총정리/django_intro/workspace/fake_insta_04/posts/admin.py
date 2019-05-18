from django.contrib import admin
from .models import Post, Hashtag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Post, PostAdmin)

class HashtagAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Hashtag, HashtagAdmin)
