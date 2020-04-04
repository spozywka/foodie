from datetime import timedelta
from random import randrange

from django.db import models
from django.utils.timezone import now

from common.enums import Categories, Cities
from common.utils import get_default_distance, get_default_photo_url


class Offer(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='offers',
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
        default=get_default_distance(),
    )
    delivery_date = models.DateTimeField(
        default=now() + timedelta(days=randrange(1, 10))
    )
    photo_url = models.CharField(
        max_length=2048,
        default=get_default_photo_url(),
    )
