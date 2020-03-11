from datetime import date
import datetime
from django.utils.translation import gettext as _

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_resized import ResizedImageField



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
    thumbnail           = ResizedImageField(size=[1000,950], crop=['middle','center'], default='property_thumbnails/default.png', upload_to='property_thumbnails', blank=True)
    # thumbnail           = models.ImageField(default='property_thumbnails/default.png', upload_to='property_thumbnails')
    tagline             = models.CharField(max_length=40, null=True)
    description         = models.TextField(blank=True)
    
    favorite            = models.ManyToManyField(User, related_name='favorite', verbose_name='users that likes the property', blank=True)
    property_type       = models.CharField(max_length=30, blank=True)
    slots               = models.IntegerField(default=0)
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
    views               = models.IntegerField(default=0)
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

    def get_absolute_url(self):
        return reverse("landlord:landlord_messages")
    

class AddTenant(models.Model):
    account             = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    account_user        = models.EmailField(max_length=60, default='defatult@gmail.com')
    dorm                = models.ForeignKey(Property, on_delete=models.CASCADE)
    room_description    = models.CharField(max_length=80)
    is_inclusive        = models.CharField(max_length=80, default='Inclusive')
    
    wallet              = models.IntegerField(default=0)
    # rent
    balance             = models.IntegerField(default=0)
    is_paid             = models.BooleanField(default=True)
    date_paid           = models.DateField(default=datetime.date.today)

    # expenses
    expense_balance             = models.IntegerField(default=0)
    expense_is_paid             = models.BooleanField(default=True)
    expense_date_paid           = models.DateField(default=datetime.date.today)
    

    def __str__(self):
        return self.account_user

    def get_absolute_url(self):
        return reverse('landlord:landlord_home')

    # rent
    def paid(self, amount):
        # self.balance = self.balance - price
        self.expense_balance = self.expense_balance - amount
        
        if self.expense_balance <= 0:
            amount = self.expense_balance
            self.expense_balance = 0
            self.expense_is_paid = True
            self.balance = self.balance + amount
            if self.balance <= 0:
                self.is_paid = True
                self.wallet = (-1) * self.balance
                self.balance = 0
                
            self.date_paid = date.today()
        else:
            self.is_paid = False
        self.save()

    def unpaid(self, price):
        
        self.balance += price
        self.is_paid = False
        
        if self.wallet > 0:
            self.balance -= self.wallet
            if self.balance <= 0:
                self.wallet = (-1) * self.balance
                self.balance = 0
                self.is_paid = True
            else:
                self.wallet = 0

        self.save()
    
    # expenses
    def expense_paid(self, amount):
        self.expense_balance = self.expense_balance - amount
        print(self.expense_balance)
        if self.expense_balance <= 0:
            self.expense_is_paid = True
            self.expense_date_paid = date.today()
        else:
            self.expense_is_paid = False
            self.save()

    def expense_unpaid(self, amount):
        self.expense_is_paid = False
        self.expense_balance += amount
        self.save()


# SECTION ADD EXPENSES
class Expenses(models.Model):
    property_name       = models.ForeignKey(Property, on_delete=models.CASCADE)
    name                = models.CharField(max_length=50)
    amount              = models.IntegerField()
    repeat              = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("landlord:landlord_home")
    
class History(models.Model):
    tenant      = models.ForeignKey(User, on_delete=models.CASCADE)
    dorm        = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount      = models.IntegerField()
    date_paid   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tenant.username