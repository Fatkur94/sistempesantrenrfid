from django.apps import AppConfig


class SantriConfig(AppConfig):
    name = 'santri'

    def ready(self):
        import santri.signals