from pyrogram import Client
from pyrogram.enums import ParseMode
import config
import os

app = Client(
    "rose_basic_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins={"root": "plugins"},
    parse_mode=ParseMode.HTML,
)

if __name__ == "__main__":
    print("Bot started as @KRIYANSH_CHOUDHARY's Rose Basic Bot")
    app.run()
