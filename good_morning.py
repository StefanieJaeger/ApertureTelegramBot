import telepot
import os

try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)

bot.sendMessage(os.environ['GROUP_ID'], "hay hay jem jem")
