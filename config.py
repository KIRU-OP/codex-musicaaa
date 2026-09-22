# ============================================================
#                     CONFIG.PY — SAMJHANE WALI FILE
# ============================================================
# Yeh file bot ki "settings/configuration" file hai.
# Isme saare secret keys, IDs, links, aur limits set hoti hain.
# Bot chalte waqt yeh values .env file (agar hai) se uthata hai,
# aur agar .env mein value nahi mili, toh yahan diya hua
# "default value" use hota hai (getenv ka doosra argument).
#
# Example: getenv("API_ID", "16457832")
#          -> Pehle .env mein "API_ID" dhundega
#          -> Agar nahi mila, toh "16457832" use karega
# ============================================================

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

# .env file ko load karta hai taaki uske andar likhi variables
# python ke environment mein aa jaayein (getenv se access karne layak)
load_dotenv()


# ------------------------------------------------------------
# TELEGRAM API CREDENTIALS (my.telegram.org se milte hain)
# ------------------------------------------------------------

# API_ID - Telegram ka unique app identifier number
API_ID = int(getenv("API_ID", "16457832"))

# API_HASH - API_ID ke saath paired secret hash
API_HASH = getenv("API_HASH", "3030874d0befdb5d05597deacc3e83ab")

# BOT_TOKEN - @BotFather se milta hai, bot ko control karne ke liye
BOT_TOKEN = getenv("BOT_TOKEN", "")  # empty rakha hai, .env mein daalna zaruri


# ------------------------------------------------------------
# DATABASE
# ------------------------------------------------------------

# MONGO_DB_URI - MongoDB database ka connection link
# (bot ka data - jaise settings, chats, users - yahan store hota hai)
MONGO_DB_URI = getenv("MONGO_DB_URI", "")


# ------------------------------------------------------------
# DURATION / TIME LIMITS
# ------------------------------------------------------------

# DURATION_LIMIT_MIN - kitne minute tak ki video/audio play ho sakti hai
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

# SONG_DOWNLOAD_DURATION - kitne second tak ka gaana download ho sakta hai
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)


# ------------------------------------------------------------
# LOGGER & OWNER
# ------------------------------------------------------------

# LOGGER_ID - jis channel/group mein bot apne logs (activity) bhejta hai
LOGGER_ID = int(getenv("LOGGER_ID", "-1002022622141"))

# OWNER_ID - bot ke owner (malik) ki Telegram user ID
# (isko full/special access milta hai)
OWNER_ID = int(getenv("OWNER_ID", "6625936112"))

# BOT_USERNAME - bot ka Telegram username (bina @ ke)
BOT_USERNAME = getenv("BOT_USERNAME", "")

# COMMAND_HANDLER - kaunse symbols se command start ho sakti hai
# jaise "!play", "/play", ".play" — sab chalenge
COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split() + [""]


# ------------------------------------------------------------
# HEROKU / RENDER HOSTING SETTINGS
# ------------------------------------------------------------

# HEROKU_APP_NAME - agar bot Heroku pe hosted hai, uska app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# HEROKU_API_KEY - Heroku account ki API key (auto-restart jaise features ke liye)
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# RENDER - agar bot Render.com pe hosted hai toh True set karo
RENDER = getenv("RENDER", "False").lower() == "true"

# PING_URL - bot ko "alive" rakhne ke liye jis URL ko ping kiya jaata hai
PING_URL = getenv("PING_URL", "")


# ------------------------------------------------------------
# GITHUB UPDATE SETTINGS (bot ko auto-update karne ke liye)
# ------------------------------------------------------------

# UPSTREAM_REPO - jis GitHub repo se bot updates leta hai
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/KIRU-OP/codex-music",
)

# UPSTREAM_BRANCH - us repo ki kaunsi branch use karni hai
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT_TOKEN - agar upstream repo PRIVATE hai, tabhi yeh bharna zaruri hai
GIT_TOKEN = getenv("GIT_TOKEN", "")


# ------------------------------------------------------------
# SUPPORT LINKS (buttons mein use hote hain)
# ------------------------------------------------------------

# SUPPORT_CHANNEL - bot ka official update/announcement channel link
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_deadly_venom")

# SUPPORT_CHAT - bot ka official support group/chat link
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+Dv-MzFXDPCdkNWU1")

# UPDATE_CHANNEL - bot ke updates/announcements wala channel link
# (Updates button isi link ko use karega)
UPDATE_CHANNEL = getenv("UPDATE_CHANNEL", "https://t.me/kiru_bots")

# ------------------------------------------------------------
# ASSISTANT & SUGGESTION SETTINGS
# ------------------------------------------------------------

# AUTO_LEAVING_ASSISTANT - True hone par assistant khud group chhod dega
# (jaise agar kaafi der se koi use nahi kar raha)
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# AUTO_SUGGESTION_MODE - jab koi song na mile, similar suggestion dikhana ya nahi
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")

# AUTO_SUGGESTION_TIME - suggestion dikhane se pehle kitna wait karna hai (ms/seconds)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))


# ------------------------------------------------------------
# SPOTIFY API CREDENTIALS
# ------------------------------------------------------------

# SPOTIFY_CLIENT_ID - Spotify Developer Dashboard se milta hai
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

# SPOTIFY_CLIENT_SECRET - Spotify ka secret key
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# ------------------------------------------------------------
# PLAYLIST & CLEANUP SETTINGS
# ------------------------------------------------------------

