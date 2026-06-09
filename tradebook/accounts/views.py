from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import TradingAccount

# Create your views here.

class AccountListView(LoginRequiredMixin, ListView):

    model = TradingAccount

    template_name = 'accounts/account_list.html'

    context_object_name = 'accounts'

    def get_queryset(self):
        return TradingAccount.objects.filter(
            user=self.request.user
        )
        
class AccountCreateView(LoginRequiredMixin, CreateView):

    model = TradingAccount

    fields = (
        'name',
        'description',
        'exchange',
    )

    template_name = 'accounts/account_form.html'

    success_url = reverse_lazy('account_list')

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)
    
class AccountUpdateView(LoginRequiredMixin, UpdateView):

    model = TradingAccount

    fields = (
        'name',
        'description',
        'exchange',
    )

    template_name = 'accounts/account_form.html'

    success_url = reverse_lazy('account_list')

    def get_object(self):

        return get_object_or_404(
            TradingAccount,
            pk=self.kwargs['pk'],
            user=self.request.user
        )
        
class AccountDeleteView(LoginRequiredMixin, DeleteView):

    model = TradingAccount

    template_name = 'accounts/account_confirm_delete.html'

    success_url = reverse_lazy('account_list')

    def get_object(self):

        return get_object_or_404(
            TradingAccount,
            pk=self.kwargs['pk'],
            user=self.request.user
        )