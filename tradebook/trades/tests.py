from decimal import Decimal

from django.test import TestCase

from users.models import CustomUser
from accounts.models import TradingAccount
from exchanges.models import Exchange

from .models import Trade
from .models import SideChoices


class TradeModelTest(TestCase):

    def setUp(self):

        self.user = CustomUser.objects.create_user(
            email="test@testik.ru", password="12345678"
        )

        self.exchange = Exchange.objects.create(name="Bybit")

        self.account = TradingAccount.objects.create(
            user=self.user, exchange=self.exchange, name="Main Account"
        )

    def test_long_trade_pnl_calculation(self):

        trade = Trade.objects.create(
            account=self.account,
            symbol="BTCUSDT",
            side=SideChoices.LONG,
            entry_price=Decimal("100"),
            exit_price=Decimal("120"),
            quantity=Decimal("2"),
            commission=Decimal("0"),
        )

        self.assertEqual(trade.pnl, Decimal("40"))

    def test_short_trade_pnl_calculation(self):

        trade = Trade.objects.create(
            account=self.account,
            symbol="BTCUSDT",
            side=SideChoices.SHORT,
            entry_price=Decimal("120"),
            exit_price=Decimal("100"),
            quantity=Decimal("2"),
            commission=Decimal("0"),
        )

        self.assertEqual(trade.pnl, Decimal("40"))

    def test_commission_is_subtracted(self):

        trade = Trade.objects.create(
            account=self.account,
            symbol="BTCUSDT",
            side=SideChoices.LONG,
            entry_price=Decimal("100"),
            exit_price=Decimal("120"),
            quantity=Decimal("2"),
            commission=Decimal("5"),
        )

        self.assertEqual(trade.pnl, Decimal("35"))
