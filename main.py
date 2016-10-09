#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram
import clever

botName = "eliKAAS"
botNameDownie = botName.lower()
ownerId = "107574851"
token = input('Token: ')
cbtoken = input('CleverBot Token: ')
cbuser = input('CleverBot User Token: ')
client = clever.CleverBot(user=cbuser, key=cbtoken)

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text("""You don't know what to say? Here is a list!
	
	I don't have a list yet... 😢 Please come back later.""")


def mainMessagesHandler(bot, update):

    if "haha" in update.message.text or "HAHA" in update.message.text:
        update.message.reply_text("hehehehe")

    if botName in update.message.text or botNameDownie in update.message.text:
        if "top kek" in update.message.text:
            update.message.reply_text(
                "ERROR: line 14:23; 'top kek' is null! **EXITING!**")

        elif update.message.text == botName or update.message.text == botNameDownie:
            update.message.reply_text(
                "Hey! For a list of things you can say to me type /help")

        else:
            update.message.reply_text(client.query(update.message.text))


    elif "we are all fucked" in update.message.text:
        update.message.reply_text("yes.")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    bot.sendMessage(chat_id=ownerId,
                    text='Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], mainMessagesHandler))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
