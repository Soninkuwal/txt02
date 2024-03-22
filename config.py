import os

API_ID = API_ID = 20945078

API_HASH = os.environ.get("API_HASH", "93f6b8ce4bb0ab61b4c7e42187f2aa64")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6298609764:AAHZWQcHTq5DlmRH1TvBCRE9_gxW_5UqXnk")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1664376941))

LOG = -1002057338886

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1664376941,1139197196").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


