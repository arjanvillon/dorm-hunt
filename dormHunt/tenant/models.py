from django.db import models
from user.models import User
from landlord.models import Property

# Create your models here.

class Application(models.Model):
    tenant          = models.ForeignKey(User, on_delete=models.CASCADE)
    move_in_date    = models.DateField(null=True, blank=True)
    bio             = models.TextField()
    
    dorm            = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return self.tenant.username
    


