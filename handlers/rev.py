from telethon import TelegramClient, events
import handlers.client
import time
client = handlers.client.client

@events.register(events.NewMessage(outgoing=True , pattern=r'\.rev'))
async def reverseHandler(event):
	   	client = event.client
	   	if event.is_reply:
	   	   replied = await event.get_reply_message()
	   	   replied_msg_rev = replied.message[::-1]
	   	   await client.edit_message(event.message , replied_msg_rev)