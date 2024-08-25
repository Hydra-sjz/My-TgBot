import logging
import asyncio
from tgbot import tgbot as Bot, LOG_CHANNEL_ID, SUDO_USERS

from pyrogram import filters, enums
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

@Bot.on_callback_query(filters.regex("^BUTTON$"))
async def botCallbacks(_, CallbackQuery: CallbackQuery):
    clicker_user_id = CallbackQuery.from_user.id
    if CallbackQuery.data == "sudo":
        if clicker_user_id not in SUDO_USERS:
            return await CallbackQuery.answer(
                "You are not in the sudo user list.", show_alert=True)              
        await CallbackQuery.edit_message_text(
            SUDO_TEXT, reply_markup=InlineKeyboardMarkup(buttons_st))




#==================•BROADCAST•==================
@Bot.on_message(filters.private & filters.command(["broadcast", "send", "b"]))
async def broadcast_handler_open(_, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if m.reply_to_message is None:
        await m.delete()
    else:
        await broadcast(m, db)

@Bot.on_message(filters.private & filters.command("stat"))
async def tsts(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    sat = await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        quote=True
    )
    await m.delete()
    await asyncio.sleep(180)
    await sat.delete()

@Bot.on_message(filters.private & filters.command("b_user"))
async def ban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to ban 🛑 any user from the bot 🤖.\n\nUsage:\n\n`/b_user user_id ban_duration ban_reason`\n\nEg: `/b_user 1234567 28 You misused me.`\n This will ban user with id `1234567` for `28` days for the reason `You misused me`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        ban_duration = int(m.command[2])
        ban_reason = " ".join(m.command[3:])
        ban_log_text = f"Banning user {user_id} for {ban_duration} days for the reason {ban_reason}."

        try:
            await c.send_message(
                user_id,
                f"You are Banned 🚫 to use this bot for **{ban_duration}** day(s) for the reason __{ban_reason}__ \n\n**Message from the admin 🤠**",
            )
            ban_log_text += "\n\nUser notified successfully!"
        except BaseException:
            traceback.print_exc()
            ban_log_text += (
                f"\n\n ⚠️ User notification failed! ⚠️ \n\n`{traceback.format_exc()}`"
            )
        await db.ban_user(user_id, ban_duration, ban_reason)
        print(ban_log_text)
        await m.reply_text(ban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True
        )

@Bot.on_message(filters.private & filters.command("unb_user"))
async def unban(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    if len(m.command) == 1:
        await m.reply_text(
            f"Use this command to unban 😃 any user.\n\nUsage:\n\n`/unb_user user_id`\n\nEg: `/unb_user 1234567`\n This will unban user with id `1234567`.",
            quote=True,
        )
        return

    try:
        user_id = int(m.command[1])
        unban_log_text = f"Unbanning user 🤪 {user_id}"

        try:
            await c.send_message(user_id, f"Your ban was lifted!")
            unban_log_text += "\n\n✅ User notified successfully! ✅"
        except BaseException:
            traceback.print_exc()
            unban_log_text += (
                f"\n\n⚠️ User notification failed! ⚠️\n\n`{traceback.format_exc()}`"
            )
        await db.remove_ban(user_id)
        print(unban_log_text)
        await m.reply_text(unban_log_text, quote=True)
    except BaseException:
        traceback.print_exc()
        await m.reply_text(
            f"⚠️ Error occoured ⚠️! Traceback given below\n\n`{traceback.format_exc()}`",
            quote=True,
        )

@Bot.on_message(filters.private & filters.command("b_users"))
async def banned_usrs(c, m):
    if m.from_user.id not in AUTH_USERS:
        await m.delete()
        return
    all_banned_users = await db.get_all_banned_users()
    banned_usr_count = 0
    text = ""
    async for banned_user in all_banned_users:
        user_id = banned_user["id"]
        ban_duration = banned_user["ban_status"]["ban_duration"]
        banned_on = banned_user["ban_status"]["banned_on"]
        ban_reason = banned_user["ban_status"]["ban_reason"]
        banned_usr_count += 1
        text += f"🆔**User_id** : `{user_id}`\n⏱️**Ban Duration** : `{ban_duration}`\n\n📆**Banned on** : `{banned_on}`\n\n💁**Reason**: `{ban_reason}`\n\n😌 @Musicx_dlbot"
    reply_text = f"Total banned user(s) 🤭: `{banned_usr_count}`\n\n{text}"
    if len(reply_text) > 4096:
        with open("banned-users.txt", "w") as f:
            f.write(reply_text)
        await m.reply_document("banned-users.txt", True)
        os.remove("banned-users.txt")
        return
    await m.reply_text(reply_text, True)
