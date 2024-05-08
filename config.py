import os

API_ID = API_ID = 29586300

API_HASH = os.environ.get("API_HASH", "7ac7f31dabaaec3ead510305e39aa250")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6563503169:AAFnyyUfInqRRzHJFpnNOQUG9aDi7Qd7M9Y")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7097107098))

LOG = -1002065274853

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


