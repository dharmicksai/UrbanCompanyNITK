from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView
)
from .models import *
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'ucnitk/customer.html')

class customer(View):
    def get(self, request):
        # services =  Service.objects.all()
        # servicelist = {}
        # servicetable = {}
        
        # i = 1
        # for service in services:
        #     servicelist.add(service.ServiceName)
        #     if i%3==0:
        #         servicetable.add(servicelist)
        #         servicelist.clear()  
        #     i+=1      
        # return render(request, 'ucnitk/customer.html', {'servicetable':servicetable})
        return render(request, 'ucnitk/customer.html')


def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')

class service_provider(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.exclude(Customer = user).filter(ServiceProvider = None)
        }
        return render(request, 'ucnitk/service_provider.html', context)

# @login_required(login_url='/login/')
class your_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(Customer = user)
        }
        return render(request, 'ucnitk/your_orders.html', context)

# @login_required(login_url='/login/')
class accepted_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(ServiceProvider = user)
        }
        return render(request, 'ucnitk/accepted_orders.html', context)

class OrderDetailView(DetailView):
    model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm

    def form_valid(self, form):
        form.instance.Customer = self.request.user
        return super().form_valid(form)

# def create_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit = False)
#             instance.Customer = request.user
#             instance.save()
#             return redirect('your-orders')
#     else:
#         form = OrderForm()
#     return render(request , 'ucnitk/order_form.html' , {'form' : form})


# def order_detail_view(request , pk):
#     context = {
#         'order': Order.objects.filter(id = pk)[0]
#     }
#     return render(request, 'ucnitk/order_detail.html', context)

def accept_order(request , pk):
    order = Order.objects.filter(id = pk)[0]
    user = request.user
    order.ServiceProvider = user
    order.save()
    return redirect('accepted-orders')