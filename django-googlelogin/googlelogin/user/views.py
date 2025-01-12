from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def home(request):
    return render(request, 'home.html')

def logout(request):
    logout(request)
    return redirect('/')