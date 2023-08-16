from django.db import models
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    license = models.ImageField(upload_to='teacher_id_proofs/')

    def __str__(self):
        return self.username
    

class Post(models.Model):
    author = models.ForeignKey(Teacher, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)  # 조회수 필드 추가
    category = models.CharField(max_length=10)
    file = models.FileField(upload_to='post_files/', blank=True, null=True)  # 파일 첨부 필드


    def increase_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']  # 최신 글이 먼저 오도록 정렬

    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
    author = models.ForeignKey(Teacher, related_name='comment_author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    

class AttachedFile(models.Model):
    post = models.ForeignKey(Post, related_name='AttachedFile_post', on_delete=models.CASCADE)
    file = models.FileField(upload_to='attached_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File {self.file.name} attached to {self.post.title}"