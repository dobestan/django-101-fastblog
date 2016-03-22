from celery import Task

import requests


class SendMessageTask(Task):

    def get_object(self, object_id):
        """
        메시지를 보낼 객체를 가져온다.
        """
        raise NotImplementedError

    def get_base_url(self, object_id):
        """
        BASE_URL을 가져온다.
        """
        raise NotImplementedError

    def get_data(self, object_id):
        """
        POST 로 넘길 데이터를 가져온다.
        """
        raise NotImplementedError

    def get_headers(self):
        """
        header에 담을 정보를 가져온다.
        """
        raise NotImplementedError

    def get_status_code(self, object_id, response):
        message_object = self.get_object(object_id)

        message_object.status_code = response.status_code
        message_object.save()
        return response.status_code

    def get_additional_response_content(self, object_id, response):
        pass

    def run(self, object_id):
        API_BASE_URL = self.get_base_url(object_id)


        response = requests.post(
            API_BASE_URL,
            data = self.get_data(object_id),
            headers= self.get_headers(),
        )

        # Response 저장하기
        self.get_status_code(
            object_id,
            response,
        )
        self.get_additional_response_content(
            object_id,
            response,
        )

        return response.content

    def get_response_content_dict(self, response_content):
        import json
        return json.loads(response_content)
