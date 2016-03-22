from celery import Task

from communications.models import SMS

from django.conf import settings

from .base import SendMessageTask
import json


class SendSMSTask(SendMessageTask):

    def get_object(self, sms_id):
        sms = SMS.objects.get(pk=sms_id)
        return sms

    def get_base_url(self, sms_id):
        sms = self.get_object(sms_id)

        API_BASE_URL = "http://api.openapi.io/ppurio/{API_VERSION}/message/sms/{CLIENT_ID}/".format(
            API_VERSION=1,
            CLIENT_ID=settings.SMS_API_CLIENT_ID,
        )
        return API_BASE_URL

    def get_data(self, sms_id):
        sms = self.get_object(sms_id)
        data = {
            'send_phone': sms.sender or settings.SMS_API_SEND_PHONE,
            'dest_phone': sms.receiver,
            'msg_body': sms.content,
        }
        return data

    def get_headers(self):
        headers={
            'x-waple-authorization': settings.SMS_API_AUTHORIZATION_KEY,
        }
        return headers

    def get_status_code(self, object_id, response):
        """
        API Store 같은 경우에는 무조건 200 status_code 를 리턴하고,
        에러 메시지는 content의 result_code에 기록됩니다.

        response.content 는 str 타입의 json 데이터가 오기 때문에,
        python dictionary 로 변경해줘야 한다.
        """
        message_object = self.get_object(object_id)

        content_dict = self.get_response_content_dict(response.text)
        message_object.status_code = content_dict.get('result_code')
        message_object.save()
        return response.status_code

    def get_additional_response_content(self, object_id, response):
        """
        CMID라는 값을 저장하려고 합니다.
        """
        message_object = self.get_object(object_id)

        content_dict = self.get_response_content_dict(response.text)
        message_object.cmid = content_dict.get('cmid')
        message_object.save()
        return message_object.cmid
