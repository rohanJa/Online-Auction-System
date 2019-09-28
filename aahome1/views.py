# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# # Create your views here.



from django.shortcuts import render,redirect
from .forms import ProductForm
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from .models import Product, P_History
import datetime
from datetime import timedelta
from django.utils import timezone
from django.db.models import F
from aform.models import Seller, Buyer, User
from decimal import Decimal
from django.db.models import Max


# Create your views here.
def present(request):
    yesterday = datetime.datetime.now() - timedelta(days=1)
    live = Product.objects.filter(start_date = datetime.date.today(), start_time__lte = timezone.now())
    for l in live:
        l.status = 'live'
        l.end_date = l.start_date
        l.end_date+=timedelta(days=1)
        l.end_time = l.start_time
        #l.end_time+=timedelta(days=1)
        l.save()
    
    live2 = Product.objects.filter(start_date = yesterday, start_time__gte = timezone.now())
    for l in live2:
        l.status = 'live'
        l.end_date = l.start_date
        l.end_date+=timedelta(days=1)
        l.end_time = l.start_time
        #l.end_time+=timedelta(days=1)
        l.save()
    return render(request,'running.html',{'live':live, 'live2': live2 })

def future(request):
    yesterday = datetime.datetime.now() - timedelta(days=1)
    count=0
    inc=1
    future2 = Product.objects.filter(status='future')
    future = Product.objects.exclude(status='future').filter(start_date = datetime.date.today(), start_time__gte = timezone.now())
    for f in future:
        f.status= 'future'
        f.save()
    return render(request,'future.html',{'future': future, 'future2': future2 })

def past(request):
    yesterday = datetime.datetime.now() - timedelta(days=1)
    past = Product.objects.filter(status='live', start_date = yesterday, start_time__lte = timezone.now())
    for p in past:
        p.status = 'past'
        p.save()
    past2 = Product.objects.filter(status = 'past')
    return render(request, 'past.html', {'past': past, 'past2': past2})
    
    
def home(request):
    t = timezone.now()
    #past = Product.objects.filter(start_date = yesterday, start_time__lte = timezone.now())
    now = datetime.datetime.now().strftime('%H:%M:%S')
    #now = timezone.now()
    return render(request,'auction.html', {'now': now })

@login_required
def bid(request,product_id):
    p = Product.objects.get(pk = product_id)
    try:
        bidder = Buyer.objects.get(user = request.user)
        p.bidded_time = timezone.now()
        p.current_bidder = bidder.user.username
        #p.current_price = p.price
        p.currnet_price = F('currnet_price')+ Decimal(100.00)
        #p.currnet_price = Decimal(amount)
        p.save()
        phist = P_History()
        phist.bidded_price = Decimal(100.00)
        phist.product=p
        phist.bidder_name= bidder.user.username
        phist.bidded_time= timezone.now()
        phist.save()
        return redirect('present')
    except:
        return redirect('login_view')

def history(request,product_id):
    p = Product.objects.get(pk = product_id)
    ph = P_History.objects.filter(product =p)
    return render(request, 'history.html', {'ph': ph })

def product_detail(request, product_id):
    p = Product.objects.get(pk = product_id)
    return render(request,'productDetail.html', {'product': p })

def main_page(request):
    return render(request,'auction.html',{})