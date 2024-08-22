import time
import os
from os import getenv
from dotenv import load_dotenv
from os import environ
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
#RSS_DELAY = int(os.environ.get("RSS_DELAY", 200))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "784589736").split()))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001784386455"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "784589736").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
GEMINI_API = os.getenv('GEMINI_API')
HEROKU_API_KEY = environ.get("HEROKU_API_KEY", "")
BT_STRT_TM = time.time()

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID", None)
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET", None)

PICS = (environ.get('PICS', 'https://telegra.ph/file/62869e1fa3feb3b54f812.jpg https://telegra.ph/file/5f3f5483889f57ef2840e.jpg https://telegra.ph/file/0e4cd3eb2d126f6a68624.jpg https://telegra.ph/file/a9519219dde18cc54c38b.jpg https://telegra.ph/file/81b06b91f1870ad1a98fd.jpg https://telegra.ph/file/07f5934b77bdcc0b748a6.jpg https://telegra.ph/file/8e27b92e1de9c10372001.jpg https://telegra.ph/file/cbf351a2a19772fe5892b.jpg https://telegra.ph/file/a4710618c55c4f463ad61.jpg https://telegra.ph/file/faf939bf4ee5b9637eeb9.jpg https://telegra.ph/file/9b2240cb38a65b707acaa.jpg https://telegra.ph/file/a3a5684a16d3a5625f8a7.jpg https://telegra.ph/file/d7625281c500dd76dc50d.jpg https://telegra.ph/file/db3354563ad6da1cec5bc.jpg https://telegra.ph/file/ad31737667d51017deb10.jpg https://telegra.ph/file/26c872eb992b520f6a871.jpg https://telegra.ph/file/d1e3cb8629f9eba0bd954.jpg https://telegra.ph/file/34e04eb2cc2a2ff671e73.jpg https://telegra.ph/file/91e00af3b4d207c16ad2a.jpg')).split()


"""
PICS = (environ.get('PICS', 'https://telegra.ph/file/6162054de1389ff916214.jpg https://telegra.ph/file/9c5f49cb0dc2a31536324.jpg https://telegra.ph/file/44446e87c1decfab6c1d7.jpg https://telegra.ph/file/bf5c473e5f9cabbc2ca78.jpg https://telegra.ph/file/8cf913d3170b06c54216f.jpg https://telegra.ph/file/10fb9ab27f4de046e65dd.jpg https://telegra.ph/file/d7806f320f4f9faf75114.jpg https://telegra.ph/file/d831af921160f348605b6.jpg https://telegra.ph/file/f7f27406bb6032ff90280.jpg https://telegra.ph/file/127e52c2a7eb0e79ab69a.jpg https://telegra.ph/file/58947490225b940367968.jpg https://telegra.ph/file/6dccb74c6206358b65e4c.jpg')).split()
"""

RECRU = int(os.environ.get("RECRU", "-1001954979279"))


class Telegram:
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "🤩", "👌",
        "😍", "🐳", "❤‍🔥", "💯",
        "💔", "🍓", "👀", "😇",
        "🤗", "🤪", "🗿", "🆒",
        "💘", "😘", "😁", "🎉",
        "🙏", "❤️‍🔥", "🕊️", "⚡",
        "🙈", "😇", "🤪", "💘"
    ]
    EMOJIS_2 = [
        "❤‍🔥"
    ]
