from django.db import models


class Keyword(models.Model):

    name = models.CharField(
        max_length=20,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def crawl_all_providers(self):
        self.crawl_naver()
        self.crawl_daum()

    def crawl_naver(self):
        import requests
        from bs4 import BeautifulSoup

        pages = 10

        for page in range(1, pages+1):
            # 네이버의 경우에는 start 라는 parameter 를 이용해서 페이지를 구분한다.
            start = (page - 1) * 10 + 1

            BASE_URL = "https://search.naver.com/search.naver?where=post&query={keyword}&start={start}".format(
                keyword=self.name,
                start=start,
            )
            response = requests.get(BASE_URL)

            dom = BeautifulSoup(response.content, "html.parser")

            blog_post_elements = dom.select('li.sh_blog_top')

            for blog_post_element in blog_post_elements:
                title = blog_post_element.select('a.sh_blog_title')[0].attrs.get('title')
                url = blog_post_element.select('a.sh_blog_title')[0].attrs.get('href')

                social_post, created = self.social_post_set.get_or_create(
                    original_url=url,
                )

                if created:
                    social_post.title = title
                    social_post.save()

    def crawl_daum(self):
        pass
