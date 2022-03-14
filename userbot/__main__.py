# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
# by rendy
""" Userbot start point """

import sys
from importlib import import_module

from telethon.tl.functions.channels import InviteToChannelRequest
from userbot import ALIVE_NAME, BOT_USERNAME, BOT_VER, BOTLOG_CHATID, LOGS, UPSTREAM_REPO_BRANCH, bot
from userbot.modules import ALL_MODULES
from userbot.utils.tools import hadeh_ajg
try:
    for module_name in ALL_MODULES:
        imported_module = import_module("userbot.modules." + module_name)
    bot.start()
    LOGS.info(f"⚡Bagaskara-Userbot⚡ ⚙️ V{BOT_VER} [ TELAH DIAKTIFKAN! ]")
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


async def bagas_ubot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"⚡ Bagaskara-Userbot Berhasil Diaktfikan ⚡\n╼┅━━━━━╍━━━━━┅╾\n❍▹ Bot Of : {ALIVE_NAME}\n❍▹ BotVer : {BOT_VER} {UPSTREAM_REPO_BRANCH}\n╼┅━━━━━╍━━━━━┅╾",
            )
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(hadeh_ajg())
bot.loop.run_until_complete(bagas_ubot_on())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
