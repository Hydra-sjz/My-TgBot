from pyrogram import Client, filters
from tgbot import tgbot as app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message 

BUTTONS = [
    [
        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/TanuM"),
    ],
]

def hex_to_text(hex_string):
    try:
        text = bytes.fromhex(hex_string).decode('utf-8')
        return text
    except Exception as e:
        return f"Error decoding hex: {str(e)}"


def text_to_hex(text):
    hex_representation = ' '.join(format(ord(char), 'x') for char in text)
    return hex_representation


# IAM_DAXX ...........................

@app.on_message(filters.command("code"))
def convert_text(_, message):
    if len(message.command) > 1:
        input_text = " ".join(message.command[1:])

        hex_representation = text_to_hex(input_text)
        decoded_text = hex_to_text(input_text)

        response_text = f"๏ ɪɴᴘᴜᴛ ᴛᴇxᴛ ➠\n {input_text}\n\n๏ ʜᴇx ʀᴇᴘʀᴇsᴇɴᴛᴀᴛɪᴏɴ ➠\n {hex_representation}\n\n๏ ᴅᴇᴄᴏᴅᴇᴅ ᴛᴇxᴛ ➠\n {decoded_text}\n\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠  ˹ ᴛᴀɴᴜ ꭙ ᴍᴜsɪᴄ™ ♡゙"

        message.reply_text((response_text),reply_markup=InlineKeyboardMarkup(BUTTONS),)
    else:
        message.reply_text("✦ Please provide text after the /code command.")
      