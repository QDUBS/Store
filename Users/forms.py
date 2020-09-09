from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, TextInput


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'first_name', 'last_name', 'middlename', 'address', 'phone']


class Form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
       