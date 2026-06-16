from django.test import TestCase

from users.models import CustomUser
from exchanges.models import Exchange

from .models import TradingAccount


class TradingAccountModelTest(TestCase):

    def test_account_creation(self):

        user = CustomUser.objects.create_user(
            email="test@testik.ru", password="12345678"
        )

        exchange = Exchange.objects.create(name="Bybit")

        account = TradingAccount.objects.create(
            user=user, exchange=exchange, name="Main Account"
        )

        self.assertEqual(account.name, "Main Account")

        self.assertEqual(account.exchange.name, "Bybit")

        self.assertEqual(account.user.email, "test@testik.ru")
