import logging

from tgbot import tgbot as Bot, LOG_CHANNEL_ID

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from tgbot.utils.broadcast_db.broadcast import broadcast
from tgbot.utils.broadcast_db.check_user import handle_user_status
from tgbot.utils.broadcast_db.database import Database
from config import AUTH_USERS, DB_URL, DB_NAME


logger = logging.getLogger(__name__)


#from anibot.data import *

db = Database(DB_URL, DB_NAME)

ST = """
➡️ **☠️LOG STURO☠️** ⬅️

📛**Triggered Command** : /start 
👤**Name** : {}
👾**Username** : @{}
💾**DC** : {}
♐**ID** : `{}`
🤖**BOT** : @GojoSatoru_Xbot
➕➕➕➕➕➕➕➕➕➕➕➕➕
"""



#=============START_CMD====================
text_st = (
   "Hello {},"
   "Welcome to the 𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡! "
   "This is a powerful bot for Telegram.\n\n"
   "Click help to know how to use me!"
)
buttons_st = [[
    InlineKeyboardButton('Channel 📢', url='https://t.me/XBOTS_X'),
    InlineKeyboardButton('Commands 📚', callback_data='help'),
    InlineKeyboardButton('About 💡', callback_data='abot')
    ],[
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_message(filters.private)
async def _(bot, cmd):
    await handle_user_status(bot, cmd)
@Bot.on_message(filters.command('start') & filters.private)
async def start_handler(bot, message):
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await client.get_me()
        await db.add_user(chat_id)
        if LOG_CHANNEL:
            await client.send_message(
                LOG_CHANNEL,
                f"🥳NEWUSER🥳 \n\n😼New User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) 😹started @spotifysavetgbot !!",
            )
        else:
            logging.info(f"🥳NewUser🥳 :- 😼Name : {message.from_user.first_name} 😹ID : {message.from_user.id}")
    await bot.send_message(LOG_CHANNEL_ID, ST.format(message.from_user.mention, message.from_user.username, message.from_user.dc_id, message.from_user.id))
    await message.reply_photo(
        photo="https://telegra.ph/file/8fd3a9326d3f0ad19e2d8.jpg",
        caption=text_st.format(message.from_user.first_name), 
        reply_markup=InlineKeyboardMarkup(buttons_st), 
        quote=True,
    )
@Bot.on_callback_query(filters.regex('^home$'))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=text_st.format(query.from_user.first_name), 
        reply_markup=InlineKeyboardMarkup(buttons_st),
        disable_web_page_preview=True
    )


#=============HELP_CMD====================
text_hp = (
    "**It's very simple to use me! 😉**\n\n"
    "test."
)
buttons_hp = [[
    InlineKeyboardButton('⬅️', callback_data='home'),
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_message(filters.command('help') & filters.private)
async def hp_handler(bot, message):
    await message.reply_text(
        text=text_hp, 
        reply_markup=InlineKeyboardMarkup(buttons_hp), 
        quote=True,
    )
@Bot.on_callback_query(filters.regex('^help$'))
async def help_handler(bot, query):
    await query.message.edit(
        text=text_hp, 
        reply_markup=InlineKeyboardMarkup(buttons_hp),
        disable_web_page_preview=True
   )

#=============ABOUT_CMD====================
text_ab = (
    "🎈 **AbouT Me** 🎈\n\n"
    "**🤖 Bot Name:**  𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡!\n"
    "**📝 Language:** [Python 3](https://www.python.org/)\n"
    "**🧰 Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n"
    "**👨‍💻 Developer:** [VGX.LEO](https://t.me/Vignesh_leo)\n"
    "**📢 Updates Channel:** [X Bots](https://t.me/Xbots_x)\n"
    "**👥 Support Group:** [X Support](https://t.me/sp)\n"
)
buttons_ab = [[
    InlineKeyboardButton('⬅️', callback_data='home'),
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_message(filters.command('about') & filters.private)
async def hp_handler(bot, message):
    await message.reply_text(
        text=text_ab, 
        reply_markup=InlineKeyboardMarkup(buttons_ab), 
        quote=True,
    )
@Bot.on_callback_query(filters.regex('^abot$'))
async def help_handler(bot, query):
    await query.message.edit(
        text=text_ab, 
        reply_markup=InlineKeyboardMarkup(buttons_ab),
        disable_web_page_preview=True
    )


#=================================
@Bot.on_callback_query(filters.regex('^close$'))
async def close_cb(bot, callback):
    await callback.answer("👋Hey i am Gojo Satoru 𝕏 Bot")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
