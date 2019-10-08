from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'account/index.html')