# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = int(getenv("API_ID", "33237438"))
API_HASH = getenv("API_HASH", "0b8473654c274c76d5f0fd222d13716f")
BOT_TOKEN = getenv("BOT_TOKEN", "8251063395:AAFYpc46hoU5d17iFLokcCNcXq2PgBzrolk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8532832031").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://forwardbot:xvpaXVydJyuZyLh0@cluster0.k304gdc.mongodb.net/?")
LOG_GROUP = -1003222305505
CHANNEL_ID = -1003547819507
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "1000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "8000"))
WEBSITE_URL = getenv("WEBSITE_URL", "vplink.in")
AD_API = getenv("AD_API", "0b8473654c274c76d5f0fd222d13716f)
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
DEFAULT_SESSION = getenv("DEFAUL_SESSION", None)  # added old method of invite link joining
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
