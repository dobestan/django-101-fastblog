from django.db import models
from django.core.urlresolvers import reverse

from users.models import User


class PostManager(models.Manager):

    def get_queryset(self):
        queryset = super(PostManager, self).get_queryset()
        return queryset.select_related(
            'user',
        )


class Post(models.Model):

    objects = PostManager()

    user = models.ForeignKey(
        User,
    )

    thumbnail_image = models.ImageField(
        blank=True,
        null=True,
    )

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

    def get_object_dict(self):
        return {
            "title": self.title,
            "content": self.content,
        }

    @property
    def comments(self):
        return self.comment_set.all()
