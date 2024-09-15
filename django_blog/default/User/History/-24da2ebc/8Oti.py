from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.


class CustomUseCreationForm(UserCreationForm):
    email = forms.EmailField()