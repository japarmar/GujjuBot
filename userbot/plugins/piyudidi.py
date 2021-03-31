from userbot.utils import admin_cmd
import io
from telethon import events
from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
import asyncio

@bot.on(events.NewMessage(incoming=True, from_users=(1404547863)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    message = event.raw_text
    if message == ".gmute":
        if event.fwd_from:
            return        
        reply = await event.get_reply_message()
        if reply is not None:
            userid = reply.sender_id
        else:
            return await borg.send_message(chat, "Please reply to a user to gmute them.",reply_to=event.message)
        if userid == 1637626702:
            return await borg.send_message(chat, "Sorry didi, you can't mute me.. 😛😛😛😛😛",reply_to=event.message)
        
        chat_id = event.chat_id
        chat = await event.get_chat()
        if is_muted(userid, "gmute"):
            return await borg.send_message(chat,"This user is already gmuted",reply_to=event.message)
        try:
            mute(userid, "gmute")
        except Exception as e:
            await borg.send_message(chat,"Error occured!\nError is " + str(e),reply_to=event.message)
        else:
            if userid == 1404547863:
                await borg.send_message(chat, "Didi ne khud ko mute kiya.... Nacho re🥳🥳🥳🥳🥳",reply_to=event.message)
            else:
                await borg.send_message(chat,"Successfully gmuted that person by piyudidi😘😘",reply_to=event.message)
            
    elif message == ".ungmute":
        if event.fwd_from:
            return        
        reply = await event.get_reply_message()
        if reply is not None:
            userid = reply.sender_id
        else:
            return await borg.send_message(chat, "Please reply to a user to unmute them.",reply_to=event.message)
        chat_id = event.chat_id
        chat = await event.get_chat()
        if userid == 1637626702:
            return await borg.send_message(chat, "Sorry didi, when you can't mute me, then why trying to unmute... 😛😛😛😛😛",reply_to=event.message)
        if not is_muted(userid, "gmute"):
            return await borg.send_message(chat,"This user is not muted",reply_to=event.message)
        try:
            unmute(userid, "gmute")
        except Exception as e:
            await borg.send_message(chat,"Error occured!\nError is " + str(e),reply_to=event.message)
        else:
            if userid == 1404547863:
                await borg.send_message(chat, "Didi ne khud ko unmute kiya.... Nacho re🥳🥳🥳🥳🥳",reply_to=event.message)
            else:
                await borg.send_message(chat,"Successfully unmuted that person by piyudidi😘😘",reply_to=event.message)
