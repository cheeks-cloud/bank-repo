from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions


# Create your views here.
def members(request):
    mypeople = Member.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mypeople':mypeople
    }

    return HttpResponse(template.render(context, request))


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = memberAccounts.objects.all()
    serializer_class = AccountsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = membercardnum.objects.all()
    serializer_class = CardsSerializer
    permission_classes = [permissions.IsAuthenticated]

















