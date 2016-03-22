from celery import Task

from socials.models import Keyword


class SocialsCrawlNaverTask(Task):

    def run(self, keyword_id):
        keyword = Keyword.objects.get(pk=keyword_id)
        keyword.crawl_all_providers()
