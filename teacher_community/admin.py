from django.contrib import admin
from .models import Funding

# Register your models here.
from .models import Teacher, Post, Comment, AttachedFile

admin.site.register(Teacher)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AttachedFile)