from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Your Username'
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Your password'
    }))

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Your Username'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Your Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Your password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class':'w-full py-4 px-6 rounded-xl',
        'placeholder':'Confirm Password'
    }))