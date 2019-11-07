from django.conf.urls import url
from django.urls import path

from main.views import base

urlpatterns = [
    path('', base),
]