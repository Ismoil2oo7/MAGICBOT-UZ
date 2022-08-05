from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.ketdi import Ketdi
import time
ketdi = Ketdi()
client = handlers.client.client
@events.register(events.NewMessage)
async def ketdihandlers(event):
			
					if '.ketdim' in event.raw_text:
						time.sleep(0.3)
						for d in ketdi.ketdi:
							time.sleep(0.3)
							await event.edit(d)