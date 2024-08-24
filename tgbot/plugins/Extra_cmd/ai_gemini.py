import os
import asyncio
import PIL.Image
from pathlib import Path
import google.generativeai as genai
from pyrogram import Client, filters, enums
from pyrogram.types import Message

from tgbot import tgbot as app, LOG_CHANNEL_ID as LOG_CHANNEL, CMD
from config import GEMINI_API

import time
import requests
from pyrogram.types import InputMediaPhoto
from MukeshAPI import api
from pyrogram.enums import ChatAction,ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
genai.configure(api_key=GEMINI_API)

generation_config_cook = {
  "temperature": 0.35,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1024,
}

model_text = genai.GenerativeModel("gemini-pro")
model = genai.GenerativeModel("gemini-pro-vision")
model_cook = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config_cook)
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
ASKAI = """
🫶**LOG ALERT FOR AI @GojoSatoru_Xbot**

📛**Triggered Command** : /askai {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#askai
"""

IMGTT = """
🍃**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aii {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#aii #ImageToTextmaker
"""

AICOOK = """
🕵️**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aicook {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#aicook #ReplayToimgToCook
"""

AISELL = """
👾**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aiseller {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#askai #ReplyToimgToselle
"""

AI_IMAGIN = """
👾**LOG ALERT FOR AI**👾

📛**Triggered Command** : /aiseller {}
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot AI

#askai #ReplyToimgToselle
"""

#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×


buttons_aski = [[
    InlineKeyboardButton('❌', callback_data='close')
]]
@app.on_message(filters.command(["askai"], CMD))
async def say_ask(bot, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait...</code>")

        if len(message.command) > 1:
         prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
         prompt = message.reply_to_message.text
        else:
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/askai [prompt/reply to message]</code>"
        )
         return

        chat = model_text.start_chat()
        response = chat.send_message(prompt)
        await i.delete()

        await message.reply_text(f"**Question:** {prompt}\n**Answer:** {response.text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", reply_markup=InlineKeyboardMarkup(buttons_aski), quote=True, parse_mode=enums.ParseMode.MARKDOWN)
        await bot.send_message(LOG_CHANNEL, ASKAI.format(prompt, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    except Exception as e:
        await i.delete()
        await message.reply_text(f"An error occurred: {str(e)}")

      
buttons_aii = [[
    InlineKeyboardButton('❌', callback_data='close')
]]
@app.on_message(filters.command(["aii"], CMD))
async def getaie(bot, message: Message):
    try:
        i = await message.reply_text("<code>Please Wait. Extracting image...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)

        response = model.generate_content(img)
        await i.delete()

        await message.reply_text(
            f"**Detail Of Image:** {response.parts[0].text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", reply_markup=InlineKeyboardMarkup(buttons_aii), quote=True, parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.send_message(LOG_CHANNEL, IMGTT.format(base_img, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(str(e))




@app.on_message(filters.command(["aicook"], CMD))
async def say_cook(bot, message: Message):
    try:
        i = await message.reply_text("<code>Some thing Cooking. please wait...</code>")

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        cook_img = [
        "Accurately identify the baked good in the image and provide an appropriate and recipe consistent with your analysis. ",
        img,
        ]

        response = model_cook.generate_content(cook_img)
        await i.delete()

        await message.reply_text(
            f"{response.text}\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.send_message(LOG_CHANNEL, AICOOK.format(base_img, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"please reply to an image.")




buttons_sell = [[
    InlineKeyboardButton('❌', callback_data='close')
]]
@app.on_message(filters.command(["aiseller"], CMD))
async def say_sell(bot, message: Message):
    try:
        i = await message.reply_text("<code>Generating your request. please wait...</code>")
        if len(message.command) > 1:
         taud = message.text.split(maxsplit=1)[1]
        else:
         await i.delete()
         await message.reply_text(
            f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>"
        )
         return

        base_img = await message.reply_to_message.download()

        img = PIL.Image.open(base_img)
        sell_img = [
        "Given an image of a product and its target audience, write an engaging marketing description",
        "Product Image: ",
        img,
        "Target Audience: ",
        taud
        ]

        response = model.generate_content(sell_img)
        await i.delete()

        await message.reply_text(
            f"<blockquote expandable>{response.text}</blockquote>\n\n**Powered by**: @XBOTS_X | ©️ @GojoSatoru_Xbot", reply_markup=InlineKeyboardMarkup(buttons_sell), quote=True, parse_mode=enums.ParseMode.MARKDOWN
        )
      
        await bot.send_message(LOG_CHANNEL, AISELL.format(taud, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
        os.remove(base_img)
    except Exception as e:
        await i.delete()
        await message.reply_text(f"<b>Usage: </b><code>/aiseller [target audience] [reply to product image]</code>")
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
#=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×
captionim = """
<b>Your prompt</b>

<i>{}</i>
 
<b>Powered by: @XBOTS_X | ©️ @GojoSatoru_Xbot</b>
"""
buttons_imgin = [[
    InlineKeyboardButton('❌', callback_data='close')
]]
@app.on_message(filters.command(["imagine"], CMD))
async def imagine_(b, message: Message):
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:

        text =message.text.split(None, 1)[1]
    mukesh=await message.reply_text( "`Please wait...,\n\nGenerating prompt .. ...`")
    try:
        await b.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        x=api.ai_image(text)
        with open("mukesh.jpg", 'wb') as f:
            f.write(x)
  
        await mukesh.delete()
        await message.reply_photo("mukesh.jpg", caption=captionim.format(text), reply_markup=InlineKeyboardMarkup(buttons_imgin), quote=True, parse_mode=enums.ParseMode.HTML)
        await bot.send_message(LOG_CHANNEL, AI_IMAGIN.format(text, message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    except Exception as e:
        await mukesh.edit_text(f"error {e}")

@app.on_message(filters.command(["mai","mask"], CMD))
async def chat_mgpt(bot, message):
    
    try:
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt Where is TajMahal?`")
        else:
            a = message.text.split(' ', 1)[1]
            r=api.gemini(a)["results"]
            await message.reply_text(f" {r} \n\n**Powered by: @XBOTS_X | ©️ @GojoSatoru_Xbot** ")     
    except Exception as e:
        await message.reply_text(f"**#Error: {e} ")
      
