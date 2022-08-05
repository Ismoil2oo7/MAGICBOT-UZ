from telethon import TelegramClient, events
import handlers.client, handlers.why
from handlers.uzb import Uzb
import time
uzb = Uzb()
client = handlers.client.client
@events.register(events.NewMessage)
async def uzbhandlers(event):
					if '.uzb' in event.raw_text:
						time.sleep(0.3)
						for d in uzb.uzb:
							time.sleep(0.6)
							await event.edit(d)