# SumikoMusic - Telegram MusicBot Project
# Copyright (C) 2021 @iisgaurav

# This file is a part of < https://github.com/iisgaurav/SumikoMusic/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/iisgaurav/SumikoMusic/blob/main/LICENSE/>.


from pyrogram import Client
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from SumikoMusic.helpers.decorators import authorized_users_only
from SumikoMusic.helpers.decorators import errors
from SumikoMusic.services.callsmusic import client as USER
from SumikoMusic.config import SUDO_USERS
from SumikoMusic.config import ASSISTANT_USERNAME

@Client.on_message(filters.command(["userbotjoin"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>First add me as a admin in your group</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "SumikoMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Assistant already in your chat</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n User {user.first_name} couldn't join your group due to heavy join requests for Assistant! Make sure user is not banned in group."
            "\n\nOr manually add {ASSISTANT_USERNAME} in your Group</b>",
        )
        return
    await message.reply_text(
        "<b>Assistant joined your Group</b>",
    )


@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group!"
            "\n\nmanually kick from your Group</b>",
        )
        return
    
@Client.on_message(filters.command(["userbotleaveall"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")
    

