import telepot
import os
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

try:
    facts = load_quotes('quotes/facts.txt')
except:
    print('Unable to read facts')
    exit(1)


# see https://core.telegram.org/bots/api
def handle(message):
    if 'new_chat_members' in message:
        for new_chat_member in message['new_chat_members']:
            if new_chat_member['id'] == bot.getMe()['id']:
                print('Was added to group "{}" with id "{}"'.format(message['chat']['title'], message['chat']['id']))
                return

        return bot.sendMessage(message['chat']['id'], random.choice(greeting_quotes))

    if 'left_chat_member' in message:
        if message['left_chat_member']['id'] == bot.getMe()['id']:
            print('Was removed from group "{}" with id "{}"'.format(message['chat']['title'], message['chat']['id']))
            return

        return bot.sendMessage(message['chat']['id'], random.choice(goodbye_quotes))

    if 'text' in message and message['text'].startswith('/fact'):
        return bot.sendMessage(message['chat']['id'], random.choice(facts))


bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
