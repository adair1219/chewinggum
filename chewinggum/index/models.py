from django.db import models

# Create your models here.

class FirstPage(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    status = models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS, verbose_name='状态')
    img = models.ImageField(upload_to='static/img', verbose_name='个性图片')
    introduction = models.CharField(max_length=300, verbose_name='网站描述')
    category = models.CharField(max_length=15, verbose_name='分类名')

    class Meta:
        verbose_name = verbose_name_plural = '首页部分'

    def __str__(self):
        return '博客首页内容'

class SiteMap(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    status = models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS, verbose_name='状态')
    pv = models.PositiveIntegerField(default=1)
    follow = models.PositiveIntegerField(default=1)
    total = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = verbose_name_plural = '站长统计部分'

    def __str__(self):
        return '站长统计'

class FriLink(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )

    status = models.PositiveIntegerField(default=STATUS_NORMAL,
        choices=STATUS_ITEMS, verbose_name='状态')
    img = models.ImageField(upload_to='static/img', blank=True,verbose_name='友链图片')
    name = models.CharField(max_length=15, verbose_name='友链名称')
    link = models.URLField(verbose_name='友链链接')

    class Meta:
        verbose_name = verbose_name_plural = '友链部分'

    def __str__(self):
        return self.name
    



