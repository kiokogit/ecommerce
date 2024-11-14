from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from orders.utils import send_sms

from .models import Order
from .serializers import GenericOrderSerializer
# Create your views here.


class OrdersViewset(ModelViewSet):
    model = Order
    permission_classes = [AllowAny]
    serializer_class = GenericOrderSerializer
    queryset = Order.objects.all()
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({'details': serializer.errors}, 400)
        
        order = serializer.save()
        
        message = f'Your order for {order.item_name} has been received successfully. Please wait as we process'
        success, info = send_sms([order.customer.phone_number], message)
        if not success:
            return Response({'details': info}, 400)
        return Response(self.serializer_class(order).data, 201)
    
            
        
