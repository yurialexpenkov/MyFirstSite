from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=16, blank=True, default='-')
    city = models.CharField(max_length=36, blank=True, default='-')
    verification_flag = models.BooleanField(default=False)
    count_of_news = models.IntegerField(verbose_name='Количество опубликованных новостей', default=0)

    class Meta:
        permissions = (
            ("verified_user", "верифицированный пользователь"),
        )


