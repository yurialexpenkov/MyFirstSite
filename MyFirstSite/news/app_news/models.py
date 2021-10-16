from django.contrib.auth.models import User
from django.db import models

# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)

class News(models.Model):

    STATUS_CHOICES = [
        ('a', 'True'),
        ('n', 'False'),
          ]
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.CharField(max_length=1000, verbose_name='Содержание')
    date = models.DateTimeField(verbose_name='Дата создания новости')
    activity = models.BooleanField(verbose_name='Флаг верификации', default=False)
    status_verifications = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name_plural = 'News'
        verbose_name = 'Новости'
        permissions = (
            ("can_publish", "может публиковать"),
        )


class MyComment(models.Model):
    user_name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    comment_text = models.CharField(max_length=200, verbose_name='Текст комментария')
    news = models.ForeignKey('News', default=None, null=True, on_delete=models.CASCADE,
                             related_name='mycomment_news', verbose_name='Новость')
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')


    def trim15(self):
        if len(self.comment_text)<=15:
            return self.comment_text
        else:
            return u"%s..." % (self.comment_text[:15],)

    trim15.short_description = "Текст комментария"


    def __str__(self):
        return self.comment_text













