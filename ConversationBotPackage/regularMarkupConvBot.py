
from telegram.ext import CallbackContext

from telegram import ReplyKeyboardMarkup

from telegram import Update


def questionnaire_start(update: Update, context: CallbackContext) -> str:
    keyboard = ReplyKeyboardMarkup(
        [
            ['отмена']
        ],
        resize_keyboard=True,
    )
    update.message.reply_text('Введите ваше имя:', reply_markup=keyboard)
    return 'name'

def get_start_keyboard():
    return ReplyKeyboardMarkup(
        [
            ['Заполнить анкету']
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )