from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login
from django.forms import Form, ModelForm

from main.models import Course


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text='')
    last_name = forms.CharField(max_length=30, help_text='')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2',)


class ContactForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    email = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, max_length=250, min_length=10, required=True)


class ProfileEditForm(forms.Form):
    new_first_name = forms.CharField(max_length=200, required=False)
    new_last_name = forms.CharField(max_length=200, required=False)


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time',
                  'first_day', 'second_day']
