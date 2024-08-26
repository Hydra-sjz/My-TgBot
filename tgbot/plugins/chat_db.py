from pyrogram import Client, filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from tgbot import tgbot as bot
from tgbot.utils.chat_db import database
 
from tgbot.utils.chat_db import MongoDb
# from bot.helpers.decorators import ratelimiter
from asyncio import sleep


from tgbot.logging import LOGGER

@Client.on_message(filters.command("chatst"))
async def dbstabbts(_, message: Message):
    """
    Returns database stats of MongoDB, which includes Total number
    of bot user and total number of bot chats.
    """ 
    #TotalUsers = await MongoDb.users.total_documents()
    TotalChats = await MongoDb.chats.total_documents()
    
    stats_string = f"**Bot Database Statics.\nTotal number of chats**  = {TotalChats}"
    return await message.reply_text(stats_string)


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
            



@Client.on_message(filters.command(["bc"]))
async def broadcast(_: Client, message: Message):
    """
    Broadcast the message via bot to bot users and groups..
    """

    if not (broadcast_msg := message.reply_to_message):
        broadcast_usage = f"Reply with command /broadcast to the message you want to broadcast.\n\n/broadcast users - To broadcast message to users only.\n\n/broadcast chats - To broadcast message to chats only.\n\n/broadcast all - To broadcast message everywhere."
        return await message.reply_text(broadcast_usage, quote=True)

    proses_msg = await message.reply_text(
        "**Broadcasting started. Please wait for few minutes for it to get completed.", quote=True)

    to_chats = False
    to_users = False
    disable_notification = True
    commands = message.command

    if len(commands) > 3:
        return await proses_msg.edit("Invalid Command")

    for command in message.command:
        if command.lower() == "all":
            to_chats = True
            to_users = True
        elif command.lower() == "users":
            to_users = True
            to_chats = False
        elif command.lower() == "chats":
            to_users = False
            to_chats = True
        elif command.lower() == "loud":
            disable_notification = False

    total_list = []
    if to_chats:
        total_list += await MongoDb.chats.get_all_id()

    if to_users:
        total_list += await MongoDb.users.get_all_id()

    failed = 0
    success = 0

    for __id in total_list:
        try:
            await broadcast_msg.copy(
                __id, broadcast_msg.caption, disable_notification=disable_notification)
            success += 1
            # preventing flood wait
            await sleep(0.3)
        except Exception as error:
            LOGGER(__name__).error(str(error))
            failed += 1

    return await proses_msg.edit(
        f"**The message has been successfully broadcasted.**\n\nTotal success = {success}\nTotal Failure = {failed}") 
