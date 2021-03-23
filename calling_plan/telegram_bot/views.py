import json
from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from queue import Queue

from typing import NoReturn
from telegram import Update, Bot
from telegram.ext import (
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)


def start(update: Update, context: CallbackContext) -> NoReturn:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> NoReturn:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> NoReturn:
    response_message = "flw vlw"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )


@csrf_exempt
def telegram_bot(request):

    """View bot telegram."""

    # Create the bot's token.
    bot = Bot(token=settings.TELEGRAM_TOKEN)
    update = Update.de_json(json.loads(request.body), bot)
    print(json.loads(request.body))
    dispatcher = Dispatcher(bot=bot, update_queue=Queue(), workers=1)

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )
    dispatcher.process_update(update)
    return HttpResponse()
