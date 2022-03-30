from django.apps import AppConfig


class StackuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stackuser'

    def ready(self):
        import stackuser.signals
