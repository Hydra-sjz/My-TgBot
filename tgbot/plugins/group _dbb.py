from pyrogram import Client, filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from tgbot import tgbot as bot
from tgbot.utils.chat_db import database



@Client.on_message(filters.new_chat_members, group=1)
async def newChat(_, message: Message):
    """
    Get notified when someone add bot in the group, then saves that group chat_id
    in the database.
    """
    await message.reply_text("thanks for adding me here 🤩.")
    chatid = message.chat.id
    for new_user in message.new_chat_members:
        if new_user.id == bot.me.id:
            await database.saveChat(chatid)
            
