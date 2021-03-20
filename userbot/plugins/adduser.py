""" Userbot module for adding users to group """

from telethon import functions
from userbot.events import register
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=r"add(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if not to_add_users and not reply:
        await event.edit("`You\'re missing ppl(\'s) ok?`")
    elif reply:
        to_add_users = str(reply.from_id)
    if to_add_users:
        if not event.is_group and not event.is_channel:
            return await event.edit("`.add` users to a chat, not to a Private Message")
        else:
            if not event.is_channel and event.is_group:
                # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
                for user_id in to_add_users.split(" "):
                    try:
                        userID = int(user_id)
                    except:
                        userID = user_id
                    try:
                        await event.client(
                            functions.messages.AddChatUserRequest(
                                chat_id=event.chat_id,
                                user_id=userID,
                                fwd_limit=1000000))
                    except Exception as e:
                        await event.reply(str(e))
                        return
                await event.edit("Added Successfully")
            else:
                # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
                for user_id in to_add_users.split(" "):
                    try:
                        userID = int(user_id)
                    except:
                        userID = user_id
                    try:
                        await event.client(
                            functions.channels.InviteToChannelRequest(
                                channel=event.chat_id, users=[userID]))
                    except Exception as e:
                        await event.reply(str(e))
                        return
                    await event.edit("Added Successfully")