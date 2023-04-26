from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# Create your models here.
class Passwords(models.Model):
    username = models.CharField(max_length=50, blank=False)
    website =  models.URLField(blank=False)
    password = models.CharField(blank=False, max_length=100)
    creater = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.website
