"""
Music Player, Telegram Voice Chat Bot
Copyright (c) 2021-present Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self) -> None:
        self.API_ID: str = os.environ.get("API_ID", "10137497")
        self.API_HASH: str = os.environ.get("API_HASH", "0184e156c25b7b00e63c648ea4283cf0")
        self.SESSION: str = os.environ.get("SESSION", "BQCRWxcsHkBDLoeU5_X4Y_2JtSguhGMD8pQslteSaBovZe-c3W7wwpRWBgSPb0J8Hr6CLGoTlipZGJskE5A7p1hPQXL3xOK7lusP0Lw-LDjdc9f0Ay4ZYLXVBLjjRxryZsCp2TEX1N3jvfbgEj_zi9ERkGQ697WtaFQrrLmH9FLswsfXx7PbfoyZgvDs0O4ikFxhyenQnZ75CCNTF_pvL2h_ILmbap0xKNuRqwdwmsYJEUjm2WObJcfGTMlGQvDvnxtPuWJ1ZKKfd7xsBadFFabeUrPtuRLz3QcgzbgZxyGS68uUgZtKyEWk6ObXYmvBwVWj7n5Ox6EP89qC8T4Ogzzfa5KmjwA")
        self.BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "5298712919:AAFYv7SF4wF1hcRctU-Ac-YgIZX_3-t3xFE")
        self.SUDOERS: list = [
            int(id) for id in os.environ.get("SUDOERS", " ").split() if id.isnumeric("908731482")
        ]
        if not self.SESSION or not self.API_ID or not self.API_HASH:
            print("ERROR: SESSION, API_ID and API_HASH is required!")
            quit(0)
        self.SPOTIFY: bool = False
        self.QUALITY: str = os.environ.get("QUALITY", "high").lower()
        self.PREFIXES: list = os.environ.get("PREFIX", "!").split()
        self.LANGUAGE: str = os.environ.get("LANGUAGE", "en").lower()
        self.STREAM_MODE: str = (
            "audio"
            if (os.environ.get("STREAM_MODE", "audio").lower() == "audio")
            else "video"
        )
        self.ADMINS_ONLY: bool = os.environ.get("ADMINS_ONLY", False)
        self.SPOTIFY_CLIENT_ID: str = os.environ.get("SPOTIFY_CLIENT_ID", "5fac2f6a995b434999ee00f39027260f")
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get("SPOTIFY_CLIENT_SECRET", "9b28585f29a44c049ec50ff6e3df3877")


config = Config()
