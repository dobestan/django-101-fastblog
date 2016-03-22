from django.core.management import BaseCommand

from socials.models import Keyword, SocialPost




class Command(BaseCommand):
    help = "Crawl posts from naver.com with provided keyword."

    def add_arguments(self, parser):
        parser.add_argument(
            "keyword",
            type=str,
        )

    def handle(self, *args, **options):
        keyword = options['keyword']

        self.stdout.write(
            "{provider} 에서 '{keyword}' 크롤링이 자동으로 시작됩니다.".format(
                provider="네이버",
                keyword=keyword,
            )
        )

        keyword, created = Keyword.objects.get_or_create(
            name=keyword,
        )

        # keyword.crawl_all_providers()
