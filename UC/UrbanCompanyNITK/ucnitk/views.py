from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    CreateView
)
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

#for payments
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.views.decorators.csrf import csrf_exempt
import razorpay

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

class view_review(View):
    def get(self, request):
        user = request.user
        context = { 
            'reviews': Order.objects.filter(ServiceProvider=user).order_by('id')
        }
        return render(request, 'ucnitk/view_review.html', context)
def review(request,pk):
    if request.method == "POST":
         order = Order.objects.filter(id = pk)[0]
         order.rating=request.POST['rating']
         order.review=request.POST['review']
         
         order.save()
         return redirect('your-orders')
    else:
         order = Order.objects.filter(id=pk)[0]

         return render(request, 'ucnitk/review.html',{"pk":order.id})

# @login_required(login_url='/login/')
class accepted_orders(View):
    def get(self, request):
        user = request.user
        context = {
            'orders': Order.objects.filter(ServiceProvider = user).order_by('-QueuedTime')
        }
        return render(request, 'ucnitk/accepted_orders.html', context)

razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_ID, settings.RAZORPAY_ACCOUNT_ID)) #('rzp_test_A2y42To2vFRXP4', 'AgR6rEINvIAhEEU2aJn2RH6e'))
#class OrderDetailView(DetailView):
    #model = Order

@login_required
def order_detail(request, pk):
    order = Order.objects.filter(id = pk)[0]

    #creating razorpay order
    order_currency = 'INR'
    callback_url = 'http://'+ str(get_current_site(request))+"/handlerequest/"
    notes = {'order-type': order.ServiceType, 'description':order.Description}
    razorpay_order = razorpay_client.order.create(dict(amount=order.Price*100, currency=order_currency, notes = notes,  payment_capture='0'))
    order.razorpay_order_id = razorpay_order['id']
    order.save()

    context ={
        'order' : order,
        'object' : order
    }
    context['order_id'] = razorpay_order['id']
    context['final_price'] = order.Price
    context['razorpay_merchant_id'] = settings.RAZORPAY_ID
    context['callback_url'] = callback_url

    return render(request, 'ucnitk/order_detail.html', context)

@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            try:
                order = Order.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505 Not Found")
            order.razorpay_payment_id = payment_id
            order.razorpay_signature = signature
            order.save()
            result = razorpay_client.utility.verify_payment_signature(params_dict)

            if result==None:
                amount = order.Price*100
                try:
                    razorpay_client.payment.capture(payment_id, amount)
                    order.payment_status = 1
                    order.Status = 'Completed'
                    order.save()
                    return HttpResponse("Payment Successful")
                except:
                    order.payment_status = 2
                    order.save()
                    return HttpResponse("Payment Failed")
            else:
                order.payment_status = 2
                order.save()
                return HttpResponse("Payment Failed")
        except:
            return HttpResponse("505 not found")


class your_issues(View):
    def get(self, request):
        user = request.user
        context = {
            'issues': Help.objects.filter(Customer = user)
        }
        return render(request, 'ucnitk/help_issues.html',context)

class create_issue(View):
    def get(self, request):
        context = {
            'is_form' : HelpForm,
            'i_form' : ImageForm
        }
        return render(request, 'ucnitk/issue_new.html',context)

    def post(self, request):

        print(request.POST)
        helpObj = Help.objects.create(Customer = User.objects.get(id = int(request.POST['Customer'])))
        files = request.POST['file_field']

        for f in files:
            print("BRUH")
            Images.objects.create(help = helpObj,image=f)

        return redirect('issues')
        
        
        
        




class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm

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

    return redirect('/order/' + str(pk))

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

    return redirect('service-provider')

def finish_order(request, pk):
    order = Order.objects.filter(id = pk)[0]
    order.OrderFinishedTime = timezone.now()
    order.Status = 'Pending Payment'
    order.Price = request.POST['price']
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

    return redirect('/order/' + str(pk))

def delete_order(request, pk):
    order = Order.objects.filter(id=pk)[0]
    order.delete()
    return redirect('your-orders')

def confirm_cash_payment(request, pk):
    order = Order.objects.filter(id=pk)[0]
    order.payment_status = 3
    order.Status = 'Completed'
    order.save()
    return redirect('/order/' + str(pk))
