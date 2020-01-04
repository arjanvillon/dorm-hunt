from django.db import models
from user.models import User
from django.utils import timezone
from django.urls import reverse



from landlord.choices import PROPERTY_TYPE_CHOICES


# Create your models here.
class Property(models.Model):
    owner       = models.ForeignKey(User, on_delete=models.CASCADE)
    name        = models.CharField(max_length=50)
    address     = models.TextField()
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
    
    
