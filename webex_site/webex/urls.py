from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from django.urls import path, include
from .views import *


urlpatterns = [
    path('',  WebexHome.as_view(), name='home'),
]
