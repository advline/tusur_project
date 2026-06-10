from django.db import models
from django.utils import timezone
from accounts.models import TradingAccount

# Create your models here.


class SideChoices(models.TextChoices):

    LONG = "LONG", "Long"

    SHORT = "SHORT", "Short"


class Trade(models.Model):

    account = models.ForeignKey(
        TradingAccount, on_delete=models.CASCADE, related_name="trades"
    )

    symbol = models.CharField(max_length=30, verbose_name="Инструмент")

    side = models.CharField(max_length=10, choices=SideChoices.choices)

    entry_price = models.DecimalField(
        max_digits=20, decimal_places=8, verbose_name="Цена входа"
    )

    exit_price = models.DecimalField(
        max_digits=20, decimal_places=8, verbose_name="Цена выхода"
    )

    quantity = models.DecimalField(
        max_digits=20, decimal_places=8, verbose_name="Объем"
    )

    pnl = models.DecimalField(
        max_digits=20, decimal_places=8, default=0, verbose_name="PnL"
    )

    commission = models.DecimalField(
        max_digits=20, decimal_places=8, default=0, verbose_name="Комиссия"
    )

    closed_at = models.DateTimeField(default=timezone.now, verbose_name="Дата закрытия")

    note = models.TextField(blank=True, verbose_name="Комментарий")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ["-closed_at"]

    def __str__(self):

        return f"{self.symbol} " f"({self.side})"

    def save(self, *args, **kwargs):

        if self.side == SideChoices.LONG:

            gross_pnl = (self.exit_price - self.entry_price) * self.quantity

        else:

            gross_pnl = (self.entry_price - self.exit_price) * self.quantity

        self.pnl = gross_pnl - self.commission

        super().save(*args, **kwargs)
