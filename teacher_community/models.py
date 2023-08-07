from django.db import models
from noticeboard.models import Post

#메인페이지 hot게시물은 조회 수 높은 순
class HotWrite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # post 모델을 외래키로 참조
    views = models.PositiveIntegerField(default=0)  # 조회수를 저장하는 필드
    
    def __str__(self):
        return self.post.title
    

#최근게시물은 최신 시간
class NewWrite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post 모델을 외래키로 참조

    def __str__(self):
        return self.post.title

    class Meta:
        ordering = ['-post__created_at']  # created_at 필드를 기준으로 내림차순 정렬


#고민게시물은 최신 시간

class ThinkWrite(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post 모델을 외래키로 참조

    def __str__(self):
        return self.post.title

    class Meta:
        ordering = ['-post__created_at']  # created_at 필드를 기준으로 내림차순 정렬
