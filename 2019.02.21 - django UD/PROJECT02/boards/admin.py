from django.contrib import admin
from .models import Board

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at',)
    # 모든 컬럼을 admin에서 보기 -> boardAdmin에서 표시
admin.site.register(Board, BoardAdmin)  
    # 삭제하면 db에 적용되므로 id가 중복해서 생성되지 않음

