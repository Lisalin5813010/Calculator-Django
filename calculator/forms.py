from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CalForm(forms.Form):
    num1 = forms.Field(required=False)
    num2 = forms.Field(required=False)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
