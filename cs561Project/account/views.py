from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import  UserCreate
from django.db.models import Q
import uuid
import random
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
# Create your views here.

def index(request):
    return render(request, 'account/index.html')
@login_required
def board(request):
    return render(request, 'account/board.html')
def pay(request):
    return render(request, 'account/Payment-page.html')
def signup(request):
    if request.method == 'POST':
        new_user_sign_up=UserCreate(request.POST)
        if new_user_sign_up.is_valid():
            usernew=new_user_sign_up.save(commit=False)
            usernew.set_password(
                new_user_sign_up.cleaned_data['password1']
            )
            usernew.user_id=random.randint(0,999999999)
            try:
                user=User.objects.get(username = new_user_sign_up.cleaned_data['username'])
            except Exception as a:
                user=None
            if user:
                return render(request, 'account/user_exists.html', )
            else:
                usernew.save()
                return render(
                    request,
                    'account/finsh_sign_up.html',
                    {'usernew': usernew}
                )
    else:
        new_user_sign_up = UserCreate()
    return render(
        request,
        'account/sign-up-page.html',
        {'new_user_sign_up': new_user_sign_up}
    )




class logInWithEmailorUserName:
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(Q(username=username)|Q(email=username))
            print(user.new_check_password(password,user.password))
            if user.new_check_password(password,user.password):
                return user
            return None
        except User.DoesNotExist:
            return None
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None