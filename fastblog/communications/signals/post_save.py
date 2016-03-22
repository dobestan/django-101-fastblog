from django.db.models.signals import post_save
from django.dispatch import receiver

from communications.models import SMS, Email, Slack


@receiver(post_save, sender=SMS)
@receiver(post_save, sender=Email)
@receiver(post_save, sender=Slack)
def post_save_message(sender, instance, created, **kwargs):
    if created:
        instance.send_message()
