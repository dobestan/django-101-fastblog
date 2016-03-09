from django.core.urlresolvers import reverse
from django.test import TestCase


class FastblogViewTestCase(TestCase):

    def test_home_should_return_status_200(self):
        response = self.client.get(
            reverse("home")
        )

        self.assertEqual(
            response.status_code,
            200,
        )
