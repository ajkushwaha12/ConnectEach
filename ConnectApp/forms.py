from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter Email'
    }))
    first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter First Name'
    }))
    last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter Last Name'
    }))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter Username'
    }))

    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'
    }))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Conform Password'
    }))

    def clean_password(self):
        password1 = self.cleaned_data['password']

        # Password validation rules
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password1):
            raise ValidationError("Password must contain at least one capital letter.")
        if not re.search(r'[a-z]', password1):
            raise ValidationError("Password must contain at least one small letter.")
        if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password1):
            raise ValidationError("Password must contain at least one special character.")

        return password1

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
