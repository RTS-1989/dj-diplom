from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField()
    last_name = forms.CharField(widget=forms.PasswordInput)
