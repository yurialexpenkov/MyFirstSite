# Generated by Django 3.2.3 on 2021-07-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0004_alter_news_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='comment',
        ),
        migrations.AddField(
            model_name='news',
            name='comment',
            field=models.ManyToManyField(default=None, null=True, related_name='news_comment', to='app_news.MyComment', verbose_name='Комментарий'),
        ),
    ]
