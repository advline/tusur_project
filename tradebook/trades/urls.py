from django.urls import path

from .views import TradeCreateView, TradeDeleteView

urlpatterns = [
    path(
        "accounts/<int:account_pk>/trades/create/",
        TradeCreateView.as_view(),
        name="trade_create",
    ),
    path("trades/<int:pk>/delete/", TradeDeleteView.as_view(), name="trade_delete"),
]
