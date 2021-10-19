from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image


USERTYPE_CHOICES = (
    ('Customer','Customer'),
    ('ServiceProvider','ServiceProvider')
)

SERVICE_CHOICES = (
    ('Electrician','Electrician'),
    ('Cleaner','Cleaner'),
    ('Salon','Salon'),
    ('Laundry','Laundry'),
    ('Delivery','Delivery'),
    ('Plumber','Plumber'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype =  models.CharField(max_length=15, choices= USERTYPE_CHOICES, default = 'Customer')
    service = models.CharField(max_length=15, choices= SERVICE_CHOICES, default = 'Delivery')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(default = "Hello")

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

