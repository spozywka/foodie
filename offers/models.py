from django.db import models

from common.enums import Categories, Cities
from common.utils import (
    get_default_distance,
    get_default_photo_url,
    get_default_delivery_date,
    get_default_offer_title,
)


class Offer(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='offers',
    )
    title = models.CharField(
        max_length=255,
        default=get_default_offer_title,
    )
    description = models.CharField(
        max_length=1024,
        default='Description',
    )
    category = models.CharField(
        max_length=255,
        choices=[(e.value, e.value) for e in Categories],
        default=Categories.Food.value,
    )
    city = models.CharField(
        max_length=255,
        choices=[(e.value, e.value) for e in Cities],
        default=Cities.Warsaw.value,
    )
    distance = models.CharField(
        max_length=255,
        default=get_default_distance,
    )
    delivery_date = models.DateTimeField(
        default=get_default_delivery_date,
    )
    photo_url = models.CharField(
        max_length=2048,
        default=get_default_photo_url,
    )

    @classmethod
    def generate(cls):
        from random import choice
        from users.models import User
        user_ids = User.objects.values_list('id', flat=True)
        return Offer.objects.create(
            user_id=choice(user_ids),
            category=choice(list(Categories)).value,
            city=choice(list(Cities)).value,
        )
