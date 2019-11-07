from django.conf.urls import url
from django.urls import path

from main.views import main_page

urlpatterns = [
    path('', main_page),
]