from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import EmailAuthenticationForm, RegisterForm
from django.contrib.auth.views import LoginView

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = 'registration/login.html'