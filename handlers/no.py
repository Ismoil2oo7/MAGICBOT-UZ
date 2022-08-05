from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.texts import Texts
import time
texts = Texts()
client = handlers.client.client
@events.register(events.NewMessage)
async def nohandlers(event):
		#for i in range(8):
					if '.no' in event.raw_text:
						time.sleep(0.3)
						for d in texts.No:
							time.sleep(0.3)
							await event.edit(d)