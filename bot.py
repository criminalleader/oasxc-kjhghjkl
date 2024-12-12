from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import *

import asyncio
from pyrogram import idle
from lazybot import lazydeveloperxbot

from util.keepalive import ping_server
from lazybot.clients import initialize_clients

import logging
import logging.config
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

PORT = "8080"
lazydeveloperxbot.start()
loop = asyncio.get_event_loop()

async def lazyDeveloperStartBOT():
    print('\n')
    print('|==> Powered by - The one & Only LAZYDEVELOPER <==||')
    print('//// Initalizing Telegram Bot  ')
    usr_bot_me = await lazydeveloperxbot.get_me()
    lazydeveloperxbot.uptime = datetime.now()
    await initialize_clients()
    print('//// Processing basic inits....  ')
    print('================================  ')
    print('================================  ')
    # if ON_HEROKU:
    #     asyncio.create_task(ping_server())


    # Note => This is old method and it is not compatible with the latest telegram version (( YT or TG : @LazyDeveloperr ))
    # So replacing the force sub method with req to join feature 🚀 (( YT or TG : @LazyDeveloperr ))
    #  
    # if FORCE_SUB_CHANNEL:
    #     try:
    #         link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
    #         if not link:
    #             await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
    #             link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
    #         self.invitelink = link
    #     except Exception as a:
    #         self.LOGGER(__name__).warning(a)
    #         self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
    #         self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL}")
    #         self.LOGGER(__name__).info("\nBot Stopped. https://t.me/LazyDeveloper for support")
    #         sys.exit()
    # if FORCE_SUB_CHANNEL2:
    #     try:
    #         link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
    #         if not link:
    #             await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
    #             link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
    #         self.invitelink2 = link
    #     except Exception as a:
    #         self.LOGGER(__name__).warning(a)
    #         self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
    #         self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL2}")
    #         self.LOGGER(__name__).info("\nBot Stopped. https://t.me/LazyDeveloper for support")
    #         sys.exit()
    
    try:
        db_channel = await lazydeveloperxbot.get_chat(CHANNEL_ID)
        lazydeveloperxbot.db_channel = db_channel
        test = await lazydeveloperxbot.send_message(chat_id = db_channel.id, text = "Test Message")
        await test.delete()
    except Exception as e:
        lazydeveloperxbot.LOGGER(__name__).warning(e)
        lazydeveloperxbot.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
        lazydeveloperxbot.LOGGER(__name__).info("\nBot Stopped. Join channel https://t.me/LazyDeveloper for support")
        # sys.exit() #if bot is admin & you are getting admin issue again and again then u can also remove this line of code 

    lazydeveloperxbot.set_parse_mode(ParseMode.HTML)
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    lazydeveloperxbot.LOGGER(__name__).info(f"[[[[[||==> ❤ with love  llı🎉 L͙a͙z͙y͙D͙e͙v͙e͙l͙o͙p͙e͙r͙r͙ 🍿ıll with love ❤ <==||]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    print("[[[[[[[[[[[[[[[[[[[[[[[❤]]]]]]]]]]]]]]]]]]]]]]]")
    lazydeveloperxbot.username = usr_bot_me.username
    #web-response
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(lazyDeveloperStartBOT())
        logging.info('-----------------------🧐 Service running in Lazy Mode 😴-----------------------')
        logging.info('=================================================================================')
    except KeyboardInterrupt:
        logging.info('-----------------------😜 Service Stopped Sweetheart 😝-----------------------')
