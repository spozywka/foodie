from rest_framework import serializers

from .models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'id',
            'user_id',
            'title',
            'description',
            'category',
            'city',
            'distance',
            'delivery_date',
            'photo_url',
        )
