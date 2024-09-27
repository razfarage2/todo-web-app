from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    firstname = forms.CharField(max_length=30, required=True)
    lastname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'username', 'password1', 'password2')
