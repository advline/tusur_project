from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password1',
            'password2',
        )

class EmailAuthenticationForm(AuthenticationForm):

    username = forms.EmailField(
        label='Email'
    )
    
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser

        fields = (
            'nickname',
        )