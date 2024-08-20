from environs import Env
import pytz

tashkent_tz = pytz.timezone("Asia/Tashkent")

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

CHANNELS = [
    ("https://t.me/studio_pubgm", -1002229745608, "Studio Chat"),
]

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
DB_NAME = env.str("DB_NAME")


