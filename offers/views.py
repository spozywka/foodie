from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Offer
from .serializers import OfferSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'city']
