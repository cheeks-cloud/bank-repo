from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Member (models.Model):
    userName = models.CharField(max_length=255)
    firstName = models.CharField(max_length =255)
    lastName = models.CharField(max_length =255)
    accounts = models.OneToOneField(User, on_delete=models.CASCADE, 
           null=True, blank=True)
    # cards = models.ManyToManyField(membercardnum)

    #to return as identified objects1
    def __str__(self):
      return f"{self.userName} {self.firstname} {self.lastname}{self.accounts}"


    def create_member(self):
      self.save()

    def delete_member(self):
      self.delete()

class memberAccounts(models.Model):
    owner = models.ForeignKey(Member,on_delete=models.SET_NULL,null=True, blank=True)
    acountNumber = models.IntegerField(16)
    balance = models.IntegerField(16)
  
# for each account match to member and bank registered to


class membercardnum(models.Model):
    ownerName = models.ForeignKey(Member,on_delete=models.SET_NULL, 
            null=True, 
            blank=True)
    ownerAcount = models.ForeignKey(memberAccounts, on_delete=models.CASCADE)

# for each card match it with the account and the member



























  # CHOICES = [('bank1', 'bank1'),
    #     ('bank2', 'bank2'),
    #     ('bank3', 'bank3'),
    #     ('bank4', 'bank4'),]
    # bank= models.CharField( choices=CHOICES, max_length=30,null=False, blank=False)
