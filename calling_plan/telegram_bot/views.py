import json
from queue import Queue

from django.conf import settings
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler

from .funs_telegram_bot import echo, help_command, register, start


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
    dispatcher.add_handler(CommandHandler("cadastro", register))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, echo)
    )
    dispatcher.process_update(update)
    return HttpResponse()
