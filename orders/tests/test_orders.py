import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop.settings')
django.setup()


from django.test import TestCase
from orders.models import Order
from customers.models import Customer
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from unittest.mock import patch



# models
class OrderTestCase(TestCase):
    def test_order_creation(self):
        customer = Customer.objects.create(name='CustomerTest', code='001BC', phone_number='+254712312312')
        order = Order.objects.create(customer=customer, item_name='ItemTest', amount=100.00)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.item_name, 'ItemTest')
        self.assertEqual(order.amount,  100.00)
        
        
# endpoints
class OrdersViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='CustomerTest', code='001BC', phone_number='+254712312312')
        self.order = Order.objects.create(customer=self.customer, item_name='Item1', amount=100.00)
        self.url = '/api/orders/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer A_ACCESS_TOKEN')

    @patch('orders.utils.send_sms')
    def test_create_order(self):
        data = {'customer': self.customer.id, 'item_name': 'Item2', 'amount': 200}
        response = self.client.post(self.url, data=data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(),  2)
        self.assertEqual(Order.objects.get(item_name='Item2').amount,  200)

    def test_orders_list(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.order.item_name)
        
