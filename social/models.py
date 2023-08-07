from django.db import models
from noticeboard.models import Post
from noticeboard.models import Comment
from social.models import Teacher  

# Create your models here.
class Teacher(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    license = models.ImageField(upload_to='teacher_id_proofs/')

    def __str__(self):
        return self.username
    

#나중에 my_write, my_reply 만들기

class MyWrite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Teacher 모델을 외래키로 참조

class MyReply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
