from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
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
        return render(request, 'ucnitk/customer.html')


def add_something(request):
    return render(request, 'ucnitk/add_something.html')

def order_service(request):
    return render(request, 'ucnitk/order_service.html')

class service_provider(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.all().exclude(Customer = user).filter(ServiceProvider = None, ServiceType=user.profile.service).order_by('-QueuedTime')
        }
        return render(request, 'ucnitk/service_provider.html', context)

# @login_required(login_url='/login/')
class your_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(Customer = user).order_by('-QueuedTime')
        }
        return render(request, 'ucnitk/your_orders.html', context)

# @login_required(login_url='/login/')
class accepted_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(ServiceProvider = user).order_by('-QueuedTime')
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
    
class reviewCreateView(LoginRequiredMixin, CreateView):
    model = review
    form_class = reviewForm

    def form_valid(self, form):
        form.instance.Customer = self.request.user
        return super().form_valid(form)

def accept_order(request , pk):
    order = Order.objects.filter(id = pk)[0]
    user = request.user
    order.ServiceProvider = user
    order.AcceptedTime = timezone.now()
    order.Status = 'Accepted'
    order.save()

    email_subject = 'Order for ' + order.ServiceType + " has been accepted by "+ user.username

    email_body = 'Hi ' +order.Customer.username + '\nOrder for ' + order.ServiceType + " has been accepted by "+ user.username
    email_body += '\nOrder Status : Accepted \nOrder Description: '+ order.Description

    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@semycolon.com',
        [order.Customer.email],
    )
    email.send(fail_silently=False)

    return redirect('accepted-orders')

def cancel_order(request, pk):
    order = Order.objects.filter(id = pk)[0]
    user = request.user
    order.ServiceProvider = None
    order.AcceptedTime = None
    order.Status = 'Not Accepted'
    order.save()

    email_subject = 'Order for ' + order.ServiceType + " has been Canceled by "+ user.username

    email_body = 'Hi ' +order.Customer.username + '\nWe are sorry to inform you that order for ' + order.ServiceType + " has been Canceled by "+ user.username
    email_body += '\nOrder Status : Not-Accepted \nOrder Description: '+ order.Description
    
    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@semycolon.com',
        [order.Customer.email],
    )
    email.send(fail_silently=False)

    return redirect('your-orders')

def finish_order(request, pk):
    order = Order.objects.filter(id = pk)[0]
    order.OrderFinishedTime = timezone.now()
    order.Status = 'Pending Payment'
    order.save()

    email_subject = 'Order for ' + order.ServiceType + " has been Finished by "+ request.user.username

    email_body = 'Hi ' +order.Customer.username + '\nOrder for ' + order.ServiceType + " has been Finished by "+ request.user.username
    email_body += '\nOrder Status : Awaiting Payment  \nOrder Description: '+ order.Description
    
    email = EmailMessage(
        email_subject,
        email_body,
        'noreply@semycolon.com',
        [order.Customer.email],
    )
    email.send(fail_silently=False)

    return redirect('accepted-orders')

def delete_order(request, pk):
    order = Order.objects.filter(id=pk)[0]
    order.delete()
    return redirect('your-orders')
