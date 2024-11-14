from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Customer
from .serializers import CustomerModelSerializer
# Create your views here.


class CustomersGenericViewSet(ModelViewSet):
    model = Customer
    permission_classes = [AllowAny]
    serializer_class = CustomerModelSerializer
    queryset = Customer.objects.all()
