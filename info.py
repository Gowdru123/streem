import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '25502576'))
API_HASH = environ.get('API_HASH', 'f0f35dbb5b0081cdc8d3c9d5383c4628')
BOT_TOKEN = environ.get('BOT_TOKEN', "6274599665:AAFTSoJTSLMweccwtQB9Z8IgWQrbIfaqv1s")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 180))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/43e6c59479c7d869bec2e.jpg https://graph.org/file/64804ede93c64c292a842.jpg https://graph.org/file/e1fa4e58918c8e8d5aa0a.jpg https://graph.org/file/bad5da58bb38181693a7a.jpg https://graph.org/file/0a930db0eb217e430c4cf.jpg https://graph.org/file/c2b39ede6dcdbacbf6289.jpg https://graph.org/file/a713b8db5df493b853cad.jpg https://graph.org/file/aae6f3c9135eacb01744c.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/efd525bc133e1cbd0c966.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/98168a0fe0764b10fe1ea.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/c71f7bc667122cd1be418.jpg")
VRFIED_IMG = environ.get("VRFIED_IMG", "https://graph.org/file/929591e4ecf9d10535d32.jpg")
VRFY_IMG = environ.get("VRFY_IMG", "https://graph.org/file/e5fd5f7ca1acbf95785ae.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5123039648').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001821450983').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '6093431204').split()]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '0')
reqst_channel = environ.get('REQST_CHANNEL_ID', '0')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://yogeshchy9997:yogeshchy9997@cluster0.nxr4drz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Sujan_BotZ")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'vnshortener.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '6c5db31980885e46221e90106f1d47b8295aa0f8')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001767829947').split()]
MAX_B_TN = environ.get("MAX_B_TN", "10")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8000")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+aSW3ErAd9zwwMGY1')
SPRT_CHNL = environ.get('SPRT_CHNL', 'https://t.me/Sujan_BotZ')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Sujan_BotZ')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/How_2_Download_From_TeraBox/5714')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', 'https://t.me/How_2_Download_From_TeraBox/5714')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ BaBy ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001870515303'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Sujan_BotZ')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LANGUAGES = ["malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

#Direct Link Generator By @AB_BotZ_Update
DIRECT_GEN_DB = int(environ.get("DIRECT_GEN_DB", "-1001731526413")) # Enter your channel id
DIRECT_GEN_URL = environ.get("DIRECT_GEN_URL", "https://autofilter-file2link-bot.onrender.com/") # https://example.com/
DIRECT_GEN = bool(DIRECT_GEN_DB and DIRECT_GEN_URL)
