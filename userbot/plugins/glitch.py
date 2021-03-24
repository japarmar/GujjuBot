#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    Sorry :(
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os

from telethon.tl.types import MessageMediaPhoto

from userbot.utils import admin_cmd

import asyncio

try:
    from glitch_this import ImageGlitcher
except:
    os.system("pip install glitch_this")
    from glitch_this import ImageGlitcher

glitcher = ImageGlitcher()
DURATION = 200  # Set this to however many centiseconds each frame should be visible for
LOOP = 0  # Set this to how many times the gif should loop
# LOOP = 0 means infinite loop
sedpath = "./Anmol-dot283/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@borg.on(admin_cmd(pattern=r"glitch"))
async def glitch(event):
    sed = await event.get_reply_message()
    okbruh = await event.edit("`Gli, Glitchiiingggg.....`")
    try:
        if isinstance(sed.media, MessageMediaPhoto):
            photolove = await borg.download_media(sed.media, sedpath)
        elif "image" in response.media.document.mime_type.split("/"):
            photolove = await borg.download_media(sed.media, sedpath)
        else:
            await event.edit("`Reply To Image`")
            return        
        fmt = "gif"
        pathsn = f"./Anmol-dot283/@blacklightningot.{fmt}"
        glitch_imgs = glitcher.glitch_image(photolove, 2, gif=True, color_offset=True)
        glitch_imgs[0].save(
            pathsn,
            format="GIF",
            append_images=glitch_imgs[1:],
            save_all=True,
            duration=DURATION,
            loop=LOOP,
        )
        await borg.send_file(event.chat_id, pathsn)
        await event.delete()
        await okbruh.delete()
        for starky in (pathsn, photolove):
            if starky and os.path.exists(starky):
                os.remove(starky)
    except:
        await event.edit("Something went wrong")
        asyncio.sleep(3)
        await event.delete()