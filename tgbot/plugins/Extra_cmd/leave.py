from pyrogram import filters
from tgbot import OWNER_ID, tgbot as app, CMD

#Leave Bot from Group!!!
@app.on_message(filters.command('leave', CMD) & filters.user(OWNER_ID))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('Give me a chat id')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
     
        k = await bot.send_message(
            chat_id=chat,
            text="Bye! \nMy Owner has told me to leave from group so,\nBye bye.",
        )
        await k.pin()
        await bot.leave_chat(chat)
        await message.reply(f"I am left the chat from: [`{chat}`]")
    except Exception as e:
        await message.reply(f"#Error {e}")
