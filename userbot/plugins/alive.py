"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`നമസ്കാരം മച്ചാനെ ^.^ \nYour bot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @IAm_DarK_Angel\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     "[Sorry No Deploy Me](https://github.com/japa)")
