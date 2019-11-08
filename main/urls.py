from django.conf.urls import url
from django.urls import path

from main.views import *

urlpatterns = [
    path('', main_page, name='home_page'),
    path('register/', register, name='register_page'),
    path('login/', log_in, name='log_in_page'),
    path('logout/', log_out, name='log_out_page'),
    path('contact_us/', contact_us, name='contact_us'),
    path('profile/', profile, name='profile_page'),
    path('edit/', profile_edit, name='profile_edit_page')
]
