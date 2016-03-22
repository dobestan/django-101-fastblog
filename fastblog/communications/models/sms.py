from django.db import models

from .base import MessageAbstractModel


class SMS(MessageAbstractModel):

    cmid = models.TextField()

    class Meta:
        verbose_name = 'SMS'
        verbose_name_plural = verbose_name

    def send_message(self, async=True):
        from communications.tasks.sms import SendSMSTask
        task = SendSMSTask()

        if async:
            return task.delay(self.id)
        return task.run(self.id)
