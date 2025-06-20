import asyncio
from aiohttp import ClientSession
from Zaid import app, clients  # adjust import if needed

aiosession = None

async def start_all():
    global aiosession
    aiosession = ClientSession()

    # Start the bot
    await app.start()
    print("Bot Started ✅")

    # Start all string session clients
    for client in clients:
        await client.start()
        print(f"{client.name} Started ✅")

    print("All Clients and Bot are up and running!")

    await idle()  # Keep the program running

    # Cleanup on shutdown
    await app.stop()
    for client in clients:
        await client.stop()
    await aiosession.close()
    print("All stopped gracefully!")

if __name__ == "__main__":
    from pyrogram import idle
    asyncio.run(start_all())
