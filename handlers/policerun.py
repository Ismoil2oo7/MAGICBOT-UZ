from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.police import Police 
import time
police = Police()
client = handlers.client.client
@events.register(events.NewMessage)
async def policehandlers(event):
		for i in range(15):
			
					if '.police' in event.raw_text:
						time.sleep(0.3)
						for d in police.police:
							time.sleep(0.3)
							await event.edit(d)