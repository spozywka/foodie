from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
    verbose_name = 'Orders'

    def ready(self):
        """
        Override this to put in:
        - Users system checks
        - Users signal registration
        """
