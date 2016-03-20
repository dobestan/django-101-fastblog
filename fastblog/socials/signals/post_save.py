from django.db.models.signals import post_save
from django.dispatch import receiver

from socials.models import Keyword


@receiver(post_save, sender=Keyword)
def post_save_keyword(sender, instance, created, **kwargs):
    if created:
        instance.crawl_all_providers()
