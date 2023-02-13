from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.


class Member (models.Model):
    email = models.CharField(max_length=255,unique=True)
    firstName = models.CharField(max_length =255)
    lastName = models.CharField(max_length =255)
    password = models.CharField(max_length=16)
 
    def __str__(self):
      return f"{self.firstName} {self.lastName}{self.email}"


    def create_member(self):
      self.save()

    def delete_member(self):
      self.delete()

class memberAccounts(models.Model):
    ownerName = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True, blank=True)
    accountNumber = models.IntegerField(16)
    balance = models.IntegerField(16)

    def save_account(self):
       self.save()
# for each account match to member and bank registered to


class membercardnum(models.Model):
    cardNumber = models.IntegerField(16)
    cardAccount = models.ForeignKey(memberAccounts, on_delete=models.CASCADE)

    def save_account(self):
       self.save()

# for each card match it with the account and the member



























