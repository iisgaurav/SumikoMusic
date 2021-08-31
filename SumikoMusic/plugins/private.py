# SumikoMusic - Telegram MusicBot Project
# Copyright (C) 2021 @iisgaurav

# This file is a part of < https://github.com/iisgaurav/SumikoMusic/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/iisgaurav/SumikoMusic/blob/main/LICENSE/>.

from pyrogram import filters
from pyrogram.types import Message
from SumikoMusic.services.callsmusic import client as USER
from SumikoMusic.config import BOT_USERNAME


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pm(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        """Hi there, This is {BOT_USERNAME} assistant .
        
        ⚠️ Disclamer:   
           - Don't add this user to private groups.  
           - Don't Share private info here
           - Don't spam here""")
    return
