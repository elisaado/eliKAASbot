#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.
"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram

botName = "eliKAAS"
botNameDownie = "elikaas"
ownerId = "107574851"

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
	
	if ("haha" in update.message.text):
			update.message.reply_text("hehehehe")

	if (botName in update.message.text or botNameDownie in update.message.text):
		if ("top kek" in update.message.text):
			update.message.reply_text("ERROR: line 14:23; 'top kek' is null! **EXITING!**")
		
		elif ("hey" in update.message.text):
			update.message.reply_text("Hey :) How are you?")

		elif ("Hey" in update.message.text):
			update.message.reply_text("Hey :) How are you?")
		
		elif ("hello" in update.message.text or "Hello" in update.message.text):
			update.message.reply_text("Hey :) How are you?")
		
		elif (botName == update.message.text or botNameDownie == update.message.text) :
			update.message.reply_text("Hey! For a list of things you can say to me type '/help'")
		
		else :
			update.message.reply_text("""I don't understand! 😢

For a list of things you can say to me type '/help'""")

	elif ("we are all fucked" in update.message.text) :
		update.message.reply_text("yes")


def error(bot, update, error):
	logger.warn('Update "%s" caused error "%s"' % (update, error))
	bot.sendMessage(chat_id=ownerId, text='Update "%s" caused error "%s"' % (update, error))


def main():
	# Create the EventHandler and pass it your bot's token.
	updater = Updater("269322124:AAFNezyol2t6ze36iSv3hgyV1cdf4aFEKSo")

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

	# Run the bot until the you presses Ctrl-C or the process receives SIGINT,
	# SIGTERM or SIGABRT. This should be used most of the time, since
	# start_polling() is non-blocking and will stop the bot gracefully.
	updater.idle()


if __name__ == '__main__':
	main()
