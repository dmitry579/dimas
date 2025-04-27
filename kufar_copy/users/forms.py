from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'avatar',
            'password1',
            'password2',
        )