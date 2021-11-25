import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "LOVELY MUSIC")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Tushar204")
ALIVE_NAME = getenv("ALIVE_NAME", "Lovely")
BOT_USERNAME = getenv("BOT_USERNAME", "LOVELYR_OBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LOVELY2VC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LOVELYAPPEAL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LOVELY_ROBOTS")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/7a19c8ec4209ca0a12126.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/attitudeking1/Lovely-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/7a19c8ec4209ca0a12126.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/7a19c8ec4209ca0a12126.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/7a19c8ec4209ca0a12126.jpg")
