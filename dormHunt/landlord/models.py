from django.db import models
from user.models import User
from django.utils import timezone
from django.urls import reverse



# Create your models here.
class Property(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    house_number= models.IntegerField(null=True)
    street      = models.CharField(max_length=50, null=True)
    barangay    = models.CharField(max_length=50, null=True)
    city        = models.CharField(max_length=50, null=True)
    zip_code    = models.CharField(max_length=5, null=True)
    address     = models.TextField(blank=True)
    capacity    = models.IntegerField()
    deposit     = models.FloatField()
    price       = models.FloatField()
    thumbnail   = models.ImageField(default='property_thumbnails/default.png', upload_to='property_thumbnails')
    latitude    = models.FloatField(null=True, blank=True)
    longitude   = models.FloatField(null=True, blank=True)
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landlord:landlord_home")
    
    