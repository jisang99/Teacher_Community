from django.db import models
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import intcomma

class Funding(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.DecimalField(max_digits=100, decimal_places=0)  # 펀딩 금액을 나타내는 필드
    created_at = models.DateTimeField(default=timezone.now)

    def formatted_amount(self):
        return intcomma(self.amount)

    def __str__(self):
        return f"{self.title} - {self.formatted_amount()}원 ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"