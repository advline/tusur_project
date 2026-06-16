from django.test import TestCase

from .models import Exchange


class ExchangeModelTest(TestCase):

    def test_exchange_creation(self):

        exchange = Exchange.objects.create(name="Bybit")

        self.assertEqual(exchange.name, "Bybit")
