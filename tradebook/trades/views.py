# from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from accounts.models import TradingAccount
from .forms import TradeForm
from .models import Trade

# Create your views here.


class TradeCreateView(LoginRequiredMixin, CreateView):

    model = Trade

    form_class = TradeForm

    template_name = "trades/trade_form.html"

    def dispatch(self, request, *args, **kwargs):

        self.account = get_object_or_404(
            TradingAccount, pk=self.kwargs["account_pk"], user=request.user
        )

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["account"] = self.account

        return context

    def form_valid(self, form):

        form.instance.account = self.account

        return super().form_valid(form)

    def get_success_url(self):

        return reverse("account_detail", kwargs={"pk": self.account.pk})


class TradeDeleteView(LoginRequiredMixin, DeleteView):

    model = Trade

    template_name = "trades/trade_confirm_delete.html"

    def get_object(self):

        return get_object_or_404(
            Trade, pk=self.kwargs["pk"], account__user=self.request.user
        )

    def get_success_url(self):

        return reverse("account_detail", kwargs={"pk": self.object.account.pk})
