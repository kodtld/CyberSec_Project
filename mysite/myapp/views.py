from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import GameForm

from django.db import connections

from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    context = {}
    games = Game.objects.all()
    return render(request,'pages/home.html',{'games':games})

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request,'pages/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render (request,'pages/register.html',context)

def createGame(request):
    form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)
        print(request.POST['title'])
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'pages/gameform.html',context)

def updateGame(request, pk):
    game = Game.objects.get(id=pk)
    form = GameForm(instance=game)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'pages/gameform.html',context)

def deleteGame(request,pk):
    game = Game.objects.get(id=pk)
    if request.method == "POST":
        game.delete()
        return redirect('home')
    context = {'item':game}
    return render(request,'pages/delete.html', context )