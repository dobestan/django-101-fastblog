from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(
        max_length=20,
    )
    content = models.TextField()

    is_public = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "포스트"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post",
            kwargs={
                "pk": self.id,
            }
        )
