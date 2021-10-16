from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Service(models.Model):
    ServiceName = models.CharField(max_length=50, primary_key=True)
    MinPrice = models.IntegerField(default=5)

    def __str__(self):
        return self.ServiceName

SERVICE_CHOICES = (
    ('Electrician','Electrician'),
    ('Cleaner','Cleaner'),
    ('Salon','Salon'),
    ('Laundry','Laundry'),
    ('Delivery','Delivery'),
    ('Plumber','Plumber'),
)

TIME_CHOICES = (
    ('Anytime','Anytime'),
    ('10AM-12PM','10AM-12PM'),
    ('2PM-5PM','2PM-5PM'),
    ('5PM-8PM','5PM-8PM'),
)
rate= (('1',1),
('2',2),
('3',3),
('4',4),
('5',5))

payment_status_choices = (
    (1, 'SUCCESS'),
    (2, 'FAILURE' ),
    (3, 'PENDING'),
)

class Order(models.Model):
    Customer = models.ForeignKey(User, related_name='Customer', on_delete=models.CASCADE)
    ServiceProvider = models.ForeignKey(User, related_name='ServiceProvider', on_delete=models.CASCADE, null=True, blank=True)
    Price = models.IntegerField(default= 100)
    FromLocation = models.TextField()
    Description = models.TextField()
    QueuedTime = models.DateTimeField(default=timezone.now)
    AcceptedTime = models.DateTimeField(default=timezone.now)
    CompletedTime = models.DateTimeField(default=timezone.now)
    ServiceType = models.CharField(max_length=15, choices= SERVICE_CHOICES, default = 'Laundry')
    PreferredTime = models.CharField(max_length=15, choices= TIME_CHOICES, default = 'Anytime')
    Status = models.CharField(max_length=15, default = 'Not Accepted')
    #Payment Fields
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})


class review(models.Model):
    Order.id= models.ForeignKey(Order, related_name='id', on_delete=models.CASCADE)
    Customer = models.ForeignKey(User, related_name='Review_Customer', on_delete=models.CASCADE)
    ServiceProvider = models.ForeignKey(User, related_name='Review_ServiceProvider', on_delete=models.CASCADE)
    ServiceType = models.CharField(max_length=15, choices= SERVICE_CHOICES, default = 'Laundry')
    rating=models.IntegerField(default=1)
    review=models.CharField(max_length=250)
    def get_absolute_url(self):
        return reverse('review', kwargs={'pk': self.pk,'cus_id':self.Customer_id,'ser_id':self.ServiceProvider_id})
