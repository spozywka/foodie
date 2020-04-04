from random import randrange

import requests
from django.conf import settings


def get_default_distance():
    return f'{float(randrange(5, 75)) / 10} km from you'


def get_default_photo_url():
    response = requests.get(settings.PHOTO_API_URL)
    response.raise_for_status()
    return response.url
