from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from main.forms import *


def base(request):
    context = {'signed_in': request.user.is_authenticated,
               }
    return render(request, 'base.html', context=context)


def main_page(request):
    context = {'signed_in': request.user.is_authenticated,
               }
    return render(request, 'mainPage.html', context=context)


def register(request):
    if request.method == 'POST':
        signupForm = SignUpForm(request.POST)
        signupForm.is_valid()
        data = signupForm.data
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']
        print(username, password1, password2)
        if len(User.objects.filter(username=username)) > 0:
            return render(request, 'signup.html', context={'error_message1': 'نام کاربری شما در سیستم موجود است'})
        if password1 != password2:
            return render(request, 'signup.html', context={'error_message2': 'گذرواژه و تکرار گذرواژه یکسان نیستند'})
        if signupForm.is_valid():
            signupForm.save()
            return redirect('home_page')
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
            context = {'login_successful': True,

                       }
            return render(request, 'mainPage.html', context=context)
        else:
            context = {'login_failed': True,

                       }
            return render(request, 'login.html', context=context)
    context = {'signed_in': request.user.is_authenticated,
               }
    return render(request, 'login.html', context=context)


def log_out(request):
    logout(request)
    return redirect('home_page')


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            return render(request, 'contact_us_response.html', {'success': True})
    form = ContactForm()
    return render(request, "contact_us.html", {'form': form, 'success': False})
    pass
