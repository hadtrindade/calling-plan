from django.urls import path
from .views import telegram_bot


app_name = "telegram_bot"

urlpatterns = [
    path("telegram_bot_wh", telegram_bot, name="telegram_bot_wh"),
]


"""
from django.urls import path
from .views import telegram_bot
from django.conf.settings import TELEGRAM_TOKEN


app_name = "telegram_bot"

urlpatterns = [
    path(f"telegram_{TELEGRAM_TOKEN}", telegram_bot, name="telegram_{TELEGRAM_TOKEN}"),
]
"""