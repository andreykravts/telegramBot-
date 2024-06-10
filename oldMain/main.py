from telegram.ext import  CommandHandler, Filters, MessageHandler, Updater
import config
from ConversationBotPackage import conversationBotStartCommand, myConversationHandler
from markup_inline import query_reactions
from markup_regular import reaction_commands, markup
from telegram.ext import CallbackQueryHandler
from telegram.ext import ConversationHandler


def main() -> None:
    updater = Updater(config.telegram_bot_api)
    dispatcher = updater.dispatcher

    # react on command /start put function inside "start_bot"
    # commands
    # dispatcher.add_handler(CommandHandler('start', myInlineMarkup.start_bot))
    # dispatcher.add_handler(CommandHandler('start', markup.start_bot))
    dispatcher.add_handler(CommandHandler('hi', reaction_commands.say_hello))
    dispatcher.add_handler(CommandHandler('photo', reaction_commands.send_photo))
    dispatcher.add_handler(CommandHandler('photo2', reaction_commands.send_photo_reply))
    dispatcher.add_handler(CommandHandler('up', reaction_commands.print_update))
    dispatcher.add_handler(CommandHandler('who', reaction_commands.who_am_i))
    dispatcher.add_handler(CommandHandler('money', markup.moneyOperation))
    # # react on text or other staff
    # # dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reaction_commands.echo))
    #
    # # message
    #set patterns before
    dispatcher.add_handler(MessageHandler(Filters.regex('^купить деньги$'), reaction_commands.buy_money))
    dispatcher.add_handler(MessageHandler(Filters.regex('^продать деньги$'), reaction_commands.sell_money))
    # set in the end
    # dispatcher.add_handler(MessageHandler(Filters.text, reaction_commands.keep_quiet_with_smart_look))


    # Conversation handler


    questionnaire_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^Заполнить анкету$'), myConversationHandler.questionnaire_start)],
        states={
            'name': [MessageHandler(Filters.text, myConversationHandler.get_name)],
            'surname': [MessageHandler(Filters.text, myConversationHandler.get_surname)],
            'age': [MessageHandler(Filters.text, myConversationHandler.get_age)],
            'phone_number': [MessageHandler(Filters.text, myConversationHandler.get_phone_number)],
        },
        fallbacks=[]
    )

    dispatcher.add_handler(CommandHandler('start', conversationBotStartCommand.start_bot))
    dispatcher.add_handler(questionnaire_handler)


    # query
    #set patterns vefore
    dispatcher.add_handler(CallbackQueryHandler(query_reactions.buy_money, pattern='^купить деньги$'))
    dispatcher.add_handler(CallbackQueryHandler(query_reactions.sell_money, pattern='^продать деньги$'))
    dispatcher.add_handler(CallbackQueryHandler(query_reactions.settings, pattern='^настройки$'))
    #set in the end
    #actually not in use when we didnt have other buttons add test button
    dispatcher.add_handler(CallbackQueryHandler(query_reactions.reply_when_click_on_inline_button))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()