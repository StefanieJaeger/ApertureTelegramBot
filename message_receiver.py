import telepot
import os
import yaml
import random
import time

try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)

with open('greeting_quotes.yml', encoding='utf8') as file:
    try:
        greeting_quotes = yaml.load(file.read())['quotes']
    except:
        print('Unable to read quotes')

with open('goodbye_quotes.yml', encoding='utf8') as file:
    try:
        goodbye_quotes = yaml.load(file.read())['quotes']
    except:
        print('Unable to read quotes')


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
