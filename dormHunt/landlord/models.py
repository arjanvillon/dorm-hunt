from django.db import models
from user.models import User
from django.utils import timezone
from django.urls import reverse



from landlord.choices import PROPERTY_TYPE_CHOICES


# Create your models here.
class Property(models.Model):
    owner               = models.ForeignKey(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50)
    # Address
    house_number        = models.IntegerField(null=True)
    street              = models.CharField(max_length=50, null=True)
    barangay            = models.CharField(max_length=50, null=True)
    city                = models.CharField(max_length=50, null=True)
    zip_code            = models.CharField(max_length=5, null=True)
    address             = models.TextField(blank=True)

    capacity            = models.IntegerField()
    deposit             = models.FloatField()
    price               = models.FloatField()
    thumbnail           = models.ImageField(default='property_thumbnails/default.png', upload_to='property_thumbnails')
    description         = models.TextField(blank=True)

    # Features
    is_air_conditioned  = models.BooleanField(default=False)
    is_ceiling_fans     = models.BooleanField(default=False)
    is_sink             = models.BooleanField(default=False)
    is_garbage_disposal = models.BooleanField(default=False)
    is_hardwood_floors  = models.BooleanField(default=False)
    is_internet         = models.BooleanField(default=False)
    is_microwave        = models.BooleanField(default=False)
    is_refrigerator     = models.BooleanField(default=False)
    is_storage          = models.BooleanField(default=False)
    is_stove            = models.BooleanField(default=False)
    is_telephone        = models.BooleanField(default=False)
    is_tile             = models.BooleanField(default=False)
    is_window_covering  = models.BooleanField(default=False)
    is_laundry          = models.BooleanField(default=False)
    is_parking          = models.BooleanField(default=False)
    is_elevator         = models.BooleanField(default=False)
    is_furnished        = models.BooleanField(default=False)
    is_pets_allowed     = models.BooleanField(default=False)
    

    # Geopy
    latitude            = models.FloatField(null=True, blank=True)
    longitude           = models.FloatField(null=True, blank=True)
    created_at          = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landlord:landlord_home")
    
    
