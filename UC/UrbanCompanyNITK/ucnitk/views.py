from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'ucnitk/customer.html')

def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')
