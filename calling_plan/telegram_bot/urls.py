from django.conf import settings
from django.urls import path

from .views import telegram_bot

app_name = "telegram_bot"

urlpatterns = [
    path(f"telegram_{settings.TELEGRAM_TOKEN}", telegram_bot),
]
