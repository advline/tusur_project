# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import Sum

# from django.db.models import Count, Q
from django.utils import timezone

# from datetime import timedelta

from .models import TradingAccount

# Create your views here.


class AccountListView(LoginRequiredMixin, ListView):

    model = TradingAccount

    template_name = "accounts/account_list.html"

    context_object_name = "accounts"

    def get_queryset(self):
        return TradingAccount.objects.filter(user=self.request.user)


class AccountCreateView(LoginRequiredMixin, CreateView):

    model = TradingAccount

    fields = (
        "name",
        "description",
        "exchange",
    )

    template_name = "accounts/account_form.html"

    success_url = reverse_lazy("account_list")

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):

    model = TradingAccount

    fields = (
        "name",
        "description",
        "exchange",
    )

    template_name = "accounts/account_form.html"

    success_url = reverse_lazy("account_list")

    def get_object(self):

        return get_object_or_404(
            TradingAccount, pk=self.kwargs["pk"], user=self.request.user
        )


class AccountDeleteView(LoginRequiredMixin, DeleteView):

    model = TradingAccount

    template_name = "accounts/account_confirm_delete.html"

    success_url = reverse_lazy("account_list")

    def get_object(self):

        return get_object_or_404(
            TradingAccount, pk=self.kwargs["pk"], user=self.request.user
        )


class AccountDetailView(LoginRequiredMixin, DetailView):

    model = TradingAccount

    template_name = "accounts/account_detail.html"

    context_object_name = "account"

    def get_object(self):

        return get_object_or_404(
            TradingAccount, pk=self.kwargs["pk"], user=self.request.user
        )

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        trades = self.object.trades.all()

        today = timezone.now().date()

        month_start = today.replace(day=1)

        today_pnl = (
            trades.filter(closed_at=today).aggregate(total=Sum("pnl"))["total"]
            or 0
        )

        month_pnl = (
            trades.filter(closed_at__gte=month_start).aggregate(
                total=Sum("pnl")
            )["total"]
            or 0
        )

        context["today_pnl"] = today_pnl

        context["month_pnl"] = month_pnl

        context["trade_count"] = trades.count()

        context["total_pnl"] = trades.aggregate(total=Sum("pnl"))["total"] or 0

        context["wins"] = trades.filter(pnl__gt=0).count()

        context["losses"] = trades.filter(pnl__lt=0).count()

        total_trades = trades.count()
        if total_trades:

            win_rate = (context["wins"] / total_trades) * 100

        else:

            win_rate = 0
        context["win_rate"] = round(win_rate, 2)
        return context
