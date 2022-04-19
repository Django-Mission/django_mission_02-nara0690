from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Faq(models.Model):
    question = models.TextField(verbose_name='질문')
    answer = models.TextField(verbose_name='답변', null=True, blank=True)
    nomal = '일반'
    auth = '계정'
    etc = '기타'
    category_choices = [
        (nomal, '일반'),
        (auth, '계정'),
        (etc, '기타'),
    ]
    category = models.CharField(
        max_length=3,
        choices=category_choices,
        default=nomal,
        verbose_name='카테고리'
    )
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name= 'writer', null=True, blank=True, verbose_name='생성자')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    last_modifier = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='last_modifier', null=True, blank=True, verbose_name='최종 수정자')
    modify_time = models.DateTimeField(verbose_name='최중 수정일시', auto_now_add=True)
