
from telegram.ext import CallbackContext

from telegram import ReplyKeyboardMarkup

from telegram import Update



# markup
def start_bot(update: Update, context: CallbackContext) -> None:
    keyboard = ReplyKeyboardMarkup(
        [
            ['/start' ,'/hello'  , '/money'],
            ['/sendPhoto' ,'/sendPhotoReply'],
            ['/printUpdate' ,'/whoAmI']

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
