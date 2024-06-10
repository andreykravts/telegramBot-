

from telegram.ext import CallbackContext

from telegram import Update


# the message with inline markup will disappear
# def reply_when_click_on_inline_button(update: Update, context: CallbackContext) -> None:
#     query = update.callback_query
#     query.answer()
#     query.edit_message_text(f'Вы выбрали: {query.data}')

#the message with inline markup will stay with the user
def reply_when_click_on_inline_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.message.reply_text(f'Вы выбрали: {query.data}')

def buy_money(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.message.reply_text('Вы купили 100 долларов')

def sell_money(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.message.reply_text('Вы продали 100 долларов')

def settings(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.message.reply_text('Здесь должны быть настройки')


