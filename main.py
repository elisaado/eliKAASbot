#!/usr/bin/env python
# -*- coding: utf-8 -*-

from uuid import uuid4
import re
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import telegram
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from cleverbot import Cleverbot
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import random
from operator import itemgetter 
import json

cb = Cleverbot()


with open('config.json') as f:
    config = json.load(f)

token = config['token']
botName = config['botName']
ownerId = config['ownerId']
randomMessagesEnabled = config['randomMessagesEnabled']
randomMessages = config['randomMessages']
advertiseGroupLinkEnabled = config['advertiseGroupLinkEnabled']
groupLink = config['groupLink']
botNameDownie = botName.lower()
botNameFirstcap = botName.title()

print("The name of the bot is {}, the ID of the owner is {}, random messages enabled: {}, Advertise group link enabled: {}, And the token is {}".format(botName, ownerId, randomMessagesEnabled, advertiseGroupLinkEnabled, token))

if "yes" in randomMessagesEnabled :
    randomMessages = randomMessages.split(",,")
    print(randomMessages[1])


# This will stay here, until i know how json works :v
#with open(configFile, 'r') as f:
#    lines = f.readlines()
#    token = lines[1].strip()
#    botName = lines[3].strip()
#    ownerId = lines[5].strip()
#    if 'yes' in lines[7]:
#        RandMessages = []
#        RandMessage1 = lines[9]
#        RandMessage2 = lines[10]
#        RandMessage3 = lines[11]
#        RandMessages.append(RandMessage1.strip())
#        RandMessages.append(RandMessage2.strip())
#        RandMessages.append(RandMessage3.strip())
#
#    botNameDownie = botName.lower()
#    botNameFirstcap = botName.title()
#    f.close()
#    print("The token is {}, the name of the bot is {} and the ID of the owner is {}!".format(token, botName, ownerId))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    if botName in update.message.text or botNameDownie in update.message.text or botNameFirstcap in update.message.text or update['message']['chat']['type'] == 'private':
        update.message.reply_text("Hi, I'm eliKAASbot! I'm made by @eliKAAS")

def help(bot, update):
    if botName in update.message.text or botNameDownie in update.message.text or botNameFirstcap in update.message.text or update['message']['chat']['type'] == 'private':
        update.message.reply_text("""You can say anything, just try it! 'Hey eliKAAS how are you?'""")

def randomMsg(bot, update):
    if botName in update.message.text or botNameDownie in update.message.text or botNameFirstcap in update.message.text or update['message']['chat']['type'] == 'private':
        update.message.reply_text(random.choice(RandomMessages))

def escape_markdown(text):
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)

def inlinequery(bot, update):
    query = update.inline_query.query
    results = list()

    results.append(InlineQueryResultArticle(id=uuid4(), title="Caps", input_message_content=InputTextMessageContent(query.upper())))
    results.append(InlineQueryResultArticle(id=uuid4(), title="Lowercase", input_message_content=InputTextMessageContent(query.down())))

    update.inline_query.answer(results)

def mainMessagesHandler(bot, update):

    print(update)

    if "top kek" in update.message.text:
        update.message.reply_text("ERROR: line 14:23; 'top kek' is null! **EXITING!**")
    
    if "we are all fucked" in update.message.text:
        update.message.reply_text("yes.")

    if "haha" in update.message.text.lower():
        if random.randint(0,100) < 15:
            update.message.reply_text("LOL haha")

    if botName in update.message.text or botNameDownie in update.message.text or botNameFirstcap in update.message.text or update['message']['chat']['type'] == 'private':
        if update.message.text == botName or update.message.text == botNameDownie:
            update.message.reply_text(
                "Hey I'm eliKAASbot, a bot made by @eliKAAS! For a list of things you can say to me type /help")
        else:
            update.message.reply_text(cb.ask(update.message.text))

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
    bot.sendMessage(chat_id=ownerId, text='Update "%s" caused error "%s"' % (update, error))

def main():
    
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("random", randomMsg))
    dp.add_handler(MessageHandler([Filters.text], mainMessagesHandler))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
