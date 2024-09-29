from pyrogram import Client, filters
from pyrogram.types import Message

from tgbot.utils.helper.pricehistory import get_price_history_text


@Client.on_message(filters.command("price"))
async def price(_, message: Message):
    """ Price History"""
    priceHistory_usage = f"**Usage:** price history. Reply to text message or just type the text after command. \n\n**Price History.** \n\n**Example:** /price link"
    prehistory_reply = await message.reply_text("...", quote=True)
    replied_message = message.reply_to_message
    try:
        if len(message.command) > 1:
            content = message.text.split(None, 1)[1]

        elif len(message.command) < 2:
            return await prehistory_reply.edit(priceHistory_usage)

        output = await get_price_history_text(content)
        return await prehistory_reply.edit(output) and await prehistory_reply.delete()
    except Exception as e:
        return await prehistory_reply.edit(f"**Error:** {e}")
