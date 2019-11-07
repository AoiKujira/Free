from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from main.forms import SignUpForm


def base(request):
    return render(request, 'base.html')


def main_page(request):
    return render(request, 'mainPage.html')


def signup(request):
    if request.method == 'POST':
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('homePage')
    else:
        signupForm = SignUpForm()
    return render(request, 'signup.html', {'signupForm': signupForm})


def login(request):
    pass
