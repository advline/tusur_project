from django.contrib import admin
from .models import TradingAccount

# Register your models here.

@admin.register(TradingAccount)
class TradingAccountAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'user',
        'created_at',
    )