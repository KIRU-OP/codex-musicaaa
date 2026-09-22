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

from time import time
from functools import wraps
from pyrogram.types import Message

def rate_limit(wait_time):
    last_clicked_times = {}

    def decorator(func):
        @wraps(func)
        async def wrapper(client, message: Message, *args, **kwargs):
            user_id = message.from_user.id
            now = time()
            
            if user_id in last_clicked_times and (now - last_clicked_times[user_id] < wait_time):
                await message.edit(f"ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ {int(wait_time - (now - last_clicked_times[user_id]))} sᴇᴄᴏɴᴅs ʙᴇғᴏʀᴇ ᴄʟɪᴄᴋɪɴɢ ᴀɢᴀɪɴ.", show_alert=True)
                return
            
            last_clicked_times[user_id] = now
            return await func(client, message, *args, **kwargs)
        
        return wrapper
    return decorator
