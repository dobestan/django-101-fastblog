from django.apps import AppConfig


class SocialsAppConfig(AppConfig):
    name = "socials"

    def ready(self):
        from socials.signals.post_save import post_save_keyword
