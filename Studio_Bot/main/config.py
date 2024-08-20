import pytz
from environs import Env

env = Env()
env.read_env()

tashkent_tz = pytz.timezone("Asia/Tashkent")

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

CHANNELS = [
    ("https://t.me/studio_pubgm", -1002229745608, "Studio Chat")
]

CHANNEL_ID = int(-1002162896780)

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_NAME = env.str("DB_NAME")

SHARE_LINK = env.str("SHARE_LINK")
