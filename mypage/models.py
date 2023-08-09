from django.db import models
from noticeboard.models import Post, Comment  # noticeboard 앱에서 Post와 Comment 모델을 가져옴

class MyWrite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class MyReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)