import os

API_ID = API_ID = 29768900

API_HASH = os.environ.get("API_HASH", "6a56e5c2383dc7b85210febe60b9f229")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6310775347:AAG403j7xRVA-JRILEBLxXKxzHhFhGxbjFI")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5986670447))

LOG = -1001778815195

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5986670447").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


