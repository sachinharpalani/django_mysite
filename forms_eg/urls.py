from django.contrib import admin
from django.urls import path, include
from .views import get_name

app_name = 'forms_eg'

urlpatterns = [
    path('contact', get_name, name='contact'),
]
