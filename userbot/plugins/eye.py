"""COMMAND : .eye"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(admin_cmd(pattern="eye"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    #input_str = event.pattern_match.group(1)

    #if input_str == "eye":

    await event.edit("👁👁")

    animation_chars = [

            "👁👁\n  👄  =====> നെയ്യാറ്റിൻകര നെരിപ്പൻമാരെ കാണാണ",
            "👁👁\n  👅  =====> കാണാനെങ്കിൽ വാ തമ്പാനൂരുവാ",    
            "👁👁\n  💋  =====> നമ്മടെ പയല്കളെ തൊട്ടാല",
            "👁👁\n  👄  =====> നമ്മടെ പെൺപിള്ളേരെ മുട്ടിയാല",
            "👁👁\n  👅  =====> പയലേ തുപ്പല് തൊട്ട് കൊട്ടടിച്ച്",    
            "👁👁\n  💋  =====> ചെവളെ കുത്തി നീരാക്കി",
            "👁👁\n  👄  =====> കൂമ്പിടിച്",
            "👁👁\n  👅  =====> സൂപ്പാക്കി വലിച്ചുകീറി ഒട്ടിക്കും",    
            "👁👁\n  💋  =====> Trivandrum ടാ ",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 103])
