
from rest_framework import serializers
from customers.models import Customer

class CustomerModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'
