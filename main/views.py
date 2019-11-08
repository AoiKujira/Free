from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

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
            message = "has sent you a new message:\n\n{0}".format(text)
            send_mail(subject=title, message=text, from_email=email, recipient_list=['webe19lopers@gmail.com'])
            return render(request, 'contact_us_response.html', {'success': True})
    form = ContactForm()
    return render(request, "contact_us.html", {'form': form, 'success': False})


@login_required()
def profile(request):
    user = request.user
    print(user.first_name)
    context = {'username': user.username,
               'first_name': user.first_name,
               'last_name': user.last_name,
               }

    return render(request, 'profile.html', context=context)


@login_required()
def profile_edit(request):
    context = {'message': ''}
    if request.method == 'POST':
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            data = form.data
            new_first_name = data['first_name']
            new_last_name = data['last_name']

            user = request.user
            u = User.objects.get(first_name=user.first_name)
            print('n1', new_last_name, 'n2', new_first_name, 'user', user, 'u', u)
            if new_first_name != '':
                u.first_name = new_first_name
                # User.objects.filter(first_name=user.first_name).update(first_name=new_first_name)
            if new_last_name != '':
                u.last_name = new_last_name
                # User.objects.filter(last_name=user.last_name).update(last_name=new_last_name)
            u.save(update_fields=['first_name', 'last_name'])
            context = {'message': 'success'}
            return redirect('profile_page')
            # return render(request, 'profile.html', context=context)
        else:
            context = {'message': 'failed'}
            return render(request, 'profile.html', context=context)
    return render(request, 'profile_edit.html', context=context)
