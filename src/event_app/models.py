from django.db import models
from authe.models import Author

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория')


class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    CHOICES = [
        ('ON','Один'),
        ('TW','Два'),
        ('TH','Три'),
        ('FR','Четыре'),
        ('FV','Пять')
    ]
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, default = None)
    link = models.URLField(
        _("Link"), 
        max_length=128, 
        db_index=True, 
        unique=True, 
        blank=True
    )
    phone = models.CharField(max_length=100, blank=True, verbose_name='Номер телефона')
    rate = models.CharField(max_length=50,choices=CHOICES)


class Author_client(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    CHOICES = [
        ('CL','Клиент'),
    ]
    type = models.CharField(max_length=50,choices=CHOICES)
    

class Comment(models.Model):
    body = models.TextField(verbose_name='Тело')
    author = models.ForeignKey(Author_client, on_delete=models.CASCADE)
    CHOICES = [
        ('ON','Один'),
        ('TW','Два'),
        ('TH','Три'),
        ('FR','Четыре'),
        ('FV','Пять')
    ]
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    rate = models.CharField(max_length=50,choices=CHOICES)
