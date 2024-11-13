from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerModelSerializer
# Create your views here.


class CustometsGenericViewSet(ModelViewSet):
    model = Customer
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerModelSerializer
    queryset = Customer.objects.all()
