import logging

from tgbot import tgbot as Bot

from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

logger = logging.getLogger(__name__)

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

@Bot.on_message(filters.command('start') & filters.private)
async def start_handler(bot, message):
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
