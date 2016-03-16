from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        primary_key=True,
        unique=True,
        related_name='user_profile',

    )

    phonenumber = models.CharField(
        max_length=16,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user.__str__()


def post_save_user(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
            user=instance,
        )


post_save.connect(post_save_user, sender=User)
