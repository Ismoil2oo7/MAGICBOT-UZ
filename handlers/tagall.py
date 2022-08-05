from telethon import TelegramClient, events
import handlers.client
import time
client = handlers.client.client

@events.register(events.NewMessage(pattern=".tagall"))
async def tagall(event):
		if event.fwd_from:
			return
		mentions = "G︎URUH AZOLARI \n"
		chat = await event.get_input_chat()
		async for x in client.iter_participants(chat, 100):
			time.sleep(0.5)
			mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
			time.sleep(0.5)
			await event.edit(mentions)