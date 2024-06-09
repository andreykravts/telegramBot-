from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext
)

def start_bot(update: Update, context: CallbackContext) -> None:
    keyboard = ReplyKeyboardMarkup(
        [
            ['Заполнить анкету']
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    update.message.reply_text('Я бот! Зачем я создан?!', reply_markup=keyboard)