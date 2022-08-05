#	U.T.C course
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
@events.register(events.NewMessage(pattern=".chatinfo(?: |$)(.*)", outgoing=True))
async def info(event):
    
    await event.edit("`Chat scanerlanmoqda...`")
    chat = await get_chatinfo(event)
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`Kutilmagan xatolik yuz berdi.`")
    return


async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`Kanal yoki guruhda qandaydir xatolik kuzatildi..`")
            return None
        except ChannelPrivateError:
            await event.edit("`Bu shaxsiy kanal/guruh yoki menga u yerdan kirish taqiqlangan`")
            return None
        except ChannelPublicGroupNaError:
            await event.edit("`Kanal yoki superguruh mavjud emas`")
            return None
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return chat_info


async def fetch_info(chat, event):
    # chat.chats is a list so we use get_entity() to avoid IndexError
    chat_obj_info = await event.client.get_entity(chat.full_chat.id)
    broadcast = chat_obj_info.broadcast if hasattr(chat_obj_info, "broadcast") else False
    chat_type = "KANAL" if broadcast else "Guruh"
    chat_title = chat_obj_info.title
    warn_emoji = emojize(":warning:")
    try:
        msg_info = await event.client(GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1), 
                                                        add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception as e:
        msg_info = None
        print("Exception:", e)
    # No chance for IndexError as it checks for msg_info.messages first
    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    # Same for msg_info.users
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Ochirilgan hisob"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    try:
        dc_id, location = get_input_location(chat.full_chat.chat_photo)
    except Exception as e:
        dc_id = "Nomalum"
        location = str(e)
    
    #this is some spaghetti I need to change
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    members_online = chat.full_chat.online_count if hasattr(chat.full_chat, "online_count") else 0
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    exp_count = chat.full_chat.pts if hasattr(chat.full_chat, "pts") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info  # this is a list
    bots = 0
    supergroup = "<b>Yes</b>" if hasattr(chat_obj_info, "megagroup") and chat_obj_info.megagroup else "No"
    slowmode = "<b>Yes</b>" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "No"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "<b>Yes</b>" if hasattr(chat_obj_info, "cheklangan") and chat_obj_info.restricted else "No"
    verified = "<b>Yes</b>" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "No"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None
    #end of spaghetti block
    
    if admins is None:
        # use this alternative way if chat.full_chat.admins_count is None, works even without being an admin
        try:
            participants_admins = await event.client(GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                                                            offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b>CHAT SCANNERI:</b>\n"
    caption += f"ID: <code>{chat_obj_info.id}</code>\n"
    if chat_title is not None:
        caption += f"{chat_type} name: {chat_title}\n"
    if former_title is not None:  # Meant is the very first title
        caption += f"Former name: {former_title}\n"
    if username is not None:
        caption += f"{chat_type} turi: ochiq\n"
        caption += f"Link: {username}\n"
    else:
        caption += f"{chat_type} turi: yopiq\n"
    if creator_username is not None:
        caption += f"KANAL YARATUVCHISI: {creator_username}\n"
    elif creator_valid:
        caption += f"kanal yaratuvchisi: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created is not None:
        caption += f"kanal yaratilgan: <code>{created.date().strftime('%b %d, %Y')} - {created.time()}</code>\n"
    else:
        caption += f"kanal yaratilgan: <code>{chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}</code> {warn_emoji}\n"
    caption += f"Data Centre ID: {dc_id}\n"
    if exp_count is not None:
        chat_level = int((1+sqrt(1+7*exp_count/14))/2)
        caption += f"{chat_type} darajasi: <code>{chat_level}</code>\n"
    if messages_viewable is not None:
        caption += f"korilgan xabarlar: <code>{messages_viewable}</code>\n"
    if messages_sent:
        caption += f"yuborilgan habarlar: <code>{messages_sent}</code>\n"
    elif messages_sent_alt:
        caption += f"yuborilgan habarlar: <code>{messages_sent_alt}</code> {warn_emoji}\n"
    if members is not None:
        caption += f"azolar: <code>{members}</code>\n"
    if admins is not None:
        caption += f"Administratorlar: <code>{admins}</code>\n"
    if bots_list:
        caption += f"Botlar: <code>{bots}</code>\n"
    if members_online:
        caption += f"hozir online: <code>{members_online}</code>\n"
    if restrcited_users is not None:
        caption += f"cheklangan foydalanuvchilar: <code>{restrcited_users}</code>\n"
    if banned_users is not None:
        caption += f"taqiqlangan foydalanuvchilar: <code>{banned_users}</code>\n"
    if group_stickers is not None:
        caption += f"{chat_type} stickerlar: <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a>\n"
    caption += "\n"
    if not broadcast:
        caption += f"Sekin rejim: {slowmode}"
        if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
            caption += f", <code>{slowmode_time}s</code>\n\n"
        else:
            caption += "\n\n"
    if not broadcast:
        caption += f"Superguruh: {supergroup}\n\n"
    if hasattr(chat_obj_info, "restricted"):
        caption += f"Restricted: {restricted}\n"
        if chat_obj_info.restricted:
            caption += f"> platforma: {chat_obj_info.restriction_reason[0].platform}\n"
            caption += f"> sabab: {chat_obj_info.restriction_reason[0].reason}\n"
            caption += f"> Text: {chat_obj_info.restriction_reason[0].text}\n\n"
           
            
        else:
            caption += "\n"
    if hasattr(chat_obj_info, "~~firibgarlik~~") and chat_obj_info.scam:
    	caption += "~~firibgarlik~~: <b>Yes</b>\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"Telegram tomonidan tasdiqlanganmi,m: {verified}\n\n"
    if description:
        caption += f"Tavfsif: \n<code>{description}</code>\n"
    return caption
    

	

