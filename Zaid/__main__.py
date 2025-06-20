import asyncio
import importlib
from aiohttp import ClientSession
from pyrogram import Client, idle
from Zaid import app, clients, ids, aiosession
from Zaid.helper import join
from Zaid.modules import ALL_MODULES

async def start_bot():
    global aiosession
    aiosession = ClientSession()

    await app.start()
    print("LOG: Bot token found. Booting...")

    for module in ALL_MODULES:
        importlib.import_module("Zaid.modules." + module)
        print(f"Successfully imported: {module} 💥")

    for cli in clients:
        try:
            await cli.start()
            me = await cli.get_me()
            await join(cli)
            print(f"Started client: {me.first_name} 🔥")
            ids.append(me.id)
        except Exception as e:
            print(f"Error starting client: {e}")

    print("All clients and bot are up ✅")
    await idle()

    await app.stop()
    for cli in clients:
        await cli.stop()
    await aiosession.close()
    print("Shutdown complete ✅")

if __name__ == "__main__":
    asyncio.run(start_bot())
