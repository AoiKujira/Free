from django.conf.urls import url
from django.urls import path

from main.views import main_page, signup, login

urlpatterns = [
    path('', main_page, name='homePage'),
    path('signup/', signup, name='signupPage'),
    path('login/', login, name='loginPage'),
]
