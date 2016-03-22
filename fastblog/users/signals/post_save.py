from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User

from communications.models import SMS


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        # instance.send_signup_greeting_sms()
        SMS.objects.create(
            receiver=instance.phonenumber,
            content="{username}님, 회원가입을 축하드립니다.".format(
                username=instance.username,
            )
        )
