from django.urls import path
from .views import telegram_bot


app_name = "telegram_bot"

urlpatterns = [
    path("telegram_bot_wh", telegram_bot, name="telegram_bot_wh"),
]
