from rest_framework import routers
from .views import CustomersGenericViewSet

router = routers.DefaultRouter()

router.register(r"", CustomersGenericViewSet, basename='customers')

urlpatterns = router.urls
