from pyrogram import filters, Client
from pyrogram.errors import UserIsBlocked
from pyrogram.types import Message
from tgbot import tgbot as Mbot, SUDO_USERS, CMD
from pyrogram.types import ReplyKeyboardMarkup
    

@Mbot.on_message(filters.command("usend", CMD) & filters.user(SUDO_USERS)) # & filters.user(ADMINS)
async def send_msg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/usend"]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            user = await bot.get_users(int(target_id))
            await message.reply_to_message.copy(int(user.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Error :- <code>{e}</code></b>")
        if success:
            await message.reply_text(f"<b>Your message has been successfully send to {user.mention} User 👤.</b>")
        else:
            await message.reply_text("<b>Aɴ #Error Oᴄᴄᴜʀʀᴇᴅ !</b>")
    else:
        await message.reply_text("<b>Command Incomplete...</b>")

@Mbot.on_message(filters.command("gsend", CMD) & filters.user(SUDO_USERS))
async def send_chatmsg(bot, message):
    if message.reply_to_message:
        target_id = message.text
        command = ["/gsend"]
        for cmd in command:
            if cmd in target_id:
                target_id = target_id.replace(cmd, "")
        success = False
        try:
            chat = await bot.get_chat(int(target_id))
            await message.reply_to_message.copy(int(chat.id))
            success = True
        except Exception as e:
            await message.reply_text(f"<b>Error :- <code>{e}</code></b>")
        if success:
            await message.reply_text(f"<b>Your message has been successfully send to {chat.id} Group 👥.</b>")
        else:
            await message.reply_text("<b>Aɴ Eʀʀᴏʀ Oᴄᴄᴜʀʀᴇᴅ !</b>")
    else:
        await message.reply_text("<b>Cᴏᴍᴍᴀɴᴅ Iɴᴄᴏᴍᴘʟᴇᴛᴇ...</b>")
