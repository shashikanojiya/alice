import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 27178940
API_HASH = "a9813a90bff1094a43f57856d2e3cb7e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7698875206:AAGbWELD3heR5o2v8ds_bODmYYOyq_Mx6Zc"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://Shashikanojiya11:wRyosAJEDeAMWftx@cluster0.alfq2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002396081980

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

SUPPORT_CHANNEL = "https://t.me/Death_cloub"
SUPPORT_GROUP = "https://t.me/Death_cloub"

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
STRING1 = "BQGet7wASREqLxhxE4WIry5jC6cCOw8PLlLU-5YNkqTLcEiOuvJLjgzV_YXwkoug_oLRl8zuW-daiqa1eeapLqkeSYoAE2JlnrxJIICyiLOlfLB2DFGYjqUNa7fcxa93U-l4-YxghVjBht65DQjQse5_cwMfRcjRVNF16hsNmxiRE2fq-jfz6pDbmkNxp2CBeMW7HIlZe1p-m0qxdFcQU4bymVQGTWI1BLpqxJBGhkz_G8BWOztQq1ZZ7jEXW-ax1QzWvINeFrpytXN8AuNduZyg8j2upq8rPapeYKV4VS0tdkbAtbSc0kU8wm2I9F2ZfIiZpqKGMKOO7oNRiFfQDCJzTXb0kQAAAAG3KCXFAA"
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


START_IMG_URL = "https://envs.sh/Z8A.jpg"

PING_IMG_URL = "https://envs.sh/Z8A.jpg"

PLAYLIST_IMG_URL = "https://envs.sh/Z8A.jpg"
STATS_IMG_URL = "https://envs.sh/Z8A.jpg"
TELEGRAM_AUDIO_URL = "https://envs.sh/Z8A.jpg"
TELEGRAM_VIDEO_URL = "https://envs.sh/Z8A.jpg"
STREAM_IMG_URL = "https://envs.sh/Z8A.jpg"
SOUNCLOUD_IMG_URL = "https://envs.sh/Z8A.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/Z8A.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://envs.sh/Z8A.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://envs.sh/Z8A.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://envs.sh/Z8A.jpg"


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
