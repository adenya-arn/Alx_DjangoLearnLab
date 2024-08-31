from django import forms
from django.contrib.auth.models import User

class LibraryName(forms.Form):
    library_name = forms.CharField(max_length=300, label="Library name")

class UserCreationForm(forms.Form):
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Confirm Password')
    email = forms.EmailField(required=False)
    first_name = forms.CharField(max_length=50)
    last_name =  forms.CharField(max_length=50)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class AddBook(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)

class DeleteBook(forms.Form):
    title = forms.CharField(max_length=100)

class ChangeBook(forms.Form):
    from_title = forms.CharField(max_length=100, label="From")
    to_title = forms.CharField(max_length=100, label="To")