from .base import MessageAbstractModel


class Email(MessageAbstractModel):

    class Meta:
        verbose_name = '이메일'
        verbose_name_plural = verbose_name
