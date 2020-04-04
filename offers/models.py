from django.db import models

from common.enums import Categories, Cities
from common.utils import (
    get_default_distance,
    get_default_photo_url,
    get_default_delivery_date,
)


class Offer(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='offers',
    )
    clients = models.ManyToManyField(
        'users.User',
        related_name='services',
    )
    title = models.CharField(
        max_length=255,
        default='Title',
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
