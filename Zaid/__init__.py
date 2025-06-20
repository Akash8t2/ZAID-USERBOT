from pyrogram import Client
from config import (
    API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN,
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4,
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8,
    STRING_SESSION9, STRING_SESSION10
)
from datetime import datetime
import time

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
clients = []
ids = []
aiosession = None  # Will be set inside main.py

# Ensure OWNER_ID is in sudo list
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# Use default fallback if missing
if not API_ID:
    print("WARNING: API ID not found, using fallback.")
    API_ID = 6435225

if not API_HASH:
    print("WARNING: API HASH not found, using fallback.")
    API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
    print("ERROR: BOT TOKEN not found. Add it in config.py!")

# Main bot (with plugin root for commands)
app = Client(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Zaid/modules/bot"),
    in_memory=True,
)

# User clients (STRING_SESSION-based)
session_strings = [
    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4,
    STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8,
    STRING_SESSION9, STRING_SESSION10
]

for i, session in enumerate(session_strings, start=1):
    if session:
        print(f"Client{i}: Found. Starting 📳")
        clients.append(Client(
            name=f"cli{i}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="Zaid/modules")
        ))
