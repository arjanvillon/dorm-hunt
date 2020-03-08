from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from django_resized import ResizedImageField
import datetime

# NOTE I changed the the choices to picker
# from user.choices import USER_TYPE_CHOICES

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, user_type, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have an email")
        if not user_type:
            raise ValueError("Users must have a type")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            user_type = user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, user_type, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            user_type = user_type,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser):
    username        = models.CharField(max_length=15, unique=True)
    email           = models.EmailField(max_length=60, unique=True)
    user_type       = models.CharField(max_length=10)

    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'user_type']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name      = models.CharField(max_length=30, blank=True)
    last_name       = models.CharField(max_length=30, blank=True)
    number          = models.CharField(max_length=15, blank=True)
    birthday        = models.DateField(default=datetime.date.today)
    age             = models.IntegerField(default=0)
    emergency_name  = models.CharField(max_length=60, blank=True)
    emergency_phone = models.CharField(max_length=15, blank=True)
    picture         = ResizedImageField(size=[150,150], crop=['middle','center'], default='profile_pictures/default.png', upload_to='profile_pictures', blank=True)
    picture55       = ResizedImageField(size=[55,55], crop=['middle','center'], default='profile_pictures/default_55.png', upload_to='profile_pictures', blank=True)
    # picture         = models.ImageField(default='profile_pictures/default.png', upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("user:user_profile", kwargs={"pk": self.user.pk})

    def calculate_age(self):
        today = date.today()
        self.age = today.year - self.birthday.year
        self.save()


    

    