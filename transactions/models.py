from django.db import models

from common.utils import get_default_qty


class Transaction(models.Model):
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='products',
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='transactions',
    )
    qty = models.IntegerField(
        default=get_default_qty,
    )

    def save(self, *args, **kwargs):
        assert self.product.offer == self.order.offer
        return super(Transaction, self).save(*args, **kwargs)
