from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    ServiceName = models.CharField(max_length=50, primary_key=True)
    MinPrice = models.IntegerField(default=5)

    def __str__(self):
        return self.ServiceName

class Order(models.Model):
    OrderId = models.IntegerField(primary_key=True)
    Customer = models.ForeignKey(User, related_name='Customer', on_delete=models.CASCADE)
    ServiceProvider = models.ForeignKey(User, null=True, blank=True, related_name='ServiceProvider', on_delete=models.CASCADE)
    Price = models.IntegerField()
    FromLocation = models.TextField()
    Description = models.TextField()
    QueuedTime = models.DateTimeField(default=timezone.now())
    AcceptedTime = models.DateTimeField(null=True)
    CanceledTime = models.DateTimeField(null=True)
    OrderFinishedTime = models.DateTimeField(null=True)
    CompletedTime = models.DateTimeField(null=True)
