import math

from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
from codex.utils.formatters import time_to_seconds


def seconds_to_time(seconds):
    """
    Seconds ko wapas "MM:SS" (ya lambi duration ke liye "HH:MM:SS")
    format mein convert karta hai. Real/ulta (remaining) timer
    dikhane ke kaam aata hai.
    """
    seconds = max(0, int(seconds))
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours:02}:{minutes:02}:{secs:02}"
    return f"{minutes:02}:{secs:02}"


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    # Remaining (ulta/countdown) time — total duration me se
    # ab tak play hua time ghata kar nikala jaata hai
    remaining_sec = duration_sec - played_sec
    remaining_time = seconds_to_time(remaining_sec)

    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 12:
        bar = "▰▱▱▱▱▱▱▱"
    elif 12 < umm < 25:
        bar = "▰▰▱▱▱▱▱▱"
    elif 25 <= umm < 37:
        bar = "▰▰▰▱▱▱▱▱"
    elif 37 <= umm < 50:
        bar = "▰▰▰▰▱▱▱▱"
    elif 50 <= umm < 62:
        bar = "▰▰▰▰▰▱▱▱"
    elif 62 <= umm < 75:
        bar = "▰▰▰▰▰▰▱▱"
    elif 75 <= umm < 87:
        bar = "▰▰▰▰▰▰▰▱"
    else:
        bar = "▰▰▰▰▰▰▰▰"

    buttons = [
        # Row 1: Progress bar with timing
        [
            InlineKeyboardButton(
                text=f"{played.lower()} {bar} -{remaining_time}",
                callback_data="GetTimer"
            )
        ],
        # Row 2: Main control buttons
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
        ],
        # Row 3: Seek backward / Download / Seek forward
        [
            InlineKeyboardButton(text="⪻  -30s", callback_data=f"SEEKBACKWARD|{chat_id}|30", style=ButtonStyle.DEFAULT),
            InlineKeyboardButton(text="📥", callback_data=f"DOWNLOAD|{chat_id}", style=ButtonStyle.DEFAULT),
            InlineKeyboardButton(text="+30s  ⪼", callback_data=f"SEEKFORWARD|{chat_id}|30", style=ButtonStyle.DEFAULT),
        ],
        # Row 4: Close button
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"].lower(), callback_data="close", style=ButtonStyle.DANGER)
        ]
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        # Row 1: Controls
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
        ],
        # Row 2: Seek backward / Download / Seek forward
        [
            InlineKeyboardButton(text="⪻  -30s", callback_data=f"SEEKBACKWARD|{chat_id}|30", style=ButtonStyle.DEFAULT),
            InlineKeyboardButton(text="📥", callback_data=f"DOWNLOAD|{chat_id}", style=ButtonStyle.DEFAULT),
            InlineKeyboardButton(text="+30s  ⪼", callback_data=f"SEEKFORWARD|{chat_id}|30", style=ButtonStyle.DEFAULT),
        ],
        # Row 3: Close
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"].lower(), callback_data="close", style=ButtonStyle.DANGER)
        ]
    ]
    return buttons


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons
def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"EraPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"EraPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
