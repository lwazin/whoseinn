from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    name = models.CharField(default='Name Not Set', max_length=255)
    surname = models.CharField(default='Surame Not Set', max_length=255)
    phone = models.CharField(default='Phone Not Set', max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'name', 'surname']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    identity = models.CharField(max_length=13, default='xxxxxxxxxxxxx')
    pic = models.ImageField(default='default.png')
