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

from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
import logging
from codex import app

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🎥 Video chat has started in {chat.title}!\n\nJoin us now for a fun time together! 😄"
    )

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message: Message):
    chat = message.chat
    await message.reply(
        f"🚫 Video chat has ended in {chat.title}.\n\nThank you for joining! See you next time! 👋"
    )
