# Generated by Django 3.2 on 2021-04-27 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0013_auto_20210420_1201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislike_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like_count',
        ),
        migrations.AlterField(
            model_name='post',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Скидки'),
        ),
    ]
