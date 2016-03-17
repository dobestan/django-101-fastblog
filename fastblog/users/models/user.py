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

    def send_signup_greeting_sms(self):
        from users.utils.sms import send_sms

        if self.phonenumber:
            send_sms(
                self.phonenumber,
                "{username}님, 회원가입을 진심으로 축하드립니다.".format(
                    username=self.username,
                ),
            )
