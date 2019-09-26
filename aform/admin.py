# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.contrib import admin

# # Register your models here.





from django.contrib import admin
from django.conf import settings
from .models import User, Seller, Buyer
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import AbstractUser

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Buyer)
admin.site.register(Seller)
