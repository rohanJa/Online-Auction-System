# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    S = 's'
    B = 'b'
    user_choice =(
        (S,'seller'),
        (B,'buyer'),
        )
    bio = models.TextField(max_length = 500, blank =True)
    usertype = models.CharField(max_length = 30, choices = user_choice, default = B,)
    def __str__(self):
        return self.username
    
class Seller(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.username

class Buyer(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return self.user.username
