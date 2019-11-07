from django.conf.urls import url
from django.urls import path

from main.views import main_page, sign_up, log_in

urlpatterns = [
    path('', main_page, name='homePage'),
    path('signup/', sign_up, name='signupPage'),
    path('login/', log_in, name='loginPage'),
]
