from django import forms
from django.contrib.auth.models import User
from .models import *


class NewMemberForm(forms.ModelForm):
    class Meta:
        model =Member
        exclude = ('admin',)


class membersAccountForm(forms.ModelForm):
    
    class Meta:
        model = memberAccounts
        fields =['owner','balance','acountNumber']


class memberscardsForm(forms.ModelForm):
    
    class Meta:
        model = membercardnum
        fields =['ownerName','ownerAcount']

