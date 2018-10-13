import telepot
import os
import yaml
import random


try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)


def get_quote():
    with open('good_morning_quotes.yml', encoding='utf8') as file:
        try:
            quotes = yaml.load(file.read())['quotes']
            return random.choice(quotes)
        except:
            print('Unable to read quotes')


bot.sendMessage(os.environ['GROUP_ID'], get_quote())
