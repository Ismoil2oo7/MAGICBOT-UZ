from telethon import TelegramClient, events
import handlers.client, handlers.kiss
from handlers.kiss import Kiss
import time
kiss = Kiss()
client = handlers.client.client
@events.register(events.NewMessage)
async def kisshandlers(event):
		for i in range(8):
			
					if '.kiss' in event.raw_text:
						time.sleep(0.3)
						for d in kiss.kiss:
							time.sleep(0.3)
							await event.edit(d)