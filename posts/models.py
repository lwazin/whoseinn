from django.utils.timezone import now
from users.models import CustomUser
from django.db import models
from django.utils import timezone

def upload_location(instance, filename):
    return "%s/%s" %(instance.post.user.username, filename)

class Accom(models.Model):
    # Location
    address = models.CharField(max_length=200, blank=True)
    province = models.CharField(max_length=200, blank=True)
    lng = models.FloatField(blank=True)
    lat = models.FloatField(blank=True)
    # Specifics
    type = models.SlugField(blank=True)
    gender = models.SlugField(default="Mixed")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    price =  models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    electricity = models.BooleanField(default=True)
    shuttle = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    # System
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cover = models.CharField(blank=True, max_length=200)
    slug = models.SlugField(unique=True)


class Image(models.Model):
    post = models.ForeignKey(Accom, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location)
    position = models.PositiveSmallIntegerField(default=0)

class Application(models.Model):
    status = models.SlugField(default='pending')
    viewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accom = models.ForeignKey(Accom, on_delete=models.CASCADE)

class InternalMessage(models.Model):
    viewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    accom = models.ForeignKey(Accom, on_delete=models.CASCADE)
    message = models.CharField(blank=True, max_length=200)
    direction = models.BooleanField(default=None)
