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
from telethon.tl.functions.photos import UploadProfilePhotoRequest
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
import os


@events.register(events.NewMessage(outgoing=True, pattern=r'\.picer'))
async def picer(event):
    client = event.client
    if event.is_reply:
        replied = await event.get_reply_message()
        
        sender = replied.sender
        
        sender_profile_pic = await client.download_profile_photo(sender)
        await client(UploadProfilePhotoRequest(
            await client.upload_file(sender_profile_pic)
        ))
        await replied.reply("""
        Ushbu odamning profile rasmi sizga avtomatik tarzda Profelingizga kochirildi """)
        await event.message.delete()

is_pm_verified = [ ]