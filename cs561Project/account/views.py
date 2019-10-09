from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .forms import  UserCreate
import uuid
import random
# Create your views here.

def index(request):
    return render(request, 'account/index.html')

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

def login(request):
    return render(request, 'account/index.html')