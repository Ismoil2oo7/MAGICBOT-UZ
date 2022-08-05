from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.lovestory import Lovestory
import time
lovestory = Lovestory()
client = handlers.client.client
@events.register(events.NewMessage(pattern='\.jjhhkkllmmnnoopp'))
async def infoconv(event):
		async for dailog in client.iter_dialogs():
			await event.reply(dailog.name + "chats id:" + str(dailog.id))
			await event.delete()