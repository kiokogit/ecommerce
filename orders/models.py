from django.db import models

from customers.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    amount = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    

