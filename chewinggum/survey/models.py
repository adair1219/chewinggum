from django.db import models

# Create your models here.

class Question(models.Model):

    qs = models.CharField(max_length=50, verbose_name='问题')

    class Meta:
        verbose_name = verbose_name_plural = '问题'

    def __str__(self):
        return self.qs[: 10]

class Answer(models.Model):
    an = models.CharField(max_length=10, verbose_name='选项')
    qs = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        verbose_name = verbose_name_plural = '选项'
    
    def __str__(self):
        return self.an