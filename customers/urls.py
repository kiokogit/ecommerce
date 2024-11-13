from rest_framework import routers
from .views import CustometsGenericViewSet

router = routers.DefaultRouter()

router.register(" ", CustometsGenericViewSet, basename='customer-view')

urlpatterns = router.urls
