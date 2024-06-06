from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater
import config
import reaction_commands, markup

def main() -> None:
    updater = Updater(config.telegram_bot_api)
    dispatcher = updater.dispatcher

    # react on command /start put function inside "start_bot"
    dispatcher.add_handler(CommandHandler('start', markup.start_bot))
    dispatcher.add_handler(CommandHandler('hello', reaction_commands.say_hello))
    dispatcher.add_handler(CommandHandler('sendPhoto', reaction_commands.send_photo))
    dispatcher.add_handler(CommandHandler('sendPhotoReply', reaction_commands.send_photo_reply))
    dispatcher.add_handler(CommandHandler('printUpdate', reaction_commands.print_update))
    dispatcher.add_handler(CommandHandler('whoAmI', reaction_commands.who_am_i))
    dispatcher.add_handler(CommandHandler('money', markup.moneyOperation))
    # react on text or other staff
    # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reaction_commands.echo))


    dispatcher.add_handler(MessageHandler(Filters.regex('^купить деньги$'), reaction_commands.buy_money))
    dispatcher.add_handler(MessageHandler(Filters.regex('^продать деньги$'), reaction_commands.sell_money))
    dispatcher.add_handler(MessageHandler(Filters.text, reaction_commands.keep_quiet_with_smart_look))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()