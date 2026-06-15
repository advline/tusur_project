from django.db import models
from django.conf import settings

from exchanges.models import Exchange

# Create your models here.


class TradingAccount(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="accounts",
    )

    exchange = models.ForeignKey(
        Exchange,
        on_delete=models.PROTECT,
        related_name="accounts",
        null=True,  # temp
        blank=True,  # temp
    )

    name = models.CharField(max_length=100, verbose_name="Название счета")

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
