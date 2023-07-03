from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Придумайте никнейм')
    email = forms.EmailField(label='Напишите адрес почты')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите никнейм')
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']