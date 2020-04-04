from django.db import models

from common.utils import (
    get_default_price,
    get_default_product_name,
)


class Product(models.Model):
    offer = models.ForeignKey(
        'offers.Offer',
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(
        max_length=255,
        default=get_default_product_name,
    )
    price = models.IntegerField(
        default=get_default_price,
    )

    @classmethod
    def generate(cls):
        from random import choice
        from offers.models import Offer
        offer_ids = Offer.objects.values_list('id', flat=True)
        return Product.objects.create(
            offer_id=choice(offer_ids),
        )
