from django.db import models

from common.utils import get_default_price


class Product(models.Model):
    offer = models.ForeignKey(
        'offers.Offer',
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(
        max_length=255,
        default='Product',
    )
    price = models.IntegerField(
        default=get_default_price,
    )
