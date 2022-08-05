from telethon import TelegramClient

api_id = 14847906
api_hash = "e4c8bab588782253015a20da73354980"
bot_token = "5372825313:AAGw4JAGGv5IQK7bSVkdSAYOXxmSio7mZi0"
client = TelegramClient('anon', api_id, api_hash)

botClient = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)