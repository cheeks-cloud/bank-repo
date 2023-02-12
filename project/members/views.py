from django.shortcuts import render,redirect
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions,generics
from django.contrib import messages
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    members = Member.objects.all().values()
    return render( request, "users.html", {'members': members})

def create_member(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.admin = request.user
            member.save()
            messages.success(
                request, 'You have succesfully created member.')
            return redirect('')
    else:
        form = NewMemForm()
    return render(request, 'new_member.html', {'form': form})

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
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

















