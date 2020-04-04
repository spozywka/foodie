from datetime import timedelta, datetime
from random import randrange

import requests
from django.conf import settings
from django.utils.timezone import now


def get_default_distance() -> str:
    return f'{float(randrange(5, 75)) / 10} km from you'


def get_default_delivery_date() -> datetime:
    return now() + timedelta(days=randrange(1, 10))


def get_default_photo_url() -> str:
    response = requests.get(settings.PHOTO_API_URL)
    response.raise_for_status()
    return response.url


def get_default_price() -> int:
    return randrange(3, 15)
