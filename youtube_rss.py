import telepot
import os
import feedparser
import time

try:
    bot = telepot.Bot(os.environ['TELEGRAM_API_KEY'])
except telepot.exception.BadHTTPResponse:
    print('Received a bad HTTP response while getting connection to bot')
    exit(1)


feed = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UCUJXm3LMFLSEe_A2IBf8GwQ')
for entry in feed.entries:
    pubDate = time.mktime(entry.published_parsed)
    if time.time() + time.timezone - pubDate <= (30 * 60 + 10):
        bot.sendMessage(os.environ['GROUP_ID'], 'New video out! {}'.format(entry.link))
    else:
        break
