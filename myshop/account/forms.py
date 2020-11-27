from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    user_name = forms.CharField()
    last_name = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('user_name', 'email', 'password1', 'password2')
