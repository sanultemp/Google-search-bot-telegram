# -*- coding: utf-8 -*- 
botID = "2126509842:AAEivNO4mI0Ky9808Ma9Pf5_riuanbqjG-0" 
from telegram import Updater
import subprocess
import logging
import sys
import time
import thread
reload(sys)
sys.setdefaultencoding('utf8')

flood = 0
def checkFlood(delay):
   while 1:
      global flood
      flood = 0
      time.sleep(60)

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Hi!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def google(bot, update):
    global flood
    if(flood == 0):
       proc = subprocess.Popen("python google.py " + update.message.text, stdout=subprocess.PIPE, shell=True)
       (out, err) = proc.communicate()
       bot.sendMessage(update.message.chat_id, text=out)
       flood = 1
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    thread.start_new_thread(checkFlood, (2,))
    updater = Updater(botID)
    dp = updater.dispatcher
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("google", google)
    dp.addErrorHandler(error)
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
