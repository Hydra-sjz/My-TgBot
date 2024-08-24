from telegraph import upload_file
from pyrogram import filters
from tgbot import tgbot as app, CMD
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "link"], CMD))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("make a link...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'Your link: {url}')

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"], CMD))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("make a link...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'Your link:  {url}')
