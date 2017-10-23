from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'project_name.apps.user'

    def ready(self):
        import project_name.apps.user.signals

