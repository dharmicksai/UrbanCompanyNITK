from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.urls.base import resolve
from .models import *
from .views import *
import json

# Create your tests here.
class TestUrls(TestCase):

    def test_urls(self):
        url = reverse('ucnitk')
        print(f'\nfound url for ucnitk')
        self.assertEquals(resolve(url).func.__name__, customer.as_view().__name__)
        print('url for ucnitk tested.')

        url = reverse('service-provider')
        print(f'\nfound url for service provider')
        self.assertEquals(resolve(url).func.view_class, service_provider)
        print('url for service-provider tested.')

        url = reverse('order-create')
        print(f'\nfound url for order-create')
        self.assertEquals(resolve(url).func.view_class, OrderCreateView)
        print('url for order-create tested.')

        url = reverse('order-detail', args=[1])
        print(f'\nfound url for order detail')
        self.assertEquals(resolve(url).func, order_detail)
        print('url for order detail tested.')

        url = reverse('review', args=[1])
        print(f'\nfound url for review')
        self.assertEquals(resolve(url).func, review)
        print('url for review tested.')

        url = reverse('your-orders')
        print(f'\nfound url for your-orders')
        self.assertEquals(resolve(url).func.view_class, your_orders)
        print('url for your-orders tested.')

        url = reverse('issues')
        print(f'\nfound url for issues')
        self.assertEquals(resolve(url).func.view_class, your_issues)
        print('url for issues tested.')

        url = reverse('view_review')
        print(f'\nfound url for view_review')
        self.assertEquals(resolve(url).func.view_class, view_review)
        print('url for view_review tested.')

#define next test
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.customer_url = reverse('ucnitk')
        
    def test_customer_GET(self):
        response = self.client.get(self.customer_url)
        print(f'\nGot response for home page view : {response}')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ucnitk/customer.html')
        print('Home page view tested')