from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ['url', 'username', 'firstName', 'lastName','accounts']


class AccountsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = memberAccounts
        fields = ['url', 'owner','accountNumber','balance']

class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = memberAccounts
        fields = ['url', 'ownerName','ownerAcount']

