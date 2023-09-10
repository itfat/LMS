from django.contrib.auth.forms import AuthenticationForm
from django import forms

class MyAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
