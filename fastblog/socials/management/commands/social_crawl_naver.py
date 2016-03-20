from django.core.management import BaseCommand

from socials.models import Keyword, SocialPost

import requests
from bs4 import BeautifulSoup



class Command(BaseCommand):
    help = "Crawl posts from naver.com with provided keyword."

    def add_arguments(self, parser):
        parser.add_argument(
            "keyword",
            type=str,
        )

    def handle(self, *args, **options):
        keyword = options['keyword']
        pages = 10

        self.stdout.write(
            "{provider} 에서 '{keyword}' 크롤링을 시작합니다.".format(
                provider="네이버",
                keyword=keyword,
            )
        )

        keyword, created = Keyword.objects.get_or_create(
            name=keyword,
        )


        for page in range(1, pages+1):

            # 네이버의 경우에는 start 라는 parameter 를 이용해서 페이지를 구분한다.
            start = (page - 1) * 10 + 1

            BASE_URL = "https://search.naver.com/search.naver?where=post&query={keyword}&start={start}".format(
                keyword=keyword,
                start=start,
            )
            response = requests.get(BASE_URL)

            dom = BeautifulSoup(response.content, "html.parser")

            blog_post_elements = dom.select('li.sh_blog_top')

            for blog_post_element in blog_post_elements:
                title = blog_post_element.select('a.sh_blog_title')[0].attrs.get('title')
                url = blog_post_element.select('a.sh_blog_title')[0].attrs.get('href')

                social_post, created = keyword.social_post_set.get_or_create(
                    original_url=url,
                )

                if created:
                    social_post.title = title
                    social_post.save()

        self.stdout.write("{provider}에서 '{keyword}' 키워드로 {social_posts_count}개의 블로그글을 가져왔습니다.".format(
            provider="네이버",
            keyword=keyword.name,
            social_posts_count=keyword.social_post_set.count(),
        ))
