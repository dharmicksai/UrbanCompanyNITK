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
class Order(models.Model):
    Customer = models.ForeignKey(User, related_name='Customer', on_delete=models.CASCADE)
    ServiceProvider = models.ForeignKey(User, related_name='ServiceProvider', on_delete=models.CASCADE)
    Price = models.IntegerField(default= 100)
    FromLocation = models.TextField()
    Description = models.TextField()
    QueuedTime = models.DateTimeField(default=timezone.now)
    AcceptedTime = models.DateTimeField(default=timezone.now)
    CompletedTime = models.DateTimeField(default=timezone.now)
    ServiceType = models.CharField(max_length=15, choices= SERVICE_CHOICES, default = 'Laundry')
    PreferredTime = models.CharField(max_length=15, choices= TIME_CHOICES, default = 'Anytime')
    Status = models.CharField(max_length=15, default = 'Not Accepted')
    rating=models.IntegerField(default=1)
    review=models.CharField(max_length=250,null=True,blank=True)
    
    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})




I_STATUS = (
    ('Resolved','Resolved'),
    ('Pending','Pending'),
)


I_TYPE = (
    ('Order Not being Accepted/Delivered','Order Not being Accepted/Delivered'),
    ('Issue With Service Provider','Issue With Service Provider'),
    ('Order Says Delivered but have not recieved anything','Order Says Delivered but have not recieved anything'),
    ('Other','Other')
)

class Help(models.Model):

    Customer = models.ForeignKey(User, related_name='Help_Customer', on_delete=models.CASCADE)
    OrderWh = models.ForeignKey(Order, related_name='Order_Wh', on_delete=models.CASCADE,default =1)
    I_Status = models.CharField(max_length=15, choices= I_STATUS, default = 'Pending')
    I_type = models.CharField(max_length=100, choices= I_TYPE, default = 'Other')
    I_details = models.CharField(max_length=100, default = 'Nothing')

class Images(models.Model):
    help = models.ForeignKey(Help,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='help/',null=True,blank=True)
