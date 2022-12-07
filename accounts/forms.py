from django import forms
from django.core.exceptions import ValidationError
from accounts.models import *


# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['email', 'password']


class RegisterFrom(forms.ModelForm):
    # username = forms.CharField(max_length=12)
    # email = forms.EmailField(max_length=200)
    # password = forms.CharField(max_length=200)
    password2 = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password_conf(self):
        cd = self.cleaned_data
        password = cd.get('password')
        password2 = cd.get('password2')
        if password and password2 and password != password2:
            raise ValidationError('password is not match')
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('User with this Email already exists.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        us = User.objects.filter(username=username)
        if us.exists():
            raise ValidationError('User with this Username already exists.')
        return username
