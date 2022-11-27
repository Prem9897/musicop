from os import getenv

from dotenv import load_dotenv

admins = {}

load_dotenv()

SESSION_NAME = getenv("SESSION_NAME", "BQAiOCyELShHUzX-TTFDWkaSYQ1UTjZaLQ8YVCIuyQNlScl2aqaeE-ofsZhMuUwIrE0BmTWt1IgcMqb4bvCVPomcg1de1kM3hILhPpGu-wRm-mqJqS5MQwj6ptarRYS_ATCI2qKt4lMZ3Nxv9I3OgI-M2PBX-KoqivNCYjRVoTNwV-kzKTvI_Z14CCjCEkx0ouPPcX0XQQqb5057eOzSOkjfYkK1W_G3mkypkf91OzrItqTE4DsmU8NyY6QnSMZF3lSZgVl9KX9XKVMyIciQZrkmjZnoUQ4ryoL6-yFma4lb1GFjiixW3SL-orlakCDELL_cxeJln9G5lKBXxcubxpUDAAAAATDvfKMA")
BOT_TOKEN = getenv("BOT_TOKEN", "5545963604:AAFaDB-N19p1c9mPBruvzScQPdiJqM-7x30")
API_ID = int(getenv("API_ID", "10448562"))
API_HASH = getenv("API_HASH", "4a8a640bb154fc59227ccbcb5d5ce612")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "5400"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Aman:Aman@cluster0.gt2bc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5497627952").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001747540803'))
ASS_ID = int(getenv("ASS_ID", "1446583656"))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5497627952").split()))
BOT_ID = int(getenv("BOT_ID", "5545963604"))
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "800"))
