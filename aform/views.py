# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# # Create your views here.


from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.http import HttpResponse, Http404
from .forms import SignUpForm, UserLoginForm
from .models import Seller, Buyer
from aahome1.forms import ProductForm, SearchForm
from aahome1.models import Product
from django.db.models import F
from datetime import timedelta
from django.utils import timezone
import datetime
from onlineAuction import settings

# Create your views here.
def signup(request):
    # print(vars(request))
    print("request method is "+str(request.method))
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # print("Form is valid "+str(form.is_valid()))
        if form.is_valid():
            user = form.save()
            user.is_active = True
            if user.usertype == 'b':
                buyer = Buyer()
                buyer.user = user
                buyer.save()
                print("I am a "+str(user.usertype))
            else:
                seller = Seller()
                seller.user = user
                seller.save()
                print("I am a "+str(user.usertype))
            return HttpResponse('added')
        else:
            raise Http404('error')
    else:
        form= SignUpForm()
    return render(request, 'aform/signup.html', {'form': form })

def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username= username, password = password)
        login(request,user)
        print(request.user.is_authenticated())
        if user.usertype == 's':
            return redirect('view_adv')
        else:
            return redirect('home')
    return render(request, 'aform/login.html', {'form': form })

def post_adv(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        s = Seller.objects.get(user = request.user)
        pname = form.cleaned_data.get('name')
        pdesc = form.cleaned_data.get('desc')
        pprice = form.cleaned_data.get('price')
        pstart_date = form.cleaned_data.get('start_date')

        pstart_time = form.cleaned_data.get('start_time')
        #pduration = form.cleaned_data.get('duration')
        pcategory = form.cleaned_data.get('category')
        pimage = form.cleaned_data.get('product_image')
        
        #pdate_time = form.cleaned_data.get('date_time')
        # product = Product(seller = s, product_image=pimage, name = pname, desc = pdesc, price = pprice, start_date= pstart_date, start_time= pstart_time,  category = pcategory)
        #product.end_time = F('product.start_time')+ F('product.duration')
        #product.end_time = F('start_time')+timedelta(days=1)
     
        product = Product(seller = s, name = pname, desc = pdesc, price = pprice, category = pcategory,product_image = pimage,start_date = pstart_date,start_time = pstart_time)   
        product.save()
        return HttpResponse('product added')    
    return render(request, 'aform/advform.html', {'form': form })

def searchl(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        scat = form.cleaned_data.get('category')
        ps = Product.objects.filter(category = scat)
        yesterday = datetime.datetime.now() - timedelta(days=1)
        live = Product.objects.filter(category = scat, start_date = datetime.date.today(), start_time__lte = timezone.now())
        for l in live:
            l.status = 'live'
            l.end_date = l.start_date
            l.end_date+=timedelta(days=1)
            l.end_time = l.start_time
            #l.end_time+=timedelta(days=1)
            l.save()
        live2 = Product.objects.filter(category = scat, start_date = yesterday, start_time__gte = timezone.now())
        for l in live2:
            l.status = 'live'
            l.end_date = l.start_date
            l.end_date+=timedelta(days=1)
            l.end_time = l.start_time
            #l.end_time+=timedelta(days=1)
            l.save()
        return render(request, 'running.html', {'live': live, 'live2': live2 })
    return render(request, 'running.html',{'form': form})

def searchf(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        scat = form.cleaned_data.get('category')
        ps = Product.objects.filter(category = scat)
        yesterday = datetime.datetime.now() - timedelta(days=1)
        count=0
        inc=1
        future2 = Product.objects.filter(category=scat, status='future')
        future = Product.objects.exclude(status='future').filter(category=scat, start_date = datetime.date.today(), start_time__gte = timezone.now())
        for f in future:
            f.status= 'future'
            f.save()
        return render(request, 'future.html', {'future': future, 'future2': future2 })
    return render(request, 'future.html',{'form': form})

def searchp(request):
    form = SearchForm(request.POST or None)
    if form.is_valid():
        scat = form.cleaned_data.get('category')
        ps = Product.objects.filter(category = scat)
        yesterday = datetime.datetime.now() - timedelta(days=1)
        past = Product.objects.filter(category=scat, status='live', start_date = yesterday, start_time__lte = timezone.now())
        for p in past:
            p.status = 'past'
            p.save()
        past2 = Product.objects.filter(status = 'past')
        return render(request, 'past.html', {'past': past, 'past2': past2})
    return render(request, 'past.html',{'form': form})


# This function is obselete for now 

def status_check(tempDate,tempTime):
    if tempDate == datetime.datetime.now().date():
        if tempTime == datetime.datetime.now().time() :
            return "Running"
        elif tempTime > datetime.datetime.now().time():
            return "Scheduled"
        else:
            return "Running " 
    elif tempDate > datetime.datetime.now().date():
        return "Scheduled" 
    else :
        return "Finished"

def view_adv(request):
    print("User type "+str(request.user.usertype))
    s = Seller.objects.get(user = request.user)
    product = Product.objects.filter(seller = s)
    # print("Product is "+str(vars(product.model)))
    tempProduct = product
    mainList = []
    statusDict = {}
    statusDict["status"]=''
    statusDict["productList"] = '' 
    for obj in tempProduct:     
        tempDT = str(obj.start_date)+' '+str(obj.start_time)
        temp = datetime.datetime.strptime(tempDT,"%Y-%m-%d %H:%M:%S")
        temp2 = temp.strftime("%m,%d,%Y %H:%M:%S")
        mainList.append({
            "productList" : obj,
            "time" : temp2,
        })
        
    print("statusDict "+str(mainList))

    return render(request, 'aform/advview.html', {'product': mainList ,})

def logout_view(request):
    logout(request)
    print(request.user.is_authenticated)
    return redirect('home')

def  single_adv(request,product_id):
    # print("I am here")

    product_obj = Product.objects.filter(id = product_id)
    product_obj2 = product_obj.first()
    tempDT = str(product_obj2.start_date)+' '+str(product_obj2.start_time)
    
    temp = datetime.datetime.strptime(tempDT,"%Y-%m-%d %H:%M:%S")
    temp2 = temp.strftime("%m,%d,%Y %H:%M:%S")
    
    return   render(request, 'aform/singlead.html', {'product':product_obj,'time':temp2})


# def change_data(request,product_id):
#     product_obj = Product.objects.filter(id = product_id)
#     product_obj2 = product_obj.first()

#     tempTime = str(product_obj2.start_time)
#     tempTime = tempTime.split(".")[0]

#     temp = datetime.datetime.strptime(tempTime,"%H:%M:%S")
#     product_obj.update(start_time = temp)

#     s = Seller.objects.get(user = request.user)
#     product = Product.objects.filter(seller = s)

#     return render(request, 'aform/advview.html', {'product': product })