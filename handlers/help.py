from telethon import events, Button
import handlers.client
#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
with client as darknet:
				darknet.add_event_handler(handlers.greetings.greeting)

@botClient.on(events.InlineQuery)
async def iquery(query):
			if query.text == 'help':
							result = query.builder.article('Help', text = "~~https://t.me/MAGICBOT_UZ~~\n\nPLUGINLAR (funksiyalar) MENUSI", buttons=[
							
												[Button.inline("NedoQuote", data=b"test"), Button.inline("ALIVE",data=b"test2")],
												[Button.inline("QUOTE", data=b"test3"), Button.inline("MemosityQuote", data=b"test4")],
												[Button.inline("CHat Info", data=b"test5"), Button.inline("Count",data=b"test6")],
												[Button.inline("rev", data=b"test7"), Button.inline("tagall",data=b"test8")],
												[Button.inline("admins", data=b"test9"), Button.inline("type",data=b"test10")],
												[Button.inline("clone pic", data=b"test11"), Button.inline("premium plugin",data=b"test12"), Button.inline("ping", data=b"test13")],
												
												
												[Button.url("TELEGRAM KANALIMIZGA OBUNA BOʻLING", url="https://t.me/fox_baby_userbot")]
											
							
							])
							await query.answer([result])
#callbackquery
@botClient.on(events.CallbackQuery)
#nq
async def callback(event):
				if event.data== b'test':
								await event.answer("~~Textni rasm korinishidagi memga aylantiradi~~\nIshga tushurish: .nq", alert=True)
								#alive
				if event.data== b'test2':
								await event.answer("~~Userbotimiz haqida Malumotlar~~\nIshga tushurish: .alive", alert=True)
								#qq
				if event.data== b'test3':
								await event.answer("~~Textlarni sticker qilib beradi~~\nIshga tushurish: .qq", alert=True)
								#mq
				if event.data== b'test4':
								await event.answer("~~Textlarni sticker meme korinishida qilib beriadi~~\nIshga tushurish: .mq", alert=True)
								#chatinfo
				if event.data== b'test5':
								await event.answer("~~Telegram ommaviy chatlar hawida Toliq malumot beroladi~~\nIshga tushurish: .chatinfo", alert=True)
								#count
				if event.data== b'test6':
								await event.answer("~~Telegramda nechta kontagiz, nechta guruhiz, nechta kaanliz, nechta botiz bor ekanini korsatadi~~\nIshga tushurish: .count", alert=True)
				if event.data== b'test8':
								await event.answer("Guruhga yozselar hamma azolarni chaqiradi\nIshlatish: .tagall", alert=True)	
				if event.data== b'test10':
								await event.answer("Type moduli siz .type + biron soz yozsez uni write effecti bn yozilvotganday qiladi\nIshlatish: .type so'z", alert=True)
				if event.data== b'test9':
								await event.answer("Telegram guruhga .admins deb yzisez grdagi adminlarni chiwarib beradi\nIshlatish: .admins", alert=True)
				if event.data== b'test7':
								await event.answer("Rev moduli nomidan ham malum biron textga reply qib yozsez textni teskari qiberadi\nishlatish: .rev", alert=True)
				if event.data== b'test11':
								await event.answer("Kimgadir reply wib yozsez uni profel rasmini sizga avtomatik koʻchirib beradi\nishlatish: .picer", alert=True)		
				if event.data== b'test12':
								await event.answer("Premium modul uchun @films_uzru guruhiga 50 ta obunachi qoʻshish kerak\nPremium modul orqali siz Userbotimiz foydalanuvchilarini qaysi chatlarda bor ekanini scanerlay olasiz", alert=True)		
				if event.data== b'test13':
								await event.answer("Userbot Tezligini korsatadi\nIshlatish: .ping", alert=True)				

			
						
												
								
								#ishga tushurish
@events.register(events.NewMessage(outgoing=True, pattern=r'\.help'))
async def helphandler(event):
				results = await client.inline_query('@Btnbtnbtnbot', 'help')
				await results[0].click(event.chat_id)
	