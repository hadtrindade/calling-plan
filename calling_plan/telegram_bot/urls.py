from django.urls import path
from .views import telegram_bot
from django.conf import settings


app_name = "telegram_bot"

urlpatterns = [
    path(f"telegram_{settings.TELEGRAM_TOKEN}", telegram_bot),
]
