# ApertureTelegramBot
A telegram bot, written in python, inspired by the Valve game Portal/Portal 2. Reachable at [@ApertureTelegramBot](https://t.me/@ApertureTelegramBot).

## Installing dependencies
`pip install -r requirements.txt`

## Environment variables
- `TELEGRAM_API_KEY` The telegram api key
- `GROUP_ID` The id of the group to send messages to

## Usage

### Good morning message
Set up cron jobs to call `good_morning.py`

### Welcome and Goodbye messages
Set up a service to run `message_receiver.py`
