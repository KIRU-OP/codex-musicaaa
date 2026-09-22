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

from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

import config
from codex import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id="6255793039705377676"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id="5397733426654626788"
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id="6255793039705377676"
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper", style=ButtonStyle.DANGER, icon_custom_emoji_id="6152069270269334526")],
        [
            InlineKeyboardButton(text="🎧", url="https://t.me/Zcziiyy", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton(text="🫦", url="https://t.me/Zcziiyy", style=ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("𝐔ᴘᴅᴀᴛᴇs 📢", url="https://t.me/Zcziiyy", style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5343597635926245720")            
        ],
        [
            InlineKeyboardButton("• ʙᴏᴛ ɪɴғᴏ •", callback_data="bot_info_data", style=ButtonStyle.SUCCESS, icon_custom_emoji_id="5235682785863153026"),
        ],
    ]
    return buttons
