# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.contrib import admin

# # Register your models here.


from django.contrib import admin
from .models import Product, P_History
# Register your models here.
admin.site.register(Product)
admin.site.register(P_History)
