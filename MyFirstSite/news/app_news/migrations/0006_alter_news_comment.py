# Generated by Django 3.2.3 on 2021-07-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0005_auto_20210717_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='comment',
            field=models.ManyToManyField(to='app_news.MyComment', verbose_name='Комментарий'),
        ),
    ]
