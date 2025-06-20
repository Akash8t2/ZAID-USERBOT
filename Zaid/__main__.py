import asyncio
import importlib
import logging
import traceback

from aiohttp import ClientSession
from pyrogram import idle
from Zaid import app, clients, ids
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
import Zaid  # for aiosession global

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s — %(levelname)s — %(name)s — %(message)s",
)
logger = logging.getLogger("ZAID-STARTUP")

async def start_bot():
    # initialize session
    Zaid.aiosession = ClientSession()

    # start the main bot
    await app.start()
    logger.info("Bot started ✅")

    # import all modules with error catching
    for module_path in ALL_MODULES:
        try:
            importlib.import_module(module_path)
            logger.info(f"✅ Imported module: {module_path}")
        except Exception as e:
            logger.error(f"❌ Failed to import {module_path}:\n{traceback.format_exc()}")

    # start all user‐clients
    for cli in clients:
        try:
            await cli.start()
            me = await cli.get_me()
            await join(cli)
            ids.append(me.id)
            logger.info(f"🔥 Client started: {me.first_name} ({cli.name})")
        except Exception:
            logger.error(f"⚠️ Client {cli.name} failed:\n{traceback.format_exc()}")

    logger.info("✅ All systems up. Awaiting events…")
    await idle()

    # graceful shutdown
    await app.stop()
    for cli in clients:
        await cli.stop()
    await Zaid.aiosession.close()
    logger.info("💤 Shutdown complete.")

if __name__ == "__main__":
    asyncio.run(start_bot())
