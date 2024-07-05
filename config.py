import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20134071"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2bc877ca2f7fe6e01f1b9f8bc110b806")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Rdteach:Abcd@123@rdteach123.r7cowgr.mongodb.net/?retryWrites=true&w=majority&appName=Rdteach123")
