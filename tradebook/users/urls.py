from django.urls import path

from .views import (
    RegisterView,
    UserLoginView,
    ProfileView,
    ProfileUpdateView,
    UserLogoutView,
)

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        UserLoginView.as_view(),
        name='login'
    ),
    
    path(
        'profile/',
        ProfileView.as_view(),
        name='profile'
    ),
    path(
        'profile/edit/',
        ProfileUpdateView.as_view(),
        name='profile_edit'
    ),
    path(
        'logout/',
        UserLogoutView.as_view(),
        name='logout'
    ),
]