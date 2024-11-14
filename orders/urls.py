from rest_framework import routers
from .views import OrdersViewset

router = routers.DefaultRouter()

router.register("", OrdersViewset, basename='orders')
urlpatterns = router.urls
