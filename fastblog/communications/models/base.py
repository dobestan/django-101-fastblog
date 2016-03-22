from django.db import models


class MessageAbstractModel(models.Model):

    receiver = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    sender = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    content = models.TextField()

    status_code = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True

    def send_message(self):
        raise NotImplementedError
