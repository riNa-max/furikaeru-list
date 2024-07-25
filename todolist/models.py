from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoStatus(models.Model):
    name=models.CharField(
        max_length=30,
        blank=False,
        null=False,
        unique=True
    )
    def __str__(self):
        return self.name

class TodoList(models.Model):
    title=models.CharField('タイトル',max_length=100)
    memo=models.TextField('内容')
    duedate=models.DateField('〆切')
    created_at=models.DateField('登録日時',auto_now_add=True)
    status=models.ForeignKey(TodoStatus,on_delete=models.CASCADE,verbose_name="処理状況")
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

