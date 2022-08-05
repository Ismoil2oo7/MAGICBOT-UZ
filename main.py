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
os.system("clear")
print ("""

   *                     (                   )                       )  
 (  `     (      (       )\ )   (     (   ( /(   *   )            ( /(  
 )\))(    )\     )\ )   (()/(   )\  ( )\  )\())` )  /(        (   )\()) 
((_)()\((((_)(  (()/(    /(_))(((_) )((_)((_)\  ( )(_))___    )\ ((_)\  
(_()((_))\ _ )\  /(_))_ (_))  )\___((_)_   ((_)(_(_())|___|_ ((_) _((_) 
|  \/  |(_)_\(_)(_)) __||_ _|((/ __|| _ ) / _ \|_   _|    | | | ||_  /  
| |\/| | / _ \    | (_ | | |  | (__ | _ \| (_) | | |      | |_| | / /   
|_|  |_|/_/ \_\    \___||___|  \___||___/ \___/  |_|       \___/ /___|  
                                                                        

""")
#part1
import handlers.client, handlers.greetings, handlers.alive, handlers.nedoquote, handlers.quote, handlers.mquote, handlers.help, handlers.chatinfo, handlers.magicrun, handlers.nikal, handlers.lulrun, handlers.kissrun, handlers.whyrun	, handlers.uzbrun, handlers.count, handlers.type, handlers.tagall, handlers.rev, handlers.ahelp, handlers.dinorun, handlers.loverun, handlers.ketdim, handlers.policerun, handlers.fuckrun, handlers.what, handlers.brainrun, handlers.ok, handlers.yes, handlers.no, handlers.pic, handlers.pk, handlers.lovestoryrun, handlers.test, handlers.ping, handlers.admins

#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
with client as darknet:
				darknet.add_event_handler(handlers.greetings.greeting)
				
#alive
with client as darknet:
				darknet.add_event_handler(handlers.alive.alive)
				
#NedoQuote
with client as darknet:
				darknet.add_event_handler(handlers.nedoquote.quotehandler)
#quote
with client as darknet:
				darknet.add_event_handler(handlers.quote.quotehandler2)
#mquote
with client as darknet:
				darknet.add_event_handler(handlers.mquote.quotehandler3)
#help
with client as darknet:
				darknet.add_event_handler(handlers.help.helphandler)

#chatinfo
with client as darknet:
				darknet.add_event_handler(handlers.chatinfo.info)
#magic
with client as darknet:
				darknet.add_event_handler(handlers.magicrun.magichandler)
#nikal
with client as darknet:
				darknet.add_event_handler(handlers.nikal.nikalhandler)
#lul
with client as darknet:
				darknet.add_event_handler(handlers.lulrun.lulhandlers)
#kiss
with client as darknet:
				darknet.add_event_handler(handlers.kissrun.kisshandlers)
#why
with client as darknet:
				darknet.add_event_handler(handlers.whyrun.whyhandlers)
#uzb
with client as darknet:
				darknet.add_event_handler(handlers.uzbrun.uzbhandlers)
#count 
with client as darknet:
				darknet.add_event_handler(handlers.count.count)
#type
with client as darknet:
				darknet.add_event_handler(handlers.type.type)
#tagall
with client as darknet:
				darknet.add_event_handler(handlers.tagall.tagall)
				
#net yuq ligida tayorlanganlar
#					rev
with client as darknet:
				darknet.add_event_handler(handlers.rev.reverseHandler)
#ahelp
with client as darknet:
				darknet.add_event_handler(handlers.ahelp.ahelphandler)
#dino
with client as darknet:
				darknet.add_event_handler(handlers.dinorun.dinohandlers)
#love
with client as darknet:
				darknet.add_event_handler(handlers.loverun.lovehandlers)
#ketdim
with client as darknet:
				darknet.add_event_handler(handlers.ketdim.ketdihandlers)
#police
with client as darknet:
				darknet.add_event_handler(handlers.policerun.policehandlers)
#fuck
with client as darknet:
				darknet.add_event_handler(handlers.fuckrun.fuckhandlers)
#what
with client as darknet:
				darknet.add_event_handler(handlers.what.whathandlers)
#brain
with client as darknet:
				darknet.add_event_handler(handlers.brainrun.brainhandler)
#yes
with client as darknet:
				darknet.add_event_handler(handlers.yes.yeshandlers)
#ok
with client as darknet:
				darknet.add_event_handler(handlers.ok.okhandlers)
#no
with client as darknet:
				darknet.add_event_handler(handlers.no.nohandlers)
#picer
with client as darknet:
				darknet.add_event_handler(handlers.pic.picer)
#pc
with client as darknet:
				darknet.add_event_handler(handlers.pk.pkhandler)
#lovestory
with client as darknet:
				darknet.add_event_handler(handlers.lovestoryrun.lovestoryhandler)
#test
with client as darknet:
				darknet.add_event_handler(handlers.test.infoconv)
#ping
with client as darknet:
				darknet.add_event_handler(handlers.ping.pingHandler)
#admins
with client as darknet:
				darknet.add_event_handler(handlers.admins.admins)










loop = asyncio.get_event_loop()
client.start()
botClient.start()
loop.run_forever()

