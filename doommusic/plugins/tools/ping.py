# -----------------------------------------------
# 🔸 Doom Music Project
# 🔹 Developed & Maintained by: Yash (https://github.com/yashcodex121)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by Yash
# -----------------------------------------------
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from doommusic import app
from doommusic.core.call import YASH
from doommusic.utils import bot_sys_stats
from doommusic.utils.decorators.language import language
from doommusic.utils.inline import supp_markup
from config import BANNED_USERS, SHASHANK_IMG
import random


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        random.choice(SHASHANK_IMG),
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await YASH.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )
