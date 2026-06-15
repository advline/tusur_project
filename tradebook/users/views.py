# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import EmailAuthenticationForm, RegisterForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    authentication_form = EmailAuthenticationForm
    template_name = "registration/login.html"


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "users/profile.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfileUpdateForm

    template_name = "users/profile_edit.html"

    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user


class UserLogoutView(LogoutView):
    pass
