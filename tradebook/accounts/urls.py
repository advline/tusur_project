from django.urls import path

from .views import (
    AccountListView,
    AccountCreateView,
    AccountUpdateView,
    AccountDeleteView,
    AccountDetailView,
)

urlpatterns = [
    path("", AccountListView.as_view(), name="account_list"),
    path("create/", AccountCreateView.as_view(), name="account_create"),
    path("<int:pk>/", AccountDetailView.as_view(), name="account_detail"),
    path("<int:pk>/edit/", AccountUpdateView.as_view(), name="account_edit"),
    path(
        "<int:pk>/delete/", AccountDeleteView.as_view(), name="account_delete"
    ),
]
