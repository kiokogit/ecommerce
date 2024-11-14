from rest_framework import serializers
from orders.models import Order
from orders.utils import send_sms


class GenericOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
    
    
    def validate(self, attrs):
        return super().validate(attrs)

