from django.contrib import admin
# Register your models here.
from .models import Teacher, Post, Comment, AttachedFile

admin.site.register(Teacher)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AttachedFile)