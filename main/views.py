from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, redirect

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
        form.is_valid()
        data = form.data
        title = data['title']
        email = data['email']
        text = data['text']
        message = "has sent you a new message:\n\n{0}".format(text)
        send_mail(subject=title, message=text + " " + email, from_email='skillup.ml@gmail.com',
                  recipient_list=['webe19lopers@gmail.com'], fail_silently=True)
        return render(request, 'contact_us_response.html', {'success': True})
    form = ContactForm()
    return render(request, "contact_us.html", {'form': form, 'success': False})


@login_required()
def profile(request):
    user = request.user
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

            u = request.user
            # u = User.objects.get(user_name=user.username)
            # print('n1', new_last_name, 'n2', new_first_name, 'user', user, 'u', u)
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


def panel(request):
    return render(request, 'panel.html', {'user': request.user})


@user_passes_test(lambda u: u.is_superuser)
def new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            print('form saved')
        else:
            print(form.errors)
        return render(request, 'new_course.html', {'form': form})

    else:
        form = CourseForm()
        return render(request, 'new_course.html', {'form': form})


def courses(request):
    if request.method == 'POST':
        return search_department(request)
    return render(request, 'courses.html', {'courses': Course.objects.all()})


def search_department(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        form.is_valid()
        if True:
            # print(request.POST['department'], request.POST['teacher'], request.POST['course'])
            if 'department' in request.POST and request.POST.get('department'):
                return render(request, 'courses.html',
                              {'courses': Course.objects.all(),
                               'found_courses': Course.objects.filter(department=request.POST['search_query'])})
            if 'teacher' in request.POST and request.POST.get('teacher'):
                return render(request, 'courses.html',
                              {'courses': Course.objects.all(),
                               'found_courses': Course.objects.filter(teacher=request.POST['search_query'])})
            if 'course' in request.POST and request.POST.get('course'):
                return render(request, 'courses.html',
                              {'courses': Course.objects.all(),
                               'found_courses': Course.objects.filter(name=request.POST['search_query'])})
        else:
            print('agrfsdegterfdstgerfdtgrfdtgrfedwgrfed')
    return redirect('courses')
