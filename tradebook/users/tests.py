from django.test import TestCase

from .models import CustomUser


class CustomUserModelTest(TestCase):

    def test_display_name_uses_nickname(self):

        user = CustomUser.objects.create_user(
            email="test@testik.ru", password="12345678", nickname="Trader"
        )

        self.assertEqual(user.display_name, "Trader")

    def test_display_name_returns_anonymous(self):

        user = CustomUser.objects.create_user(
            email="anonymous@testik.ru", password="12345678"
        )

        self.assertTrue(user.display_name.startswith("Anonymous #"))
