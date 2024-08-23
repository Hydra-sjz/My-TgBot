from pyrogram import filters
import asyncio
import pyfiglet 
from random import choice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.handlers import MessageHandler
from tgbot import tgbot as app



def figle(text):
    x = pyfiglet.FigletFont.getFonts()
    font = choice(x)
    figled = str(pyfiglet.figlet_format(text,font=font))
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="🔄Change🔄", callback_data="figlet"),InlineKeyboardButton(text="❌ Close", callback_data="close")]])
    return figled, keyboard

@app.on_message(filters.command("figlet"))
async def echo(bot, message):
    global text
    try:
        text = message.text.split(' ',1)[1]
    except IndexError:
        return await message.reply_text("Example:`/figlet Gojo`")
    kul_text, keyboard = figle(text)
    await message.reply_text(f"Here is your Figlet.\n<pre>{kul_text}</pre>", quote=True, reply_markup=keyboard)

@app.on_callback_query(filters.regex("figlet"))
async def figlet_handler(Client, query: CallbackQuery):
  try:
      kul_text, keyboard = figle(text)
      await query.message.edit_text(f"Here is your Figlet.\n<pre>{kul_text}</pre>", reply_markup=keyboard)
  except Exception as e : 
      await message.reply(e)
