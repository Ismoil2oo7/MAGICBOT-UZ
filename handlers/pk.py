from telethon import TelegramClient, events
import handlers.client
import time

client = handlers.client.client
@events.register(events.NewMessage)
async def pkhandler(event):
    if '.pk' in event.raw_text:
        await event.edit("Sen insonmisan?")
        time.sleep(5)
        await event.edit("daunmisan?")
        