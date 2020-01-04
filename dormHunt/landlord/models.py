from django.db import models

from landlord.choices import PROPERTY_TYPE_CHOICES


# Create your models here.
class Properties(models.Model):
    property_name = models.CharField(max_length=60, blank=True),

