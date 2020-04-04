from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'
    verbose_name = 'Products'

    def ready(self):
        """
        Override this to put in:
        - Users system checks
        - Users signal registration
        """
