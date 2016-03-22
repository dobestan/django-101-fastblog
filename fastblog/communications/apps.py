from django.apps import AppConfig


class CommunicationsAppConfig(AppConfig):
    name = 'communications'

    def ready(self):
        from communications.signals.post_save import post_save_message
