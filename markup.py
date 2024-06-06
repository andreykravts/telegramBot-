
from telegram.ext import CallbackContext

from telegram import ReplyKeyboardMarkup, Update

# markup
def start_bot(update: Update, context: CallbackContext) -> None:
    keyboard = ReplyKeyboardMarkup(
        [
            ['/start' ,'/hello' ,'/sendPhoto' ,'/sendPhotoReply' ,'/printUpdate' ,'/whoAmI', '/money']
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    update.message.reply_text('Я бот! Зачем я создан?!', reply_markup=keyboard)

def moneyOperation(update: Update, context: CallbackContext) -> None:
    keyboard = ReplyKeyboardMarkup(
        [
            ['купить деньги'],
            ['продать деньги']
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    update.message.reply_text('Welcome to money changer!', reply_markup=keyboard)
