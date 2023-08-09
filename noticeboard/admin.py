from django.contrib import admin
from .models import Post, Comment, AttachedFile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'views')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'author__username')  # 'author__username'으로 Teacher 모델의 username 필드 검색

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('post__title', 'author__username')  # 'post__title', 'author__username'으로 검색

@admin.register(AttachedFile)
class AttachedFileAdmin(admin.ModelAdmin):
    list_display = ('post', 'file', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('post__title',)  # 'post__title'로 검색