# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:02:02 2020

@author: ACER
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update,context):
    update.message.reply_text("Hajime")

def echo(update,context):
    update.message.reply_text(update.message.text)
    
def error(update,context):
    logger.warning('Update "%s" caused "%s" error',update,context.error)
    
def get_photo():
    content = requests.get('https://random.dog/woof.json').json()
    url = content['url']
    return url

def get_photo_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_photo()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def dog(update,context):
    url = get_photo_url()
    update.message.reply_photo(url)

def main():
    updater = Updater("1002731806:AAF2Il5Q-h7IHwtHcXNv76ahBIN_c17pM0g", use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("good_boi",dog))
    dp.add_handler(MessageHandler(Filters.text,echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()