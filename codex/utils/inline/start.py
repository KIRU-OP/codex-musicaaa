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
        [
            InlineKeyboardButton(
                text="𝐒ᴜᴘᴘᴏʀᴛ",
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.SUCCESS
            ),
            InlineKeyboardButton(
                text="𝐔ᴘᴅᴀᴛᴇs",
                url=config.UPDATE_CHANNEL,
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id="5343597635926245720"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐂ʜᴀɴɴᴇʟ",
                url=config.UPDATE_CHANNEL,
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text="𝐁ᴏᴛ ɪɴғᴏ",
                callback_data="bot_info_data",
                style=ButtonStyle.SUCCESS,
                icon_custom_emoji_id="5235682785863153026"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=ButtonStyle.DANGER,
                icon_custom_emoji_id="6152069270269334526"
            )
        ],
    ]
    return buttons
