from pyrogram import filters, enums
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

import logging
import asyncio
from tgbot import tgbot as Bot, LOG_CHANNEL_ID, SUDO_USERS



text_st = (
   "👋😄__Hello {},__\n\n"
   "<blockquote> Welcome to the 🎈𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡! This is a powerful⚡🌪️ bot for Telegram.</blockquote>\n\n"
   "**__Click help to know how to use me!__**"
)
buttons_st = [[
    InlineKeyboardButton('Channel 📢', url='https://t.me/XBOTS_X'),
    InlineKeyboardButton('Commands 📚', callback_data='help'),
    InlineKeyboardButton('About 💡', callback_data='abot'),
    InlineKeyboardButton('Sudo 👥', callback_data='sudo')
    ],[
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_callback_query(filters.regex('^home$'))
async def st_cb_handler(bot, query):
    await query.message.edit(
        text=text_st.format(query.from_user.first_name), 
        reply_markup=InlineKeyboardMarkup(buttons_st),
        disable_web_page_preview=True
    )


#=============HELP_CMD====================
text_hp = (
    "**__Hey👋😁 {}!__**\n\n"
    "<blockquote>Are you Ready to explore?\n"
    "Click the button below to discover my commands!</blockquote>"
)
buttons_hp = [[
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_message(filters.command('help') & filters.private)
async def hp_handler(bot, message):
    await message.reply_text(
        text=text_hp.format(message.from_user.first_name), 
        reply_markup=InlineKeyboardMarkup(buttons_hp), 
        quote=True,
    )
@Bot.on_callback_query(filters.regex('^help$'))
async def help_cb_handler(bot, query):
    await query.message.edit(
        text=text_hp.format(query.from_user.first_name), 
        reply_markup=InlineKeyboardMarkup(buttons_hp),
        disable_web_page_preview=True
   )

#=============ABOUT_CMD====================
text_ab = (
    "🎈 **AbouT Me** 🎈\n\n"
    "<blockquote expandable>**🤖 Bot Name:**  𝐺𝑜𝑗𝑜 𝑆𝑎𝑡𝑜𝑟𝑢 𝕏 | 𝐵𝑜𝑡!\n"
    "**📝 Language:** [Python 3](https://www.python.org/)\n"
    "**🧰 Framework:** [Pyrogram](https://github.com/pyrogram/pyrogram)\n"
    "**👨‍💻 Developer:** [VGX.LEO](https://t.me/Vignesh_leo)\n"
    "**📢 Updates Channel:** [X Bots](https://t.me/Xbots_x)\n"
    "**👥 Support Group:** [X Support](https://t.me/sp)</blockquote>"
)
buttons_ab = [[
    InlineKeyboardButton('⬅️', callback_data='home'),
    InlineKeyboardButton('❌', callback_data='close')
]]
@Bot.on_message(filters.command('about') & filters.private)
async def ab_handler(bot, message): 
    await message.reply_text(
        text=text_ab, 
        reply_markup=InlineKeyboardMarkup(buttons_ab), 
        quote=True,
        parse_mode=enums.ParseMode.HTML
    )
@Bot.on_callback_query(filters.regex('^abot$'))
async def abot_cb_handler(bot, query):
    await query.message.edit(
        text=text_ab, 
        reply_markup=InlineKeyboardMarkup(buttons_ab),
        disable_web_page_preview=True
    )

#==============CLOSE===================
@Bot.on_callback_query(filters.regex('^close$'))
async def close_cb(bot, callback):
    await callback.answer("❌Closed the Module❌")
    await callback.message.delete()
    await callback.message.reply_to_message.delete()
#=================
SUDO_TEXT = """
Hi Sudo Bro 🤡🤣
"""

@Bot.on_callback_query(filters.regex("^sudo$"))
async def botCallbacks(_, CallbackQuery: CallbackQuery):
    clicker_user_id = CallbackQuery.from_user.id
    if clicker_user_id not in SUDO_USERS:
        return await CallbackQuery.answer(
            "You are not in the sudo user list.", show_alert=True)              
    await CallbackQuery.edit_message_text(
        SUDO_TEXT, reply_markup=InlineKeyboardMarkup(buttons_st))
