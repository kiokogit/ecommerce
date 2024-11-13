from rest_framework import serializers
from orders.models import Order
from orders.utils import send_sms


class GenericOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):
        order = Order.objects.create(
            **validated_data
        )
        message = f'Your order for {order.item_name} has been received successfully. Please wait as we process'
        
        send_sms([order.customer.phone_number], message)
        return True, 'Success'
    

