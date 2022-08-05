from telethon import TelegramClient, events
import handlers.client, handlers.dino
from handlers.dino import Dino
import time
dino = Dino()
client = handlers.client.client
@events.register(events.NewMessage)
async def dinohandlers(event):
		for i in range(8):
			
					if '.dino' in event.raw_text:
						time.sleep(0.3)
						for d in dino.dino:
							time.sleep(0.3)
							await event.edit(d)