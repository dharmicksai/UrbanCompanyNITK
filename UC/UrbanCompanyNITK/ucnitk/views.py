from django.shortcuts import render
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'ucnitk/customer.html')

def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')

class service_provider(View):
    def get(self, request):
        return render(request, 'ucnitk/service_provider.html')
