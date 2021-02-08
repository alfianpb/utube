import os

class Config:

    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    
    SESSION_NAME = "alfianytupload"

    API_ID = "2030112"

    API_HASH = "0bc033cdc59296e1906d6562a7295d67"

    CLIENT_ID = os.environ.get("CLIENT_ID")

    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")

    BOT_OWNER = "1477145315"

    AUTH_USERS = [1477145315, 952774613]
    
    VIDEO_DESCRIPTION = ""
    
    VIDEO_CATEGORY = "0"
    
    VIDEO_TITLE_PREFIX = ""
    
    VIDEO_TITLE_SUFFIX = ""
    
    DEBUG = bool("")
    
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ['private', 'public', 'unlisted']:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"



