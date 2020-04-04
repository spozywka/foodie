from datetime import timedelta, datetime
from random import randrange, choice

import requests
from django.conf import settings
from django.utils.timezone import now


def get_default_offer_title() -> str:
    first_list = [
        "John's", "Ben's", "Farmer's", "Piotrek's",
        "Monika's", "Eliza's", "Rafal's", "Marcin's",
        "Ola's", "Martyna's", "Szymon's", "Kinga's"
    ]
    second_list = [
        'Good', 'Best', 'Cheap', 'Local', 'Fresh',
        'Quick', 'Instant', 'Calm', 'Big', 'Clean',
    ]
    third_list = [
        'Food', 'Berries', 'Salads', 'Meat',
        'Pork', 'Ham', 'Fruits', 'Candies',
    ]
    return f'{choice(first_list)} {choice(second_list)} {choice(third_list)}'


def get_default_distance() -> str:
    return f'{float(randrange(5, 75)) / 10} km from you'


def get_default_delivery_date() -> datetime:
    return now() + timedelta(days=randrange(1, 10))


def get_default_photo_url() -> str:
    response = requests.get(settings.PHOTO_API_URL)
    response.raise_for_status()
    return response.url


def get_default_product_name() -> str:
    first_list = [
        'Dark', 'Grey', 'Pink', 'Red', 'Blue',
        'Green', 'Spicy', 'Hot', 'Big', 'Small',
        'Light', 'Heavy', 'Straight', 'Curvy',
    ]
    second_list = [
        'Banana', 'Tuna', 'Salad', 'Apple',
        'Pork', 'Ham', 'Blueberry', 'Strawberry',
        'Veggies', 'Flour', 'Pepper', 'Salt',
    ]
    return f'{choice(first_list)} {choice(second_list)}'


def get_default_price() -> int:
    return randrange(3, 15)


def get_default_qty() -> int:
    return randrange(1, 10)
