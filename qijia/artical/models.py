from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '分类'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签名')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = verbose_name_plural = '标签'
    
    def __str__(self):
        return self.name

class Artical(models.Model):
    title = models.CharField(max_length=20, verbose_name='文章标题')
    desc = models.CharField(max_length=50, blank=True, verbose_name='文章描述')
    text = models.TextField(default='', verbose_name='文本')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    pv = models.PositiveIntegerField(default=1, verbose_name='点击量')
    uv = models.PositiveIntegerField(default=1, verbose_name='浏览量')
    
    class Meta:
        verbose_name = verbose_name_plural = '文章'
        ordering = ['-id']

    def __str__(self):
        return self.title 




