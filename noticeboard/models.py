from django.db import models
from social.models import Teacher  # social 앱에서 Teacher 모델을 가져옴

class Post(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE)  # Teacher 모델을 외래키로 참조
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)  # 조회수 필드 추가

    def increase_views(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

class AttachedFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attached_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"File {self.file.name} attached to {self.post.title}"