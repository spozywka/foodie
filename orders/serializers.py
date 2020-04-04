from rest_framework import serializers

from transactions.serializers import TransactionSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    products = TransactionSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'user_id',
            'offer_id',
            'order_date',
            'products',
        )
