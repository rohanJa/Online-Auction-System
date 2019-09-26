from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.conf import settings
# Create your models here.

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('usertype', 'username', 'email', 'password1', 'password2')
        
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("this user does'nt exist")
            if not user.check_password(password):
                raise forms.ValidationError("incorrect password")
            if not user.is_active:
                raise forms.ValidationError("this is not active user")
        return super(UserLoginForm, self).clean(*args, **kwargs)
