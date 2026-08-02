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

from doommusic.core.bot import YASH
from doommusic.core.dir import dirr
from doommusic.core.git import git
from doommusic.core.userbot import Userbot
from doommusic.misc import heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = YASH()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "YashMusicBot"
