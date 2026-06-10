from django.forms import ModelForm
from django import forms
from .models import Trade


class TradeForm(ModelForm):

    class Meta:

        model = Trade

        exclude = (
            "account",
            "created_at",
            "pnl",
        )

        widgets = {"closed_at": forms.DateInput(attrs={"type": "date"})}
