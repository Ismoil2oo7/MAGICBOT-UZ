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

import handlers.client
client = handlers.client.client

@events.register(events.NewMessage(pattern=".count"))
async def count(event):
				if event.fwd_from:
								return
				start = datetime.now()
				u = 0
				g = 0
				c = 0
				bc = 0
				b = 0
				await event.edit("Telegram guruhlaringiz ,kanallaringiz, botlaringiz, kontaklaringiz hisoblanmoqda ....")
				async for d in client.iter_dialogs(limit=None):
								if d.is_user:
												if d.entity.bot:
																b += 1
												else:
																u += 1
								elif d.is_channel:
												if d.entity.broadcast:
																bc += 1
												else:
																c += 1
								elif d.is_group:
												g += 1
								else:
												logger.info(d.stringify())
				end = datetime.now()
				ms = (end - start).seconds
				await event.edit("""
Malumotlar {} soniyada olingan.
userlar:\t{}
guruhlar:\t{}
kanallar:\t{}
super guruhlar:\t{}
botlar:\t{}
				""".format(ms, u, g, c, bc, b))