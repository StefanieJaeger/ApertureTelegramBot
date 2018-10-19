import telepot
import os
import yaml
import random
from quotes import load_quotes


try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)


def get_quote():
    try:
        quotes = load_quotes('quotes/good_morning.txt')
        return random.choice(quotes)
    except:
        print('Unable to read quotes')
        exit(1)


bot.sendMessage(os.environ['GROUP_ID'], get_quote())
