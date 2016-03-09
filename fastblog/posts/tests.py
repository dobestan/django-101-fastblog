from django.core.urlresolvers import reverse
from django.test import TestCase


class PostViewTestCase(TestCase):

    def test_posts_should_return_status_200(self):
        response = self.client.get(
            reverse("posts")
        )

        self.assertEqual(
            response.status_code,
            200,
        )
