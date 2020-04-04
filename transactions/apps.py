from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    name = 'transactions'
    verbose_name = 'Transactions'

    def ready(self):
        """
        Override this to put in:
        - Users system checks
        - Users signal registration
        """
