from django.db import models
from django.contrib.auth.models import User



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
