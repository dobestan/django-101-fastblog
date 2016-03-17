from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phonenumber = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "회원 정보"
        verbose_name_plural = verbose_name
