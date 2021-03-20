# USE !bin and send message then reply message .gen and get email
import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot
from userbot.events import register

#Module By @noobanon thnxkk bye :)
@register(outgoing=True, pattern="^.gen(?: |$)(.*)")
async def pembohong(gen):
    if gen.fwd_from:
        return 
    if not gen.reply_to_msg_id:
       await gen.edit("```Send Message !bin { Your Bin } then for generate cards !gen { bin } the reply your message with .gen ```")
       return
    reply_message = await gen.get_reply_message() 
    if not reply_message.text:
       await gen.edit("```Send Message !bin { Your Bin } then for generate cards !gen { bin } the reply your message with .gen```")
       return
    chat = "@CasperCarderBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await gen.edit("```Reply to actual users message.```")
       return
    await gen.edit("```Wait till Me Generate ```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=560528366))
              await bot.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await gen.reply("```Please unblock @CasperCarderBot and or use /start in @CasperCarderBot try again```")
              return
          if response.text.startswith("send"):
             await gen.edit("```can you kindly disable your forward privacy settings for good?```")
          else: 
             await gen.edit(f"{response.message.message}")