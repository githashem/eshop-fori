# Generated by Django 3.2.3 on 2021-05-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_category', '0002_auto_20210530_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='عنوان در url'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=50, verbose_name='عنوان'),
        ),
    ]