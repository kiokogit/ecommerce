from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order
from .serializers import GenericOrderSerializer
# Create your views here.


class OrdersViewset(ModelViewSet):
    model = Order
    permission_classes = [IsAuthenticated]
    serializer_class = GenericOrderSerializer
    queryset = Order.objects.all()
    
    def perform_create(self, serializer):
        if not serializer.is_valid():
            return Response({'details': serializer.errors}, 400)
        
        success, info = serializer.save()
        if not success:
            return Response({'details': info})
        return Response({'details': 'Order placed successfully'}, 200)
    
            
        
