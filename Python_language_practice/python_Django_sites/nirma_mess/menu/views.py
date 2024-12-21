from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserCreationFormWithEmail
from .models import Menu


def home(request):
    return render(request, 'menu/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'menu/signupuser.html', {'form': UserCreationFormWithEmail()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['email']
                )
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'menu/signupuser.html', {'form': UserCreationFormWithEmail(),
                                                                'error': 'That username has already been taken. '
                                                                         'Please choose a new username'})
        else:
            return render(request, 'menu/signupuser.html',
                          {'form': UserCreationFormWithEmail(), 'error': 'Passwords did not match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'menu/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'menu/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currenttodos')


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def menu(request):
    return render(request, 'menu/menu.html', {'Menu': Menu})
