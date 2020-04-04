from rest_framework import routers

from .views import OfferViewSet

router = routers.DefaultRouter()
router.register('', OfferViewSet)
urlpatterns = router.urls
