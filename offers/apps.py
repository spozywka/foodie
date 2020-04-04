from django.apps import AppConfig


class OffersConfig(AppConfig):
    name = 'offers'
    verbose_name = 'Offers'

    def ready(self):
        """
        Override this to put in:
        - Users system checks
        - Users signal registration
        """
