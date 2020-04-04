from rest_framework import routers

from .views import TransactionViewSet

router = routers.DefaultRouter()
router.register('', TransactionViewSet)
urlpatterns = router.urls
