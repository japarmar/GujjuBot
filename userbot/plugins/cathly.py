from PIL import Image
import sys
import os
from userbot.utils import admin_cmd
from userbot import bot 
from userbot import bot as borg
if not os.path.isdir("./thug/"):
    os.makedirs("./thug/")

#made by  @THE_B_LACK_HAT Some errors solved by Sh1vam

@bot.on(admin_cmd(pattern=r"cthug"))
async def scan(event):
    path = "thug"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)

    import cv2

    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
    
    os.system('wget https://telegra.ph/file/2369a71cc9c8b47a85735.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "2369a71cc9c8b47a85735.png"
    
    ##cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "thug.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
if not os.path.isdir("./pro/"):
    os.makedirs("./pro/")


@bot.on(admin_cmd(pattern=r"cpro"))
async def scan(event):
    path = "pro"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2
    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
  
    
    os.system('wget https://telegra.ph/file/f061c861ba85fbb23a51e.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "f061c861ba85fbb23a51e.png"
    
    ##cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "pro.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
if not os.path.isdir("./old/"):
    os.makedirs("./old/")


@bot.on(admin_cmd(pattern=r"cold"))
async def scan(event):
    path = "old"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2
    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
    
    os.system('wget https://telegra.ph/file/55fcb205c6f8f4790585e.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "55fcb205c6f8f4790585e.png"
    
    ##cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "old.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)




if not os.path.isdir("./cprotect/"):
    os.makedirs("./cprotect/")




@bot.on(admin_cmd(pattern=r"ccprotect"))
async def scan(event):
    path = "cprotect"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2
    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
   
    
    os.system('wget https://telegra.ph/file/b934a713abb321bd1a9fe.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "b934a713abb321bd1a9fe.png"
    
    #cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "cprotect.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
			
if not os.path.isdir("./hide/"):
    os.makedirs("./hide/")


@bot.on(admin_cmd(pattern=r"cgold"))
async def scan(event):
    path = "hide"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
    
    os.system('wget https://telegra.ph/file/4cc40d1e0846667488341.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "4cc40d1e0846667488341.png"
    
    #cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "hide.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
if not os.path.isdir("./coverit/"):
    os.makedirs("./coverit/")


@bot.on(admin_cmd(pattern=r"ccoverit"))
async def scan(event):
    path = "coverit"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
    
    os.system('wget  https://telegra.ph/file/df2d739544595ae337642.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "df2d739544595ae337642.png"
    
    #cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "coverit.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
if not os.path.isdir("./krish/"):
    os.makedirs("./krish/")


@bot.on(admin_cmd(pattern=r"ckrish"))
async def scan(event):
    path = "krish"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()  
    
    os.system('wget https://telegra.ph/file/54d2a267d411951b41a20.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "54d2a267d411951b41a20.png"
    
    #cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "krish.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)
if not os.path.isdir("./masks/"):
    os.makedirs("./masks/")


@bot.on(admin_cmd(pattern=r"cmasks"))
async def scan(event):
    path = "masks"
     
    kk = await event.delete()

    reply = await event.get_reply_message()
    
    lol = await borg.download_media(reply.media, path)


    import cv2

    img = cv2.VideoCapture(lol) 
    tales, miraculous = img.read()
    
    os.system('wget https://telegra.ph/file/f20fa37a521aaedc11bd5.png')

    imagePath = cv2.imwrite("shivamcat.jpg", miraculous)
    
    maskPath = "f20fa37a521aaedc11bd5.png"
    
    #cascPath = "haarcascade_frontalcatface.xml"
   
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
   
    image = cv2.imread("shivamcat.jpg")
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    faces = faceCascade.detectMultiScale(gray, 1.15)
   
    background = Image.open("shivamcat.jpg")
   
    for (x, y, w, h) in faces:
        mask = Image.open(maskPath)
        mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(mask, offset, mask=mask)
   
    file_name = "masks.png"
   
    hehe = path + "/" + file_name
   
    background.save(hehe, "PNG")
   
    await borg.send_file(event.chat_id, hehe)
   

    for files in (hehe, lol):
        if files and os.path.exists(files):
            os.remove(files)


