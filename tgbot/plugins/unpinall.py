from pyrogram import filters, enums
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatPermissions
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    UserAdminInvalid,
    BadRequest
)

import datetime
from tgbot import app, CMD




@app.on_message(filters.command(["unpinall"]) & filters.group)
async def pin(_, message: Message):
    if message.command[0] == "unpinall":
        return await message.reply_text(
            "Aʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜɴᴘɪɴ ᴀʟʟ ᴍᴇssᴀɢᴇs?",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ʏᴇs", callback_data="unpin_yes"),
                        InlineKeyboardButton(text="ɴᴏ", callback_data="unpin_no"),
                    ],
                ]
            ),
        )


@app.on_callback_query(filters.regex(r"unpin_(yes|no)"))
async def callback_query_handler(_, query: CallbackQuery):
    if query.data == "unpin_yes":
        await app.unpin_all_chat_messages(query.message.chat.id)
        return await query.message.edit_text("Aʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀᴠᴇ ʙᴇᴇɴ ᴜɴᴘɪɴɴᴇᴅ.")
    elif query.data == "unpin_no":
        return await query.message.edit_text(
            "Uɴᴘɪɴ ᴏғ ᴀʟʟ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ʜᴀs ʙᴇᴇɴ ᴄᴀɴᴄᴇʟʟᴇᴅ."
        )
        



"""
@app.on_callback_query(filters.regex(r"^unpin"))
async def unpin_callbacc(client, CallbackQuery):
    user_id = CallbackQuery.from_user.id
    name = CallbackQuery.from_user.first_name
    chat_id = CallbackQuery.message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            await CallbackQuery.answer("You dont have rights, baka!", show_alert=True)
            return
    else:
        await CallbackQuery.answer("You dont have rights, baka!", show_alert=True)
        return
    
    msg_id = CallbackQuery.data.split("=")[1]
    try:
        msg_id = int(msg_id)
    except:
        if msg_id == "yes":
            await client.unpin_all_chat_messages(chat_id)
            textt = "I have unpinned all the pinned messages"
        else:
            textt = "Ok, i wont unpin all the messages"

        await CallbackQuery.message.edit_caption(
            textt,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Delete", callback_data="delete_btn=admin")]
                ]
            )
        )
        return
        
    await client.unpin_chat_message(chat_id, msg_id)
    await CallbackQuery.message.edit_caption(
        "unpinned!!", 
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Delete", callback_data="delete_btn=admin")]
            ]
        )
    )


@app.on_message(filters.command(["unpinall"], CMD))
async def unpin_command_handler(client, message):
    chat = message.chat
    chat_id = chat.id
    admin_id = message.from_user.id
    admin_name = message.from_user.first_name
    member = await chat.get_member(admin_id)
    if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER:
        if member.privileges.can_pin_messages:
            pass
        else:
            msg_text = "Yᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴘɪɴ sᴏᴍᴇᴛʜɪɴɢ"
            return await message.reply_text(msg_text)
    else:
        msg_text = "Yᴏᴜ ᴅᴏɴᴛ ʜᴀᴠᴇ ᴘᴇʀᴍɪssɪᴏɴ ᴛᴏ ᴜɴᴘɪɴ sᴏᴍᴇᴛʜɪɴɢ"
        return await message.reply_text(msg_text)
    
    await message.reply_text(
        "**Aʀᴇ ʏᴏᴜ sᴜʀᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜɴᴘɪɴ ᴀʟʟ ᴛʜᴇ ᴘɪɴɴᴇᴅ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ᴄʜᴀᴛ??**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [
                    InlineKeyboardButton(text="𝗬𝗘𝗦", callback_data="unpinall=yes"),
                    InlineKeyboardButton(text="𝗡𝗢", callback_data="unpinall=no")
                ]
            ]
        )
    )
"""
