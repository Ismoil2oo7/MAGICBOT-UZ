from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.brain import Online
import time
brain = Online()
client = handlers.client.client
@events.register(events.NewMessage)
async def brainhandler(event):
		if '.brain' in event.raw_text:
			time.sleep(0.3)
			for d in brain.online:
				time.sleep(0.3)
				await event.edit(d)