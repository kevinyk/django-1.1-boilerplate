from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    messages.error(request, 'make sure to modify urls.py to match the wireframe!')
    return render(request, 'boilerplate_app/index.html')

def login(request):
    messages.error(request, 'login has not been implemented yet!')
    return redirect('/')

def register(request):
    messages.error(request, 'register has not been implemented yet!')
    return redirect('/')