from telegram import  Update
from telegram.ext import (
    CallbackContext,
    ConversationHandler
)

from telegram.ext import  Filters, MessageHandler

from ConversationBotPackage import regularMarkupConvBot


#conversation handler
#first function work for next function upate.message.text is getting answer of user

# def questionnaire_start(update: Update, context: CallbackContext) -> str:
#     update.message.reply_text('Введите ваше имя:')
#     return 'name'

def get_name(update: Update, context: CallbackContext) -> str:
    context.user_data['name'] = update.message.text
    update.message.reply_text('Введите вашу фамилию:')
    return 'surname'


def get_surname(update: Update, context: CallbackContext) -> str:
    context.user_data['surname'] = update.message.text
    update.message.reply_text('Введите ваш возраст:')
    return 'age'


def get_age(update: Update, context: CallbackContext) -> str:
    context.user_data['age'] = update.message.text
    update.message.reply_text('Введите ваш номер телефона:')
    return 'phone_number'

def get_phone_number(update: Update, context: CallbackContext) -> int:
    context.user_data['phone_number'] = update.message.text
    update.message.reply_text(
        f'Имя: {context.user_data["name"]}\n'
        f'Фамилия: {context.user_data["surname"]}\n'
        f'Возраст: {context.user_data["age"]}\n'
        f'Номер телефона: {context.user_data["phone_number"]}',
        reply_markup = regularMarkupConvBot.get_start_keyboard()
    )
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Очень жаль, что вы так рано уходите',
                              reply_markup=regularMarkupConvBot.get_start_keyboard())
    return ConversationHandler.END



# Conversation handler
questionnaire_handler = ConversationHandler(
    entry_points=[MessageHandler(Filters.regex('^Заполнить анкету$'), regularMarkupConvBot.questionnaire_start)],
    states={
        'name': [MessageHandler(Filters.text & ~Filters.regex('^отмена$'),  get_name)],
        'surname': [MessageHandler(Filters.text & ~Filters.regex('^отмена$'), get_surname)],
        'age': [MessageHandler(Filters.text & ~Filters.regex('^отмена$'), get_age)],
        'phone_number': [MessageHandler(Filters.text & ~Filters.regex('^отмена$'), get_phone_number)],
    },
    fallbacks=[MessageHandler(Filters.regex('^отмена$'), cancel)]
)

