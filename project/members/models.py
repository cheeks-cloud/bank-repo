from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 
from pygments import highlight 
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

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

    def save_account(self):
       self.save()
# for each account match to member and bank registered to


class membercardnum(models.Model):
    ownerName = models.ForeignKey(Member,on_delete=models.SET_NULL, 
            null=True, 
            blank=True)
    ownerAcount = models.ForeignKey(memberAccounts, on_delete=models.CASCADE)

# for each card match it with the account and the member



























