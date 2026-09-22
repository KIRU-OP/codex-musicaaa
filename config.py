# Copyright (c) 2025 @SUDEEPBOTS <HellfireDevs>
# Location: delhi,noida
#
# All rights reserved.
#
# This code is the intellectual SUDEEPBOTS.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: sudeepgithub@gmail.com

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "16457832"))

API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")

BOT_TOKEN = getenv("BOT_TOKEN", "7000859933:AAEnaU9196qHT0bSyaoqROwmc_XCImYhP4E")#

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://codexNew:Mongo@cluster0.zllsvlo.mongodb.net/?appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1002022622141"))

OWNER_ID = int(getenv("OWNER_ID", "6625936112"))

BOT_USERNAME = getenv("BOT_USERNAME" , "@Syn_Ixbot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split() + [""]

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

RENDER = getenv("RENDER", "False").lower() == "true"

PING_URL = getenv("PING_URL", "")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TrickBySaqib/codexMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", ""
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Zcziiyy")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DEVTAL")


AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))

BASE_URL = getenv("BASE_URL", "https://babyapi.pro")
API_KEY = getenv("API_KEY", None)
# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "BQD7IGgARZlAB1lCIrHI1TFZlaT1oQafB_ADnYhMLFcT3N5-utYkkPHx8BZHxege07D0DRHke2f-0PDPlKWeV6Us4AIi7hF2rtuU7yiEC_I5sHdqeN958ug4XF_9pHCwUqmke12c5csZa6MCIJ8ooGCg8Ndo5ABvtvxDAOVMyFOayk47iaJoYzBN5JQpmozzd_euToUIuWzpTmt7pjJ-6XB04u4RTE_MY6Ox3ey9jqwUKwRIJAdgb_4QRXWDyqYOSGjrWr1putbJC4yVx99En0EUcesfHmMzo-wFWg9oqhU382AqmDbBIPxpl2KbWsbiTqIWLiGhKgFu0_Xi59nb-7N3Ij_qowAAAAHFA_aoAA")
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
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/kzcoir.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/8b3614b932b12996c6378-5fff06ef0dee7a3106.jpg"
STATS_IMG_URL = "https://graph.org/file/8b3614b932b12996c6378-5fff06ef0dee7a3106.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/8b3614b932b12996c6378-5fff06ef0dee7a3106.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/8b3614b932b12996c6378-5fff06ef0dee7a3106.jpg"
STREAM_IMG_URL = "https://graph.org/file/8b3614b932b12996c6378-5fff06ef0dee7a3106.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )

VALID_EMOJII = ["🔥", "💋", "🥺", "😒", "💖",
                "💘", "💕", "✨", "🥰", "🍌", "💔",
                "😓", "🫧"]

EFFECT_IDS = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]
