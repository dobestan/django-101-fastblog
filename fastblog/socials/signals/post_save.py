from django.db.models.signals import post_save
from django.dispatch import receiver

from socials.models import Keyword
from socials.tasks import SocialsCrawlNaverTask


@receiver(post_save, sender=Keyword)
def post_save_keyword(sender, instance, created, **kwargs):
    if created:
        task = SocialsCrawlNaverTask()
        task.delay(instance.id)
