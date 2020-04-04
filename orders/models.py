from django.db import models

from common.utils import get_default_qty


class Order(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='orders',
    )
    offer = models.ForeignKey(
        'offers.Offer',
        on_delete=models.CASCADE,
        related_name='orders'
    )
    order_date = models.DateTimeField(
        auto_now_add=True,
    )
    qty = models.IntegerField(
        default=get_default_qty,
    )
