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
class Order(models.Model):
    Customer = models.ForeignKey(User,null = True, blank = True, related_name='Customer', on_delete=models.CASCADE)
    ServiceProvider = models.ForeignKey(User, null=True, blank=True, related_name='ServiceProvider', on_delete=models.CASCADE)
    Price = models.IntegerField(null = True)
    FromLocation = models.TextField()
    Description = models.TextField()
    QueuedTime = models.DateTimeField(auto_now_add=True)
    AcceptedTime = models.DateTimeField(null=True)
    CanceledTime = models.DateTimeField(null=True)
    OrderFinishedTime = models.DateTimeField(null=True)
    CompletedTime = models.DateTimeField(null=True)
    ServiceType = models.CharField(max_length=15, choices= SERVICE_CHOICES, default = 'Laundry')
    PreferredTime = models.CharField(max_length=15, choices= TIME_CHOICES, default = 'Anytime')
    
    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})