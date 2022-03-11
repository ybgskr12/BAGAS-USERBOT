# credit by @kyuraxx
# own kyura

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.djancok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI KALAU DEPLOY BAGASKARA-USERBOT**")
    sleep(1)
    await typew.edit("**JOIN JUGA SUPPORT NYA DJANCOK!!**")
    sleep(1)
    await typew.edit("**DEPLOY DOANG GA JOIN**")
    sleep(1)
    await typew.edit("**DASAR DJANCOK!**")


@register(outgoing=True, pattern='^.vcs(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH LONTE APLIKASI**")
    sleep(1)
    await typew.edit("**KALO GA PUNYA HARGA DIRI**")
    sleep(1)
    await typew.edit("**GAUSAH JUAL DIRI GOBLOK**")
    sleep(1)
    await typew.edit("**KASIAN ORANG TUA LU TOLOL**")
    
    
CMD_HELP.update({
    "animasi2":
    "`.djancok`; `.vcs`\
    \nUsage: liat aja."
})
