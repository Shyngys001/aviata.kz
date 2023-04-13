from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Tasks
from django.forms import ModelForm, TextInput, Textarea


class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ["titles", "tasks"]
        widgets = {
            "titles": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input title'
            }),
            "tasks": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input description'
            }),
        }

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    def get_success_url(self):
        return reverse("create")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))