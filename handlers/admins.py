from telethon import TelegramClient, events, sync 
from telethon.errors import rpcbaseerrors
import time
##
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location

from datetime import datetime
#
import random
import time
import os, sys
import asyncio
import random
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins

from datetime import datetime
from time import sleep
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import handlers.client
import time

client = handlers.client.client


@events.register(events.NewMessage(pattern=".admins"))
async def admins(event):
		if event.fwd_from:
			return
		mentions = "︎GURUH ADMINLARI\n"
		chat = await event.get_input_chat()
		async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
			mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
		reply_message = None
		if event.reply_to_msg_id:
			reply_message = await event.get_reply_message()
			await reply_message.reply(mentions)
		else:
			await event.reply(mentions)