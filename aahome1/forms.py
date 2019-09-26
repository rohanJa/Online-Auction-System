from django import forms
from django.contrib.auth import authenticate
#from django.contrib.auth.models import User
from .models import Product
import datetime



class ProductForm(forms.ModelForm):
    start_time =forms.TimeField(widget=forms.TextInput(attrs={'placeholder': 'hh:mm'}))
    start_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    
    class Meta:
        model = Product
        fields = ( 'name', 'product_image', 'category', 'desc', 'price','start_date','start_time',)

        # fields = ( 'name', 'product_image', 'category', 'desc', 'price','start_time','start_date',)

        
class SearchForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category',)