# PLAYLIST_FETCH_LIMIT - ek baar mein kitne songs fetch honge playlist se
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

# CLEANMODE_DELETE_MINS - purani messages/queue kitne minute baad clean hongi
CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))


# ------------------------------------------------------------
# FILE SIZE LIMITS (bytes mein)
# ------------------------------------------------------------

# TG_AUDIO_FILESIZE_LIMIT - audio file ka maximum size jo bhej sakte hain
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 21474836480))

# TG_VIDEO_FILESIZE_LIMIT - video file ka maximum size jo bhej sakte hain
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 21474836480))


# ------------------------------------------------------------
# API / BASE URL
# ------------------------------------------------------------

# BASE_URL - external API service ka base address
BASE_URL = getenv("BASE_URL", "https://babyapi.pro")

# API_KEY - us external API ki access key
API_KEY = getenv("API_KEY", None)


# ------------------------------------------------------------
# PYROGRAM STRING SESSIONS (Assistant accounts ke liye)
# ------------------------------------------------------------
# Yeh sessions "assistant" account ko login karne ke liye hote hain
# (jo voice chat mein aake gaana bajata hai).
# Inhe @Shsusu_bot se generate kiya jaata hai.
# Zyada se zyada 5 alag-alag assistant accounts support karta hai.

STRING1 = getenv("STRING_SESSION", "BQD7IGgARZlAB1lCIrHI1TFZlaT1oQafB_ADnYhMLFcT3N5-utYkkPHx8BZHxege07D0DRHke2f-0PDPlKWeV6Us4AIi7hF2rtuU7yiEC_I5sHdqeN958ug4XF_9pHCwUqmke12c5csZa6MCIJ8ooGCg8Ndo5ABvtvxDAOVMyFOayk47iaJoYzBN5JQpmozzd_euToUIuWzpTmt7pjJ-6XB04u4RTE_MY6Ox3ey9jqwUKwRIJAdgb_4QRXWDyqYOSGjrWr1putbJC4yVx99En0EUcesfHmMzo-wFWg9oqhU382AqmDbBIPxpl2KbWsbiTqIWLiGhKgFu0_Xi59nb-7N3Ij_qowAAAAHFA_aoAA")  # 1st assistant session
STRING2 = getenv("STRING_SESSION2", None)  # 2nd assistant session (optional)
STRING3 = getenv("STRING_SESSION3", None)  # 3rd assistant session (optional)
STRING4 = getenv("STRING_SESSION4", None)  # 4th assistant session (optional)
STRING5 = getenv("STRING_SESSION5", None)  # 5th assistant session (optional)


# ------------------------------------------------------------
# RUNTIME DATA STORAGE (in-memory dictionaries/lists)
# ------------------------------------------------------------
# Yeh saare khaali dictionaries/lists hain jo bot chalte waqt
# temporary data store karne ke kaam aate hain (RAM mein, restart
# hone par khaali ho jaate hain — database nahi hai).

BANNED_USERS = filters.user()   # banned users ka filter
adminlist = {}                  # har chat ke admins ki list
lyrical = {}                    # lyrics feature ka temporary data
votemode = {}                   # skip-vote mode ka data
autoclean = []                  # auto-clean hone waale chats ki list
confirmer = {}                  # confirmation-wait state
chatstats = {}                  # chat-wise statistics
userstats = {}                  # user-wise statistics
clean = {}                      # cleanup related data

autoclean = []  # (note: yeh line upar wali autoclean = [] ko overwrite kar rahi hai)


# ------------------------------------------------------------
# IMAGE URLS (bot ke different messages mein use hone waali images)
# ------------------------------------------------------------

# START_IMG_URL - /start command pe dikhne waali image
START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/kzcoir.jpg"
)

# PING_IMG_URL - /ping command pe dikhne waali image
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/ac589b90138d32ef749e3-7182273a0f23f0c76e.jpg"
)

# Baaki saari images alag-alag features/platforms ke liye hain
# (playlist, stats, telegram audio/video, soundcloud, youtube, spotify)
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


# ------------------------------------------------------------
# HELPER FUNCTION
# ------------------------------------------------------------

def time_to_seconds(time):
    """
    Yeh function "HH:MM:SS" jaisi time-string ko total seconds mein convert karta hai.
    Example: "1:30:00" -> 5400 seconds
    """
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


# DURATION_LIMIT_MIN aur SONG_DOWNLOAD_DURATION (jo minute mein the)
# ko upar wale function se seconds mein convert kar rahe hain
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))


# ------------------------------------------------------------
# VALIDATION CHECKS (galat link daalne par bot start hi nahi hoga)
# ------------------------------------------------------------

# Check karta hai ki SUPPORT_CHANNEL link "http://" ya "https://" se start ho raha hai ya nahi
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

# Check karta hai ki SUPPORT_CHAT link bhi sahi format mein hai ya nahi
if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )


# ------------------------------------------------------------
# EMOJI & EFFECTS (fun/reaction features ke liye)
# ------------------------------------------------------------

# VALID_EMOJII - in emojis ko bot kisi feature (jaise random reaction) mein use kar sakta hai
VALID_EMOJII = ["🔥", "💋", "🥺", "😒", "💖",
                "💘", "💕", "✨", "🥰", "🍌", "💔",
                "😓", "🫧"]

# EFFECT_IDS - Telegram ke special message-effects (premium animations) ki IDs
EFFECT_IDS = [
    5046509860389126442,
    5107584321108051014,
    5104841245755180586,
    5159385139981059251,
]
