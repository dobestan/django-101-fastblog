from django.db import models


class SocialPost(models.Model):

    Keyword = models.ForeignKey(
        "Keyword"
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
