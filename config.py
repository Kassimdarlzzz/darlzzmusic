# Powered by @HYPER_AD13 | @ShiningOff
# Dear Pero ppls Plish Don't remove this line from here🌚

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "18641113"))
API_HASH = getenv("API_HASH", "bc5fea81e7bf9f3c0784a0a7d35f9c71")
BOT_TOKEN = getenv("5712171328:AAEieYyTKBoxMkQsDnvCMV40c5aJHX5f7ig", None)
OWNER_USERNAME = getenv("kassimdarlzzz", "ShiningOff")
BOT_USERNAME = getenv("Shadowxmusic_bot")
SUPPORT_GROUP = getenv("vanakkamda_mapla", "SilentVerse")
BOT_NAME = getenv("BOT_NAME","shinchan x music🥀")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "360"))
SESSION_NAME = getenv("AQCRbpMZRCun02ZdJ6j8wQ4pkOMy8P5mBYxiJEavLlWjgDsQljShUh94PHzCMtNMk7WtfRmqq9UVee8p2c8TNOcYu3No4UAynYEBS1fE2nRfo60-PMVEI6MB_X3CUNOQ4KkkdOje2tx2cdGUNFMiomERDrwSDolOiljbHrfSutRHpSjLacXl3m7HlUOFeCa-uMSuhLJ8-kX5_VVjHBhnsDZSCyT7duS0YZRAfnO2Ikq6KCx0bmHXWZXyEQKRRJRdOWkQU08XJwB6Ny-PfLmHd8K4U8vB2keU9CpPFWT_i7vlVMFlWn1ROROK9kT_P_4Bcs1smaDKK55oCdHJGVVtU0r_AAAAAU7LTEIA", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", "DISABLE")
BOT_IMG = getenv("BOT_IMG", "https://telegra.ph/file/2c3097ae03f950800a66f.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5323266323").split()))
