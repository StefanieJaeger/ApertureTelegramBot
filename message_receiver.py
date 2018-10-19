import telepot
import os
import yaml
import random
import time
from quotes import load_quotes

try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)

try:
    greeting_quotes = load_quotes('quotes/greeting.txt')
except:
    print('Unable to read quotes')
    exit(1)

try:
    goodbye_quotes = load_quotes('quotes/goodbye.txt')
except:
    print('Unable to read quotes')
    exit(1)


# see https://core.telegram.org/bots/api
def handle(message):
    if 'new_chat_members' in message:
        return bot.sendMessage(message['chat']['id'], random.choice(greeting_quotes))

    if 'left_chat_member' in message:
        return bot.sendMessage(message['chat']['id'], random.choice(goodbye_quotes))


bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
