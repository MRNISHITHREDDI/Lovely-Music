import asyncio
from pytgcalls import idle
from driver.lovely import call_py, bot

async def lovely_bot():
    print("Lovely: STARTING BOT CLIENT")
    await bot.start()
    print("Lovely: STARTING PYTGCALLS CLIENT")
    await call_py.start()
    await idle()
    await pidle()
    print("Lovely: STOPPING BOT & USERBOT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(lovely_bot())
