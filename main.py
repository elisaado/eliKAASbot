#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from cleverbot import Cleverbot
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

cb = Cleverbot()
botName = "eliKAAS"
botNameDownie = botName.lower()
ownerId = "107574851"
token = input('Token: ')


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    if botName in update.message.text or botNameDownie in update.message.text or update['message']['chat']['type'] == 'private':
        update.message.reply_text("Hi, I'm eliKAASbot! I'm made by @eliKAAS")


def help(bot, update):
    if botName in update.message.text or botNameDownie in update.message.text or update['message']['chat']['type'] == 'private':
        update.message.reply_text("""You can say anything, just try it! 'Hey eliKAAS how are you?'""")



def escape_markdown(text):
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(id=uuid4(),
                                            title="eliKAAS:",
                                            input_message_content=InputTextMessageContent(
                                                query.upper())))

    update.inline_query.answer(results)


def mainMessagesHandler(bot, update):

    print(update)

    if "haha" in update.message.text or "HAHA" in update.message.text or "Haha" in update.message.text:
        update.message.reply_text("LOL haha")

    if botName in update.message.text or botNameDownie in update.message.text or update['message']['chat']['type'] == 'private':
        if "top kek" in update.message.text:
            update.message.reply_text(
                "ERROR: line 14:23; 'top kek' is null! **EXITING!**")

        elif update.message.text == botName or update.message.text == botNameDownie:
            update.message.reply_text(
                "Hey I'm eliKAASbot, a bot made by @eliKAAS! For a list of things you can say to me type /help")

        else:
            update.message.reply_text(cb.ask(update.message.text))


    elif "we are all fucked" in update.message.text:
        update.message.reply_text("yes.")


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    #bot.sendMessage(chat_id=ownerId,
    #                text='Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler([Filters.text], mainMessagesHandler))
    
    dp.add_handler(InlineQueryHandler(inlinequery))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
