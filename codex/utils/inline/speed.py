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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle


def speed_markup(_, chat_id):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="🕒 0.5x",
                    callback_data=f"SpeedUP {chat_id}|0.5",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
                InlineKeyboardButton(
                    text="🕓 0.75x",
                    callback_data=f"SpeedUP {chat_id}|0.75",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
            ],
            [
                InlineKeyboardButton(
                    text=_["P_B_4"],
                    callback_data=f"SpeedUP {chat_id}|1.0",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
            ],
            [
                InlineKeyboardButton(
                    text="🕤 1.5x",
                    callback_data=f"SpeedUP {chat_id}|1.5",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
                InlineKeyboardButton(
                    text="🕛 2.0x",
                    callback_data=f"SpeedUP {chat_id}|2.0",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
            ],
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.PRIMARY, icon_custom_emoji_id="5397733426654626788"),
            ],
        ]
    )
    return upl
