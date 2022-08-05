from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.love import Love
import time
love = Love()
client = handlers.client.client
@events.register(events.NewMessage)
async def lovehandlers(event):
		for i in range(2):
			
					if '.love' in event.raw_text:
						time.sleep(0.3)
						for d in love.love:
							time.sleep(0.3)
							await event.edit(d)