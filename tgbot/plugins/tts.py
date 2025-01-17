from pyrogram import Client, filters
from gtts import gTTS
from tgbot import tgbot as app, CMD


@app.on_message(filters.command('tts', CMD))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('speech.mp3')
    client.send_audio(message.chat.id, 'speech.mp3')
