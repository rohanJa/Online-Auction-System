# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.db import models

# # Create your models here.


from django.db import models
#from django.contrib.auth.models import User
from django.db.models import F
from django.conf import settings
from aform.models import Seller, Buyer, User
import datetime
from datetime import timedelta
from django.utils import timezone
from decimal import Decimal

# Create your models here.
class Product(models.Model):
    seller = models.ForeignKey(Seller)
    product_image = models.FileField(blank=True)
    name = models.CharField(max_length = 30)
    category = models.CharField(max_length = 30)
    desc = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    start_date = models.DateField(default = datetime.date.today)
    start_time = models.TimeField(default = timezone.now)
    duration = models.TimeField(default = datetime.time(2, 00))
    #end_time = models.TimeField(blank = True)
    current_bidder = models.CharField(max_length=30, null = True, blank = True)
    currnet_price = models.DecimalField(max_digits=8, decimal_places=2, default= 0.00)
    bidded_time = models.DateTimeField(null = True, blank = True)
    status = models.CharField(max_length=30, default = 'future')
    no_of_bids = models.IntegerField(null = True)
    #date_time= models.DateTimeField(default = datetime.datetime.today)
    end_date = models.DateField(default = datetime.date.today)
    end_time = models.TimeField(default = timezone.now)
    #bid_amount = models.DecimalField(max_digits = 10, decimal_places=2, default = 0.00)
    def __str__(self):
        return self.name
    
    
class P_History(models.Model):
    product = models.ForeignKey(Product)
    bidder_name = models.CharField(max_length= 30)
    bidded_time = models.TimeField(default= timezone.now)
    bidded_price =models.DecimalField(max_digits = 14, decimal_places=2, default=0.00)

    def __str__(self):
        return self.product.name
