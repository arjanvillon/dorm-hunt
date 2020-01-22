from datetime import date
import datetime
from django.utils.translation import gettext as _

from django.db import models
from django.utils import timezone
from django.urls import reverse



from landlord.choices import PROPERTY_TYPE_CHOICES
from user.models import User

# Create your models here.
class Property(models.Model):

    owner               = models.ForeignKey(User, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50)
    # Address
    address             = models.CharField(max_length=255, blank=True)

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
    views               = models.IntegerField(null=True)
    # Geopy
    latitude            = models.FloatField(null=True, blank=True)
    longitude           = models.FloatField(null=True, blank=True)
    created_at          = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landlord:property_detail", kwargs={"pk": self.pk})

class Reminder(models.Model):
    property_name       = models.ForeignKey(Property, on_delete=models.CASCADE)
    category            = models.CharField(max_length=30)
    sub_category        = models.CharField(max_length=30, blank=True)
    issue               = models.CharField(max_length=80, blank=True)
    # gen info
    next_service        = models.DateField(_("Date"), default=datetime.date.today)
    description         = models.TextField(blank=True)

    def __str__(self):
        return self.issue
    

class AddTenant(models.Model):
    account             = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    account_user        = models.EmailField(max_length=60, default='defatult@gmail.com')
    dorm                = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_description    = models.CharField(max_length=80)

    balance             = models.IntegerField(null=True)
    is_paid             = models.BooleanField(default=False)
    date_paid           = models.DateField(null=True)

    def __str__(self):
        return self.account_user

    def get_absolute_url(self):
        return reverse('landlord:landlord_home')

    def paid(self):
        self.is_paid = True
        self.date_paid = date.today()
        self.save()

    
    
