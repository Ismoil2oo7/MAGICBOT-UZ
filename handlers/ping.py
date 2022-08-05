from telethon import TelegramClient, events
import handlers.client
import time

client = handlers.client.client


@events.register(events.NewMessage(pattern='\.ping'))
async def pingHandler(event):
	   start = datetime.now()
	   msg = await event.reply("Pong!")
	   end = datetime.now()
	   ms = (end - start).microseconds / 1000
	   await msg.edit(f"**Pong!!**\n `{ms} ms`")