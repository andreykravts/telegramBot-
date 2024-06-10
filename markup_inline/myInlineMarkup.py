from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

from telegram.ext import CallbackContext
# inline markup

def start_bot(update: Update, context: CallbackContext) -> None:
    buttons = [
        [
            InlineKeyboardButton('купить деньги', callback_data='купить деньги'),
            InlineKeyboardButton('продать деньги', callback_data='продать деньги')
        ],
        [InlineKeyboardButton('настройки', callback_data='настройки')],
        [InlineKeyboardButton('test', callback_data='test')]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text('Я бот! Зачем я создан?!', reply_markup=keyboard)