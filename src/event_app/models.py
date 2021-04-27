from django.db import models
from authe.models import Author
from django.contrib.postgres.fields import ArrayField

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    CHOICES = [
        ('1','Посмотреть'),
        ('2','Покушать'),
        ('3','Развлекательное'),
        ('4','Познавательное'),
        ('5','Активный отдых'),
        ('6','Что купить?')        
    ]
    sale = models.BooleanField(default=False,verbose_name='Скидки')
    category = models.CharField(max_length=50,choices=CHOICES,verbose_name='Категории')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default = None)
    phone = models.CharField(max_length=100, blank=True, verbose_name='Номер телефона')
    link_list = ArrayField(models.CharField(max_length=200), blank=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE,related_name='images')
    images = models.CharField(max_length=100, blank=True, verbose_name='Url картинок',null=True)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


    def __str__(self):
        return self.post.title