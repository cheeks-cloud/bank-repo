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
from django.contrib.auth.decorators import login_required

def home(request):
    members = Member.objects.all().values()
    return render( request, "users.html", {'members': members})


def register_request(request):

	if request.method == "POST":
		form =NewMemberForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewMemberForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


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


@login_required(login_url='login')
def new_account(request):
	if request.method == 'POST':
			form = membersAccountForm(request.POST,request.FILES)
			if form.is_valid():
				new_post = form.save()
				new_post.save_account()
			return redirect('home')
	else:
		form = membersAccountForm()
	return render(request, 'users.html', {'form': form})














