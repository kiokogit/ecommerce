
from rest_framework import serializers
import re
from .models import Customer

class CustomerModelSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Customer
        fields = '__all__'
    
    
    def validate_phone_number(self, value):
        """
            Phone numbers must have country codes for SMS Africa's talking
        """
        try:
            if not re.match(r"^\+\d{1,3}\d{3,}$", value):
                raise serializers.ValidationError('Phone number is invalid. Update with the format +2547xxxxxx')
        except ValueError:
            raise serializers.ValidationError('Add a phone number')
        return value
    
    # def create(self, validated_data):
    #     return Customer.objects.create(**validated_data)
