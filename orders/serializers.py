from rest_framework import serializers

from offers.serializers import OfferSerializer
from transactions.serializers import TransactionSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = TransactionSerializer(many=True)
    delivery_date = serializers.DateTimeField(source='offer.delivery_date')
    total = serializers.SerializerMethodField()
    offer = OfferSerializer(read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user_id',
            'offer_id',
            'order_date',
            'products',
            'delivery_date',
            'total',
            'offer',
        )

    @staticmethod
    def get_total(obj):
        return obj.total
