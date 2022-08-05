from telethon import TelegramClient, events
import handlers.client, handlers.lul
from handlers.lul import Lul
import time
lul = Lul()
client = handlers.client.client
@events.register(events.NewMessage)
async def lulhandlers(event):
		for i in range(8):
			
					if '.lul' in event.raw_text:
						time.sleep(0.3)
						for d in lul.lul:
							time.sleep(0.3)
							await event.edit(d)