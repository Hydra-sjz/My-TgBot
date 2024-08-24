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

LOG_CHANNEL_ID = -1001954979279
GROUP_ID = -1001954979279
CHANNEL = -1001954979279
#OWNER_ID = 784589736
BOT_ID = 7057123792
DEVS = [784589736]

RECRU = int(os.environ.get("RECRU", "-1001954979279"))


#API_TOOLS
CURRENCY_API = environ.get("CURRENCY_API")
GPT_API = os.environ.get("GPT_API")
DAXX_API = os.environ.get("DAXX_API")
DEEP_API = os.environ.get("DEEP_API")
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY','')
GENIUS_API = os.getenv('GEMINI_API')
GEMINI_API = os.getenv('GEMINI_API')
FORCE_SUB   = environ.get("FORCE_SUB", "XBOTS_X") 




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
