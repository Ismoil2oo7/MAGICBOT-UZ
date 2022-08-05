from telethon import TelegramClient, events
import handlers.client, handlers.why
from handlers.why import Why
import time
why = Why()
client = handlers.client.client
@events.register(events.NewMessage)
async def whyhandlers(event):
					if '.why' in event.raw_text:
						time.sleep(0.3)
						for d in why.why:
							time.sleep(5)
							await event.edit(d)