from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Memories

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

class loginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(widget=forms.PasswordInput())

class addform(forms.ModelForm):
    class Meta:
        model = Memories
        fields = ('title','content')
