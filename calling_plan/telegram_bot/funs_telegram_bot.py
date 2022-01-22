from typing import NoReturn
from telegram import Update
from telegram.ext import CallbackContext
from calling_plan.military.models import Military


def start(update: Update, context: CallbackContext) -> NoReturn:
    """Send a message when the command /start is issued."""
    update.message.reply_text("Bem vindo ao Bot CallingPlan\n\n")


def register(update: Update, context: CallbackContext) -> NoReturn:
    """."""
    if not context.args:
        update.message.reply_text(
            "Comando inválido Exemplo: /cadastro 000.000.000-00"
        )
    else:
        try:
            military = Military.objects.get(identidade=context.args[0])
        except Exception:
            military = None

        if military:
            military.telegram_id = update.effective_chat.id
            military.save()
            update.message.reply_text(
                "Cadastrado no Plano de Chamada e Lembrete."
            )
        else:
            update.message.reply_text(
                "Usuário inválido ou fora do padão ex: 000.000.000-00"
            )


def help_command(update: Update, context: CallbackContext) -> NoReturn:
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        """
        Comandos: 
        /cadastro nome-de-usuario ex: /cadastro 000.000.000-00 ou fulandodetal\n 
        /Aditamento
        /boletim
        /escala
        """
    )


def echo(update: Update, context: CallbackContext) -> NoReturn:
    response_message = """
        Comandos: 
        /cadastro nome-de-usuario ex: /cadastro 000.000.000-00 ou fulandodetal\n 
        /Aditamento
        /boletim
        /escala
        """
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )
