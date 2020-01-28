from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import CustomUser as User
from django.contrib.auth import (login as auth_login,  authenticate, logout as _logout)
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
                user = User.objects.create_user(email=request.POST['email'], password=request.POST['password1'], name=request.POST['name'], surname=request.POST['surname'], username=request.POST['username'])
                auth_login(request, user)

                subject = "Email Confirmation - WhoseInn.com"
                message = """Thank you for signing up to use the WhoseInn service.

                Feel free to express your experience as your input is highly appreciated and will go a long way in the app's overall development."""
                from_email = settings.EMAIL_HOST_USER
                to_list = [request.POST['email'], settings.EMAIL_HOST_USER]

                try:
                    send_mail(subject, message, from_email, to_list, fail_silently=False)
                    print('email sent')
                except:
                    print('email not sent')
                return redirect('home')


    return redirect("home")

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
