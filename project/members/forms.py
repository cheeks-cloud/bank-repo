from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.



class NewMemberForm(forms.ModelForm):
    class Meta:
        model =Member
        fields = ('firstName','lastName','email','password')


class LoginForm(forms.Form):
  email = forms.CharField(max_length=255, widget=forms.EmailInput())
  password = forms.CharField(max_length=255, widget=forms.PasswordInput())


class membersAccountForm(forms.ModelForm):
    
    class Meta:
        model = memberAccounts
        fields =['ownerName','balance','accountNumber']


class memberscardsForm(forms.ModelForm):
    
    class Meta:
        model = membercardnum
        fields =['cardAccount','cardNumber']

