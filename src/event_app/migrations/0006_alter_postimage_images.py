# Generated by Django 3.2 on 2021-04-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_alter_postimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Url картинок'),
        ),
    ]
