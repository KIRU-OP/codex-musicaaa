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

import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from codex import LOGGER, app, userbot
from codex.core.call import Sagar
from codex.misc import sudo
from codex.plugins import ALL_MODULES
from codex.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    if config.RENDER:
        try:
            import server
            server.keep_alive_ping()
            LOGGER(__name__).info("Web server started for Render keep-alive.")
        except Exception as e:
            LOGGER(__name__).error(f"Failed to start web server: {e}")

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("codex.plugins" + all_module)
    LOGGER("codex.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴀʟʟ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Sagar.start()
    try:
        await Sagar.stream_call("https://te.legra.ph/file/39b302c93da5c457a87e3.mp4")
    except NoActiveGroupCall:
        LOGGER("codex").error(
            "Please turn on the Voice Chat in your Logger Group/Channel.\n\nBot is shutting down..."
        )
        exit()
    except:
        pass
    await Sagar.decorators()
    LOGGER("codex").info(
        "codex Music Bot Started Successfully!"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("codex").info("Stopping codex Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
