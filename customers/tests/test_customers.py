import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlineshop.settings')
django.setup()


from django.test import TestCase
from customers.models import Customer
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


# the model
class CustomerTestCase(TestCase):
    def test_customer_creation(self):
        customer = Customer.objects.create(name='CustomerTest', code='001BC', phone_number='+254712312312')
        self.assertEqual(customer.name, 'CustomerTest')
        self.assertEqual(customer.code, '001BC')


# endpoints
class CustomerViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='CustomerTest', code='001BC', phone_number='+254712312312')
        self.url = '/api/customers/'
        self.client.credentials(HTTP_AUTHORIZATION='Bearer A_ACCESS_TOKEN')

    def test_create_customer(self):
        data = {'name': 'CustomerTest2', 'code': '002BC', 'phone_number': '+254700900900'}
        response = self.client.post(self.url, data=data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(),  2)
        self.assertEqual(Customer.objects.get(code='002BC').name, 'CustomerTest2')

    def test_customers_list(self):
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.customer.name)
    
        