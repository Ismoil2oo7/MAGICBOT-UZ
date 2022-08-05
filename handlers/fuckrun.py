from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.fuck import Fuck
import time
fuck = Fuck()
client = handlers.client.client
@events.register(events.NewMessage)
async def fuckhandlers(event):
		for i in range(8):
					if '.fuck' in event.raw_text:
						time.sleep(0.3)
						for d in fuck.fuck:
							time.sleep(0.3)
							await event.edit(d)