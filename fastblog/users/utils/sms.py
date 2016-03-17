from django.conf import settings
import requests


API_BASE_URL = "http://api.openapi.io/ppurio/{API_VERSION}/message/sms/{CLIENT_ID}/".format(
    API_VERSION=1,
    CLIENT_ID=settings.SMS_API_CLIENT_ID,
)


def send_sms(dest_phone, msg_body):
    response = requests.post(
        API_BASE_URL,
        data = {
            'send_phone': settings.SMS_API_SEND_PHONE,
            'dest_phone': dest_phone,
            'msg_body': msg_body,
        },
        headers={
            'x-waple-authorization': settings.SMS_API_AUTHORIZATION_KEY,
        }
    )

    return response
