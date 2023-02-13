from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'email', 'firstName', 'lastName','password']


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = memberAccounts
        fields = ['url', 'ownerName','accountNumber','balance']

class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = memberAccounts
        fields = ['url','cardAccount','cardNumber',]

