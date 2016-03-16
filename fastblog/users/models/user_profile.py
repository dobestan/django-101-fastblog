from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
            user=instance,
        )
