from os import environ 

class Config:
    API_ID = environ.get("API_ID", "5128432")
    API_HASH = environ.get("API_HASH", "5436f836f2887d3e680628ff1010e949")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7602790697:AAH2NqK2gu2suk_ZTsUZ-jvZp4jcY3A322s") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://DOXDKGBOT:9pqvIrVMgpqdMsmf@doxdkgbot.klwdk.mongodb.net/?retryWrites=true&w=majority&appName=DOXDKGBOT")
    DATABASE_NAME = environ.get("DATABASE_NAME", "DOXDKGBOT")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1440378158').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
