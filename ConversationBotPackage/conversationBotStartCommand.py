from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext
)

from ConversationBotPackage import regularMarkupConvBot


def start_bot(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Я бот! Зачем я создан?!', reply_markup=regularMarkupConvBot.get_start_keyboard())