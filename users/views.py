from django.shortcuts import render, redirect
from .models import CustomUser as User, Profile
from django.contrib.auth import (login as auth_login,  authenticate, logout as _logout)
from django.contrib import auth

def signup(request):
    context = {}
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =Level_One User.objects.get(email=request.POST['email'])
                return redirect('home')
            except user.DoesNotExist:
                user = User.objects.create_user(email=request.POST['email'], password=request.POST['password1'], name=request.POST['name'], surname=request.POST['surname'])
                auth_login(request, user)
            return redirect('home')
    else:
        pass
    return redirect('home')


def login(request):
    if request.method == 'POST':
        _email = request.POST['email']
        _password = request.POST['password']
        user = authenticate(username=_email, password=_password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                if request.user.is_authenticated:
                    pass
                return redirect('home')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    if request.user.is_authenticated:
        pass
    return redirect('home')

def logout(request):
    context = {}
    auth.logout(request)
    return redirect('home')
