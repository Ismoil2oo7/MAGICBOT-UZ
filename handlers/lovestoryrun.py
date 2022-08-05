from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.lovestory import Lovestory
import time
lovestory = Lovestory()
client = handlers.client.client
@events.register(events.NewMessage)
async def lovestoryhandler(event):
			
					if '.sexstory' in event.raw_text:
						time.sleep(1)
						for d in lovestory.lovestory:
							time.sleep(1)
							await event.edit(d)