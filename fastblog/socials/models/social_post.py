from django.db import models


class SocialPost(models.Model):

    keyword = models.ForeignKey(
        "Keyword",
        related_name="social_post_set",
    )

    provider = models.CharField(
        max_length=20,
    )

    title = models.CharField(
        max_length=200,
    )

    original_url = models.URLField(
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.original_url
