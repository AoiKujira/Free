from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from main.forms import SignUpForm


def base(request):
    context = {'signed_in': request.user.is_authenticated,
               }
    return render(request, 'base.html', context=context)


def main_page(request):
    context = {'signed_in': request.user.is_authenticated,
               }
    return render(request, 'mainPage.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        signupForm = SignUpForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('homePage')
    else:
        signupForm = SignUpForm()
    context = {'signed_in': request.user.is_authenticated,
               'signupForm': signupForm,
               }
    return render(request, 'signup.html', context=context)


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            return redirect('loginPage')
    context = {'signed_in': request.user.is_authenticated,
            }
    return render(request, 'login.html', context=context)
