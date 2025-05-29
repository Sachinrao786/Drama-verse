#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7609037936:AAGtZLZnXusAcJ7UxZW0IDhbWuFR4aNjobc")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "25236931"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fc138979f4f7f144a06b5330755e7610")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002604560162"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7607147920"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://kaido0099878:XR5TnmaT55neAJ2U@cluster0.ksifz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Drama_Verse_Bot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002315092712"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002492194041"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ae5ad0ac386e5b8e8288b-66495730df0ccbfae9.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/9b316094cb97aa52102b1-9bf1affaa24d7d8fcc.jpg")

#text
HELP_TXT = "<blockquote><b>Hi Dude!\n\nTo use this bot you just have to join both channels that's it..\nWatch Tutorial to open Link - <a href=https://t.me/your_dramas_hindi/2>Clickhere</a></b></blockquote>"
ABOUT_TXT = "<blockquote><b><i>About Us..\n\n‣ Made for : <a href=https://t.me/@Its_Mr_Bunny>ClickHere</a>\n‣ Owned by : @Its_Mr_Bunny\n‣ Maintained by : @Its_Mr_Bunny\n‣ Developed by : @Its_Mr_Bunny\n\n Adios !!</i></b></blockquote>"
SHORT_MSG = "<b>⌯ ʏᴏᴜʀ ʟɪɴᴋ ɪꜱ ʀᴇᴀᴅʏ, ᴋɪɴᴅʟʏ ᴄʟɪᴄᴋ ᴏɴ ᴏᴘᴇɴ ʟɪɴᴋ ʙᴜᴛᴛᴏɴ..</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\n\nᴘᴏᴡᴇʀᴇᴅ ʙʏ : <a href=https://t.me/Hindi_Dub_Dramas>𝐇𝐢𝐧𝐝𝐢 𝐃𝐮𝐛 𝐃𝐫𝐚𝐦𝐚𝐬</a></b>")
try:
    ADMINS=[7035751998]
    for x in (os.environ.get("ADMINS", "7035751998").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ for content ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "LinkCents.com")
SHORT_API = os.environ.get("SHORTNER_API", "764330bd9ab252522b1d31b98e6244cf58936f57")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - @Hindi_Dub_Dramas"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "600"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(1418213560)

LOG_FILE_NAME = "filesharingbot.txt"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
