from django.apps import AppConfig


class QnaConfig(AppConfig):
    name = 'QnA'
    def ready(self):
        import QnA.signals
 