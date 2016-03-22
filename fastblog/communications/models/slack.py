from .base import MessageAbstractModel


class Slack(MessageAbstractModel):

    class Meta:
        verbose_name = 'Slack'
        verbose_name_plural = verbose_name
