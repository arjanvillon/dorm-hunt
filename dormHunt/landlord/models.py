import datetime
from django.utils.translation import gettext as _

from django.db import models
from user.models import User
from django.utils import timezone
from django.urls import reverse



from landlord.choices import PROPERTY_TYPE_CHOICES
from user.models import User

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

    deposit             = models.FloatField()
    price               = models.FloatField()
    thumbnail           = models.ImageField(default='property_thumbnails/default.png', upload_to='property_thumbnails')
    tagline             = models.CharField(max_length=40, null=True)
    description         = models.TextField(blank=True)
    
    favorite            = models.ManyToManyField(User, related_name='favorite', verbose_name='users that likes the property', blank=True)
    property_type       = models.CharField(max_length=30, blank=True)
    capacity            = models.IntegerField()
    bathroom            = models.IntegerField(default=0)

    # Features
    is_furnished        = models.BooleanField(default=False)
    is_pets_allowed     = models.BooleanField(default=False)

    # bath no
    # room type
    is_laundry          = models.BooleanField(default=False)
    is_parking          = models.BooleanField(default=False)
    is_storage          = models.BooleanField(default=False)
    is_air_conditioned  = models.BooleanField(default=False)
    is_ceiling_fans     = models.BooleanField(default=False)
    is_sink             = models.BooleanField(default=False)
    is_garbage_disposal = models.BooleanField(default=False)
    is_hardwood_floors  = models.BooleanField(default=False)
    is_internet         = models.BooleanField(default=False)
    is_microwave        = models.BooleanField(default=False)
    is_refrigerator     = models.BooleanField(default=False)
    is_stove            = models.BooleanField(default=False)
    is_telephone        = models.BooleanField(default=False)
    is_tile             = models.BooleanField(default=False)
    is_window_covering  = models.BooleanField(default=False)
    is_elevator         = models.BooleanField(default=False)

    terms_of_agreement  = models.TextField(blank=True)

    # Geopy
    latitude            = models.FloatField(null=True, blank=True)
    longitude           = models.FloatField(null=True, blank=True)
    created_at          = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landlord:landlord_home")

class Reminder(models.Model):
    property_name       = models.ForeignKey(Property, on_delete=models.CASCADE)
    category            = models.CharField(max_length=30)
    sub_category        = models.CharField(max_length=30, blank=True)
    issue               = models.CharField(max_length=80, blank=True)
    # gen info
    next_service        = models.DateField(_("Date"), default=datetime.date.today)
    days_before         = models.CharField(max_length=30)
    description         = models.TextField(blank=True)

class AddTenant(models.Model):
    # account_user        = models.ForeignKey(User, on_delete=models.CASCADE)
    account_user        = models.EmailField(max_length=60)
    dorm                = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_description    = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse('landlord:landlord_home')



    
    
