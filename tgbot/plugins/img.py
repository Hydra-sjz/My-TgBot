import requests
from pyrogram import Client, filters
from tgbot import tgbot as app

@app.on_message(filters.command("magicimg"))
async def magicimg(client, message):
    prompt = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not prompt:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ɪᴍᴀɢᴇ.")
        return
    try:
        response = requests.get(f"https://magicimg.apiitzasuraa.workers.dev/?prompt={prompt}")
        response.raise_for_status()
        image_url = response.json().get("magicimg")
        if image_url:
            await message.reply_photo(photo=image_url, caption=f"ɢᴇɴᴇʀᴀᴛᴇᴅ sᴛʏʟᴇ ɪᴍᴀɢᴇ ғᴏʀ: {prompt}")
        else:
            await message.reply_text("No image found.")
    except Exception as e:
        await message.reply_text(f"Sorry, something went wrong: {e}")

@app.on_message(filters.command("aiimage"))
async def aiimage(client, message):
    prompt = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not prompt:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴀɴ ɪᴍᴀɢᴇ.")
        return
    try:
        response = requests.get(f"https://aiimage.apiitzasuraa.workers.dev/?prompt={prompt}")
        response.raise_for_status()
        image_url = response.json().get('image1')
        if image_url:
            await message.reply_photo(photo=image_url, caption=f"ɢᴇɴᴇʀᴀᴛᴇᴅ ɪᴍᴀɢᴇ ғᴏʀ: {prompt}")
        else:
            await message.reply_text("No image found.")
    except Exception as e:
        await message.reply_text(f"Sorry, something went wrong: {e}")

@app.on_message(filters.command("animeimg"))
async def animeimg(client, message):
    prompt = ' '.join(message.command[1:])
    if not prompt:
        await message.reply_text('ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ.')
        return
    try:
        response = requests.get(f"https://animeimg.apiitzasuraa.workers.dev/?prompt={prompt}")
        response.raise_for_status()
        image_url = response.json().get('image')
        if image_url:
            await message.reply_photo(photo=image_url, caption=f"ɢᴇɴᴇʀᴀᴛᴇᴅ ᴀɴɪᴍᴇ-sᴛʏʟᴇ ɪᴍᴀɢᴇ ғᴏʀ: {prompt}")
        else:
            await message.reply_text("No image found.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")

@app.on_message(filters.command("disneyimg"))
async def disneyimg(client, message):
    prompt = ' '.join(message.command[1:])
    if not prompt:
        await message.reply_text("ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴀ ᴘʀᴏᴍᴘᴛ.")
        return
    try:
        response = requests.get(f"https://disneyimg.apiitzasuraa.workers.dev/?prompt={prompt}")
        response.raise_for_status()
        image_url = response.json().get("image")
        if image_url:
            await message.reply_photo(photo=image_url, caption=f"ɢᴇɴᴇʀᴀᴛᴇᴅ ᴅɪsɴᴇʏ-sᴛʏʟᴇ ɪᴍᴀɢᴇ ғᴏʀ: {prompt}")
        else:
            await message.reply_text("No image found.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {e}")
