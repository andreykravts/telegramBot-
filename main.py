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
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()