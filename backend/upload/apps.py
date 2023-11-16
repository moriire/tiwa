from django.apps import AppConfig

class UploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload'

    def ready(self) -> None:
        from . import signal
        return super().ready()
