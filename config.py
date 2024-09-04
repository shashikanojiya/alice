import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27178940
API_HASH = "a9813a90bff1094a43f57856d2e3cb7e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7471888709:AAGIYs-3CsljQ-WXLxewHN2keCSrTykfV-8"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://shashikanojiya115:shashikanojiya115@cluster0.ptjyx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1001903333368

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7367828933

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/XTM_WORLD"
SUPPORT_GROUP = "https://t.me/XTM_WORLD"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGet7wAYmO-pZ-43w2eg5BtWRWRFqECrenUEGfC8e_DjKGOsBioJWHJEWCL_qQz0nVuWTHUFbfr9g5GgxHHupJLN4SHtOT-5pc2aWlSQLasTf-k7s9TxPS7EUwc0R-wEzPvNa27q3R7m3iS04_BDO6m9WMbor552bH_B5gsoIK1FvVXVkhXQNpLYnwdOXYXbcq48kx5Fx_AGTa7jC4gjELCCt8TCBeMARUr4bojIcjRGH7EgLrWY_oSMQw3JqRpAqAAD8GERBmglmclL3vCBF2tKDLdwvzHLFJra9FZIBNE0tlQ-5trESSqSN6UzjEliI-XXLMVMkxDttSkBu0e2uO916mncQAAAAG3KCXFAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"

PING_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
STATS_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
STREAM_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/b7561344761beb7356a40.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
