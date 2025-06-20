import asyncio
import importlib
from aiohttp import ClientSession
from pyrogram import idle
from Zaid import app, clients, ids
from Zaid.helper import join
from Zaid.modules import ALL_MODULES
import Zaid  # for setting aiosession globally

async def start_bot():
    Zaid.aiosession = ClientSession()

    await app.start()
    print("LOG: Bot started ✅")

    # Load all modules dynamically
    for module in ALL_MODULES:
        importlib.import_module("Zaid.modules." + module)
        print(f"✅ Imported: {module}")

    # Start all user clients
    for cli in clients:
        try:
            await cli.start()
            me = await cli.get_me()
            await join(cli)
            print(f"🔥 Client started: {me.first_name}")
            ids.append(me.id)
        except Exception as e:
            print(f"⚠️ Client failed: {e}")

    print("✅ All systems operational. Waiting for events.")
    await idle()

    # Cleanup on shutdown
    await app.stop()
    for cli in clients:
        await cli.stop()
    await Zaid.aiosession.close()
    print("💤 All stopped cleanly.")

if __name__ == "__main__":
    asyncio.run(start_bot())
