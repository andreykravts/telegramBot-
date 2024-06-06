import json

from telegram.ext import CallbackContext

from telegram import ReplyKeyboardMarkup, Update

import config
# reaction






def buy_money(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(update.effective_chat.id, 'You buy $50 dollars')

def sell_money(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(update.effective_chat.id, 'You sell %50 dollars')

def keep_quiet_with_smart_look(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(update.effective_chat.id, 'keep_quiet_with_smart_look')






# def start_bot(update: Update, context: CallbackContext) -> None:
#
#     update.message.reply_text('I am a bot! Commnds: /start /hello /sendPhoto /sendPhotoReply /printUpdate /whoAmI')
# def echo(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text(update.message.text)

def say_hello(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(update.effective_chat.id, 'Hello')

def send_photo(update: Update, context: CallbackContext) -> None:
    with open('photo/picture.jpg', 'rb') as photo:
        # https://docs.python-telegram-bot.org/en/v13.13/telegram.bot.html#telegram.Bot.send_animation
        context.bot.send_photo(update.effective_chat.id, photo)

def send_photo_reply(update: Update, context: CallbackContext) -> None:
    with open('photo/picture.jpg', 'rb') as photo:
        update.message.reply_photo(photo)

def print_update(update: Update, context: CallbackContext) -> None:
    message=update.to_json()
    message=json.loads(message)
    message=json.dumps(message, indent=4)
    context.bot.send_message(update.effective_chat.id, message)

def who_am_i(update: Update, context: CallbackContext) -> None:
    message=update.message.chat.first_name+" "\
            +update.message.chat.last_name+" "\
            +update.message.chat.username+" "

    context.bot.send_message(update.effective_chat.id, message)
