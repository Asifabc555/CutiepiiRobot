import json
import os


def get_user_list(config, key):
    with open("{}/Cutiepii_Robot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "14980683"
    API_HASH = "5bc2e9cd58092119e741c1f2b545c1bf"
    APP_ID = "14980683"  # 2nd API_ID
    APP_HASH = "5bc2e9cd58092119e741c1f2b545c1bf"  # 2ns API_HASH
    ARQ_API_KEY = "UMPYGF-MVNLVW-RTNXKA-FJWOUH-ARQ"
    BOT_ID = "5724176249"
    TOKEN = "5724176249:AAEUx_8vGdfmXdZKhxOvDKLXK4Ws37DE4nk"
    OWNER_ID = "5667156680"
    OPENWEATHERMAP_ID = "ca1f9caacbb92187db96c0bf5686017b"
    OWNER_USERNAME = "HSSLevii"
    BOT_USERNAME = "Riass_Gremory_Bot"
    SUPPORT_CHAT = "WoFBotsSupport"
    UPDATES_CHANNEL = "WoFBotsSupport"
    SUPPORT_CHANNEL = "WoFBotsSupport"
    JOIN_LOGGER = "-1001745301697"
    EVENT_LOGS = "-1001793111970"
    ERROR_LOGS = "-1001754970449"

    SQLALCHEMY_DATABASE_URI = "postgres://repmvdyk:EJu4_GvXFdR-pz0UigysTMiYWM0aGtMX@heffalump.db.elephantsql.com/repmvdyk"
    DB_URL = ""
    MONGO_DB_URL = "mongodb+srv://ath:atharva@cluster0.osln3an.mongodb.net/?retryWrites=true&w=majority"  # needed for any database modules
    MONGO_URL = ""
    DB_URL2 = ""  # YOUR MONGO_DB_URI
    ARQ_API_URL = "https://arq.hamker.in"
    BOT_API_URL = "https://api.telegram.org/bot"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""
    SPAMWATCH_SUPPORT_CHAT = "@WoFBotsSupport"

    REDIS_URL = ""

    DRAGONS = get_user_list("elevated_users.json", "sudos")
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    REQUESTER = get_user_list("elevated_users.json", "whitelists")
    DEMONS = get_user_list("elevated_users.json", "supports")
    INSPECTOR = get_user_list("elevated_users.json", "sudos")
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = "https://t.me/HSSLevii"
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
    AI_API_KEY = "p1r3mTfeLP9-NkFGA1EVkPKgVyj9v0LvWIkx4v8SPT34hNjAum3q3ASM78HtnfoK"
    BL_CHATS = []
    SPAMMERS = None
    SPAMWATCH_API = "QsrtejDpiLrvimOWSQeq6hpLNyMI_RIA_TfKExdSnBKE20I2gIXeDxBxYC76kLE6"
    ALLOW_CHATS = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    REM_BG_API_KEY = "PxCe5v4ZX3RmoQnPdDzf2TTz"
    LASTFM_API_KEY = "FMLODA"
    CF_API_KEY = "KISS"
    BL_CHATS = []
    MONGO_PORT = "27017"
    MONGO_DB = "Cutiepii_Robot"
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
