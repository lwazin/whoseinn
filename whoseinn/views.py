from django.shortcuts import render, redirect
from posts.models import Accom, Application

def Home(request):
    context = {
        'posts': Accom.objects.all(),
    }
    if request.method == 'POST':
        pass
    return render(request, 'index.html', context)

def fourZeroFour(request):
    context = {
    }
    return render(request, '404.html', context)
