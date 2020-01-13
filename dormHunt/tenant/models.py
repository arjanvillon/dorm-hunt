from django.db import models
from django.urls import reverse
from django.utils import timezone
from user.models import User
from landlord.models import Property

# Create your models here.

class Application(models.Model):
    tenant          = models.ForeignKey(User, on_delete=models.CASCADE)
    move_in_date    = models.DateField(null=True, blank=True)
    bio             = models.TextField()
    
    dorm            = models.ForeignKey(Property, on_delete=models.CASCADE)
    is_approved     = models.BooleanField(default=False)
    is_disapproved  = models.BooleanField(default=False)

    created_at      = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tenant

    def get_absolute_url(self):
        return reverse("tenant:tenant")

    def approve(self):
        self.is_approved = True
        self.save()

    def disapprove(self):
        self.is_disapproved = True
        self.save()