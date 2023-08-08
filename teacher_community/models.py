from django.db import models
from noticeboard.models import Post
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma

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

class Funding(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=100, decimal_places=0)  # 펀딩 금액을 나타내는 필드
    created_at = models.DateTimeField(default=timezone.now)

    def formatted_amount(self):
        return intcomma(self.amount)

    def __str__(self):
        return f"{self.title} - {self.formatted_amount()}원 ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"