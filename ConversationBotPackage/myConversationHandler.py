from telegram import  Update
from telegram.ext import (
    CallbackContext,
    ConversationHandler
)

#conversation handler
#first function work for next function upate.message.text is getting answer of user
def questionnaire_start(update: Update, context: CallbackContext) -> str:
    update.message.reply_text('Введите ваше имя:')
    return 'name'

def get_name(update: Update, context: CallbackContext) -> str:
    name = update.message.text
    update.message.reply_text('Введите вашу фамилию:')
    return 'surname'


def get_surname(update: Update, context: CallbackContext) -> str:
    surname = update.message.text
    update.message.reply_text('Введите ваш возраст:')
    return 'age'


def get_age(update: Update, context: CallbackContext) -> str:
    age = update.message.text
    update.message.reply_text('Введите ваш номер телефона:')
    return 'phone_number'

def get_phone_number(update: Update, context: CallbackContext) -> int:
    phone_number = update.message.text
    update.message.reply_text('<Здесь будет информация о пользователе>')
    return ConversationHandler.END