import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name="Email")

    nickname = models.CharField(max_length=50, blank=True, verbose_name="Никнейм")

    public_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    @property
    def display_name(self):

        if self.nickname:
            return self.nickname

        return f"Anonymous #{str(self.public_id)[:8]}"
