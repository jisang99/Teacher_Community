from django.contrib import admin
from .models import MyWrite, MyReply

@admin.register(MyWrite)
class MyWriteAdmin(admin.ModelAdmin):
    list_display = ('post',)

@admin.register(MyReply)
class MyReplyAdmin(admin.ModelAdmin):
    list_display = ('comment',)