from django.db import models
from authe.models import Author



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
    category = models.CharField(max_length=50,choices=CHOICES,verbose_name='Категории')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default = None)
    phone = models.CharField(max_length=100, blank=True, verbose_name='Номер телефона')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Link(models.Model):
    link = models.CharField(max_length=500)
    post = models.ForeignKey(Post,related_name = 'post', verbose_name = 'Ссылки',on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    