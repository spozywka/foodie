from rest_framework import serializers

from transactions.models import Transaction
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

    def create(self, validated_data):
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for product in products:
            Transaction.objects.create(
                order=order,
                **product,
            )
        return order
