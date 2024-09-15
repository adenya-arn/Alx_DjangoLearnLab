from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# Create your views here.


class CustomUseCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')