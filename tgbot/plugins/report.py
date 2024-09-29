import os
from os import error
import pyrogram
from config import LOG_CHANNEL
from pyrogram import filters, Client, enums
from tgbot import CMD

A = """
🚨 **REPORT** 🚨
----------------------
👤**Name :** {}
🚹 **UserName :** @{}
🆔**User ID :** {}
🔗**Direct link :** {}

#report
----------------------
Else:- tg://openmessage?user_id={}„
--------------------------->
⬇️His Reported Message⬇️:"""

@Client.on_message(filters.command("report", CMD) | filters.command(["admins", "admin"], prefixes="@"))
async def report_me(bot, message):
    if message.reply_to_message:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        k = await message.reply_text("Processing your report...⏳", quote=True)
        await bot.send_message(LOG_CHANNEL, A.format(message.from_user.first_name, message.from_user.username, message.from_user.id, message.from_user.mention, message.from_user.id))
        await message.reply_to_message.forward(chat_id=LOG_CHANNEL)
        await k.edit_text("**Thanks for Reporting :)**\nI have forwarded your message to my Owner. He will reply you When ever he will be free.")
    else:
        await message.reply_text("**Please Send me a message** and Then Reply that message with `/report`, so that I can report that to my Owner.")
