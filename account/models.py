from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/',default =True)
    name = models.CharField(max_length=10,blank=True)
    management = models.TextField(max_length=30,blank=True)
    team = models.CharField(max_length=5,blank=True)

    def __str__(self):
        return self.name