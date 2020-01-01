from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)
from user.choices import USER_TYPE_CHOICES

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
    user_type       = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)

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
    
