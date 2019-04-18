from django.contrib import admin
from .models import Post, Image

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['content',]
admin.site.register(Post, PostAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ['file', 'post_id',]
admin.site.register(Image, ImageAdmin)