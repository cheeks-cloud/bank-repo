from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib import messages
from .forms import *
# Create your views here.
# def members(request):
#     mypeople = Member.objects.all().values()
#     template = loader.get_template('index.html')
#     context = {
#         'mypeople':mypeople
#     }

#     return HttpResponse(template.render(context, request))
def home(request):
    return render(request, 'index.html')

def create_member(request):
    if request.method == 'POST':
        form = NewMemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.admin = request.user
            member.save()
            messages.success(
                request, 'You have succesfully created member.')
            return redirect('members')
    else:
        form = NewMemberForm()
    return render(request, 'users.html', {'form': form})

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

















