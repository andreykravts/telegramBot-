from telegram.ext import  CommandHandler,  Updater
import config
from ConversationBotPackage import conversationBotStartCommand, myConversationHandler


def main() -> None:
    updater = Updater(config.telegram_bot_api)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', conversationBotStartCommand.start_bot))
    dispatcher.add_handler(myConversationHandler.questionnaire_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()