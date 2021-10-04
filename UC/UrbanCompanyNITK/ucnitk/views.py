from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView
)
from .models import *
from .forms import OrderForm

# Create your views here.

def index(request):
    return render(request, 'ucnitk/customer.html')

class customer(View):
    def get(self, request):
        services =  Service.objects.all()
        servicelist = {}
        servicetable = {}
        
        i = 1
        for service in services:
            servicelist.add(service.ServiceName)
            if i%3==0:
                servicetable.add(servicelist)
                servicelist.clear()  
            i+=1      
        return render(request, 'ucnitk/customer.html', {'servicetable':servicetable})


def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')

class service_provider(View):
    def get(self, request):
        context = {
            'orders': Order.objects.all()
        }
        return render(request, 'ucnitk/service_provider.html', context)

class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

