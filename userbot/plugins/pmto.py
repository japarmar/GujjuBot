from userbot.utils import admin_cmd
from telethon.tl.functions.users import GetFullUserRequest
import asyncio


@borg.on(admin_cmd(pattern="pmto ?(.*)"))
async def pmto(event):
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        chat_id=await event.client(GetFullUserRequest(reply_message.from_id))
        msg = event.pattern_match.group(1)
        try:
            await borg.send_message(chat_id, msg)
            await event.edit("Message sent!")
            await asyncio.sleep(3)
            await event.delete()
        except BaseException:
            await event.edit("Something went wrong.")
    else:
        a = event.pattern_match.group(1)
        b = a.split(" ")
        chat_id = b[0]
        try:
            chat_id = int(chat_id)
        except BaseException:
            pass
        msg = ""
        for i in b[1:]:
            msg += i + " "
        if msg == "":
            return
        try:
            await borg.send_message(chat_id, msg)
            await event.edit("Message sent!")
            await asyncio.sleep(3)
            await event.delete()
        except BaseException:
            await event.edit("Something went wrong.")
