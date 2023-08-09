from django.db import models

class Post(models.Model):
    author  = models.ForeignKey('social.Teacher', on_delete=models.CASCADE,related_name='noticeboard_posts')  # 'social.Teacher' 형식으로 가져오기
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
    
    class Meta:
        ordering = ['-created_at']  # 최신 글이 먼저 오도록 정렬
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author =  models.ForeignKey('social.Teacher', on_delete=models.CASCADE, related_name='noticeboard_comments')  # 'social.Teacher' 형식으로 가져오기
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