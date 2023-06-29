"""
MIT License

Copyright (c) 2022 ABISHNOI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Abishnoi
#     MY ALL BOTS :- Abishnoi_bots
#     GITHUB :- KingAbishnoi ""

import json
import os


def get_user_list(config, key):
    with open("{}/Exon/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "10821359"
    API_HASH = "2b1b1a5e842bff25ad1baa12657b3894"
    APP_ID = "23377505"  # 2nd API_ID
    APP_HASH = "7fed25e2e1858a5f3add05e30393e7f3"  # 2ns API_HASH
    ARQ_API_KEY = "HDPBMZ-QXNRNN-QYGIVF-GMDXHT-ARQ"
    BOT_ID = "6178626262"
    TOKEN = "6178626262:AAGYaJJ0-9seijKX0wT54BW_PaiER82rpN0"
    OWNER_ID = "6257122478"
    OPENWEATHERMAP_ID = "22322"
    OWNER_USERNAME = "Fuckingenos"
    BOT_USERNAME = "Esdeath_probot"
    SUPPORT_CHAT = "Mega_Bots_Support"
    UPDATES_CHANNEL = "Mega_Bot_Updates"
    SUPPORT_CHANNEL = "TeamMegaz"
    JOIN_LOGGER = "-1001972656429"
    EVENT_LOGS = "-1001837797753"
    ERROR_LOGS = "-1001972656429"

    DB_URI = "postgres://xzuvghotkiomnu:e2263a2d1e5ef572304f570fd86a06513737e2a6f70f9acbbe185b380dbda12b@ec2-35-169-184-61.compute-1.amazonaws.com:5432/d10ivlrn2n4rss"
    DB_URL = "postgres://ctoixwyr:CThCpbMv1lkdUuN90qeGdZ4VxdjpgTty@snuffleupagus.db.elephantsql.com/ctoixwyr"
    MONGO_DB_URL = "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority"
    DB_URL2 = "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority"  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.in"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "TVsho8jatGQ6xyA61O~PNMBZaRB9NTNKyFMKwmWWDq8tU7mMF~MKydYWKQxCaW8M"
    SPAMWATCH_SUPPORT_CHAT = "@AbishnoiMF"

    REDIS_URL = "redis://Madharjoot:GuKhao123_@redis-12276.c275.us-east-1-4.ec2.cloud.redislabs.com:12276/Madharjoot"

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "whitelists")
    DEMONS = get_user_list("elevated_users.json", "supports")
    INSPECTOR = get_user_list("elevated_users.json", "sudos")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/Abishnoi1M"
    CERT_PATH = None
    STRICT_GBAN = "True"
    PORT = ""
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = 8
    BAN_STICKER = ""
    ALLOW_EXCL = True
    CASH_API_KEY = "VQ45LFKYPMJ2LKIU"
    TIME_API_KEY = "65G8ZKE6050P"
    WALL_API = "F-OFF"
    AI_API_KEY = "LOVEYOU"
    BL_CHATS = []
    SPAMMERS = None
    SPAMWATCH_API = ""
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "PxCe5v4ZX3RmoQnPdDzf2TTz"
    LASTFM_API_KEY = "FMLODA"
    CF_API_KEY = "KISS"
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "Levi"
    STRING_SESSION =""
    PHOTO = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    HELP_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    START_IMG = "https://telegra.ph/file/14d1f98500af1132e5460.jpg"
    TIME_API_KEY = "65G8ZKE6050P"
    INFOPIC = False
    GENIUS_API_TOKEN = "p1r3mTfeLP9-NkFGA1EVkPKgVyj9v0LvWIkx4v8SPT34hNjAum3q3ASM78HtnfoK"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
