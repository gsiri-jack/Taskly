from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import task


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))


class task_creation_form(forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'
