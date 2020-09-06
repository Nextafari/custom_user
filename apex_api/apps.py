from django.apps import AppConfig


class ApexApiConfig(AppConfig):
    name = 'apex_api'

    def ready(self):
        import apex_api.signals
