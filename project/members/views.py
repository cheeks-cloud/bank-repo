from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import permissions, generics,viewsets
from django.contrib import messages
from .forms import *
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.forms import AuthenticationForm 
from django.core.exceptions import ValidationError


def home(request):
    members = Member.objects.all().values()
    return render(request, "home.html", {'members': members})


def register_request(request):

    if request.method == "POST":
        form = NewMemberForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('login')
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewMemberForm()
    return render(request=request, template_name="register.html", context={"register_form": form})

def login_request(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        print(form)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            print(user)
            
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.error(request,"Invalid username or password.")
        else:
                            messages.error(request,"Invalid username or password.")


    form = LoginForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")


class MembersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AccountsViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = memberAccounts.objects.all()
    serializer_class = AccountsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class CardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cards to be viewed or edited.
    """
    queryset = membercardnum.objects.all()
    serializer_class = CardsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


