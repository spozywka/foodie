from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response

from transactions.models import Transaction
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']

    def create(self, request, *args, **kwargs):
        """
        DRF is a bitch.
        Nested create has empty valid_data.
        """
        data = request.data
        assert data.get('offer_id') is not None
        assert data.get('user_id') is not None
        assert data.get('products') is not None
        assert isinstance(data.get('products'), list)
        products = data.pop('products')
        order = Order.objects.create(
            **data,
        )
        for product in products:
            assert product.get('product_id') is not None
            assert product.get('qty') is not None
            Transaction.objects.create(
                order=order,
                **product,
            )
        serializer = OrderSerializer(instance=order)
        return Response(
            data=serializer.data,
            status=status.HTTP_201_CREATED,
        )
