from pyrogram import Client, filters
from pyrogram.types import Message, ChatMember
import logging
from codex import app

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.video_chat_started)
async def video_chat_started(client, message: Message):
    chat = message.chat
    try:
        await message.reply(
            f"🎥 Video chat has started in {chat.title}!\n\nJoin us now for a fun time together! 😄"
        )
    except Exception as e:
        logging.warning(f"Could not send video_chat_started message in {chat.id}: {e}")

@app.on_message(filters.video_chat_ended)
async def video_chat_ended(client, message: Message):
    chat = message.chat
    try:
        await message.reply(
            f"🚫 Video chat has ended in {chat.title}.\n\nThank you for joining! See you next time! 👋"
        )
    except Exception as e:
        logging.warning(f"Could not send video_chat_ended message in {chat.id}: {e}")
