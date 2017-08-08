from django.db import models
# from django.contrib.auth.models import AbstractUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return self.username

class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y/%m')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


# tag（标签）
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=50, verbose_name='文章描述')
    content = models.TextField(verbose_name='文章内容')
    # click_count = models.IntegerField(default=0, verbose_name='点击次数')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')


    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __str__(self):
        return self.title