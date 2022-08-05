from telethon import TelegramClient, events
import handlers.client, handlers.magic
from handlers.magic import Magic
import time
magic = Magic()
client = handlers.client.client
@events.register(events.NewMessage)
async def magichandler(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)